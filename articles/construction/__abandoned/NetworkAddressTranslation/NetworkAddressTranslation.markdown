
# Network Address Translation (NAT)

Simple
 
Allows N computers to share the same IP address as seen from the outside of that network. A router maintains a table of the "outside" and "inside" IP addresse / port (http://www.techterms.com/definition/nat).
 
More Details
 
- Allows a single IP address to connect N computers to the internet under the NAT private network. Used to address the scarcity of IP addresses problem.
 
The NAT sits between the "home network" and outside network. The outside network only sees one IP address. When a computer in the network makes a request on the outside:
 
192.168.1.1:1234 ==> [NAT] ==> 10.1.2.3:2000
192.168.1.2:1234 ==> [NAT] ==> 10.1.2.3:2001
 
… the NAT changes the address in the TCP (or IP??) data. This way, N computers can use the same port, their message will make it to the destination. A message coming back will be disambiguated with the NAT (the NAT keeps the equivalency table) and sent to the right computer using the port (all inbound traffic comes to the same IP address).
 
One of the problem of this approach is that outside computer cannot initiate requests to a computer "inside the NAT": how to tell which of the computer inside the NAT that this message should be conveyed to? A computer inside the network has to register ("static NAT") the incoming port (e.g: 80) to the NAT, which makes it unavailable for incoming traffic to all the other computers in the private network. After the static NAT is set of a port, all traffic to this IP:PORT will be forwarded to that machine.
 
"NAT traversal" is used to alleviate some of these problems.
 
Refs
 
http://en.wikipedia.org/wiki/Network_address_translation
 
 
NAT Traversal, Hole Punching
 
http://en.wikipedia.org/wiki/NAT_traversal
http://en.wikipedia.org/wiki/TCP_hole_punching
http://en.wikipedia.org/wiki/UDP_hole_punching
 
# OLD
 
To avoid ambiguity in the handling of returned packets, a one-to-many NAT must alter higher level information such as TCP/UDP ports in outgoing communications and must maintain a translation table so that return packets can be correctly translated back. RFC 2663 uses the term NAPT (network address and port translation) for this type of NAT.

