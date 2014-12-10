# TCP / HTTP Listening On Ports: How Can the Server Handle Multiple Connections on the Same Port

So, what happens when a server listen for incoming connections on a TCP port? For example, let's say you have a web-server on port 80. Let's assume that your computer has the public IP address of 24.14.181.229 and the person that tries to connect to you has IP address 10.1.2.3. This person can connect to you by opening a TCP socket to 24.14.181.229:80. Simple enough.

Intuitively (and wrongly), most people assume that it looks something like this:

        Local Computer    | Remote Computer
        --------------------------------
        <local_ip>:80     | <foreign_ip>:80

        ^^ not actually what happens, but this is the conceptual model a lot of people have in mind.

This is intuitive, because from the standpoint of the client, he has an IP address, and connects to a server at IP:PORT. Since the client connects to port 80, then his port must be 80 too? This is a sensible thing to think, but actually not what happens. If that were to be correct, we could only serve one user per foreign IP address. Once a remote computer connects, then he would hog the port 80 to port 80 connection, and no one else could connect. 

Three things must be understood:

1.) On a server, a process is _listening_ on a port. Once it gets a connection, it hands it off to another thread. The communication never hogs the listening port. 

2.) Connections are uniquely identified by the OS by the following 5-tuple: (local-IP, local-port, remote-IP, remote-port, protocol). If any element in the tuple is different, then this is a completely independent connection.

3.) When a client connects to a server, it picks a _random, unused high-order source port_. This way, a single client can have up to ~64k connections to the server for the same destination port.

So, this is really what gets created when a client connects to a server:

        Local Computer   | Remote Computer           | Role
        -----------------------------------------------------------
        0.0.0.0:80       | <none>                    | LISTENING
        127.0.0.1:80     | 10.1.2.3:<random_port>    | ESTABLISHED

## Looking at What Actually Happens

First, let's use netstat to see what is happening on this computer. We will use port 500 instead of 80 (because a whole bunch of stuff is happening on port 80 as it is a common port, but functionally it does not make a difference).

        netstat -atnp | grep -i ":500 "

As expected, the output is blank. Now let's start a web server:

        sudo python3 -m http.server 500

Now, here is the output of running netstat again:

        Proto Recv-Q Send-Q Local Address           Foreign Address         State  
        tcp        0      0 0.0.0.0:500             0.0.0.0:*               LISTEN      - 

So now there is one process that is actively listening (State: LISTEN) on port 500. The local address is 0.0.0.0, which is code for "listening for all". An easy mistake to make is to listen on port 127.0.0.1, which will only accept connections from the current computer. So this is not a connection, this just means that a process requested to bind() to port IP, and that process is responsible for handling all connections to that port. This hints to the limitation that there can only be one process per computer listening on a port (there are ways to get around that using multiplexing, but this is a much more complicated topic). If a web-server is listening on port 80, it cannot share that port with other web-servers.

So now, let's connect a user to our machine:

        quicknet -m tcp -t localhost:500 -p Test payload.

This is a simple script (https://github.com/grokit/quickweb) that opens a TCP socket, sends the payload ("Test payload." in this case), waits a few seconds and disconnects. Doing netstat again while this is happening displays the following:

        Proto Recv-Q Send-Q Local Address           Foreign Address         State  
        tcp        0      0 0.0.0.0:500             0.0.0.0:*               LISTEN      -
        tcp        0      0 192.168.1.10:500        192.168.1.13:54240      ESTABLISHED -

If you connect with another client and do netstat again, you will see the following:

        Proto Recv-Q Send-Q Local Address           Foreign Address         State  
        tcp        0      0 0.0.0.0:500             0.0.0.0:*               LISTEN      -
        tcp        0      0 192.168.1.10:500        192.168.1.13:26813      ESTABLISHED -

... that is, the client used another random port for the connection. So there is never confusion between which connections should send to which port -- every connection has a unique 5-tuple. The TCP/IP packets head out with the (foreign ip, foreign port) in the IP header, and it is the right place since it is the right destination (IP identifies the client) and the right port (same as the random port that the initial message came in with, which was randomly picked by the client and guaranteed to be unique).
