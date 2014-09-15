
# DNS (Domain Name System) in a Nutshell

The DNS is used to translate a FQDN (e.g: http://www.grokit.ca) into an IP address (e.g: 74.125.20.121). This is necessary since FQDNs themselves are not used to convey data on the Internet, IP addresses are. FQDNs are used because we, humans, can remember better long series of letters than long series of numbers. Therefore, we built a system to allow us to type a (human-readable) FQDN in a browser that the computer covertly resolves into an IP address. This IP address can actually be used to convey data on the Internet.

## Looking at the bits on The Wire

After starting a Wireshark capture, I issue a ping to www.grokit.ca (ping is an ICMP protocol command, which will be covered in a separate article -- the thing to remember here is that ping needed to know the IP address associated with the queried FQDN so it had to do a DNS lookup).

    43  1.161347000 192.168.1.8 192.168.1.1 DNS 73  Standard query 0x338a  A www.grokit.ca
    52  1.259355000 192.168.1.1 192.168.1.8 DNS 123 Standard query response 0x338a  CNAME ghs.googlehosted.com A 74.125.28.121

192.168.1.1 is my router, and why the DNS request goes to my router instead of a root DNS server is an advanced topic. For now, just assume that my router is the DNS server.

So, here is the request:

    43  1.161347000 192.168.1.8 192.168.1.1 DNS 73  Standard query 0x338a  A www.grokit.ca
    ==>
    0000   00 26 62 ae 71 b4 a0 88 b4 e4 31 64 08 00 45 00  .&b.q.....1d..E.
    0010   00 3b 10 a9 00 00 80 11 a6 af c0 a8 01 08 c0 a8  .;..............
    0020   01 01 c1 de 00 35 00 27 4d 15 33 8a 01 00 00 01  .....5.'M.3.....
    0030   00 00 00 00 00 00 03 77 77 77 06 67 72 6f 6b 69  .......www.groki
    0040   74 02 63 61 00 00 01 00 01                       t.ca.....

Up to "33 8a ..." it is just a standard IP-UDP message from 192.168.1.8 (my computer) to 192.168.1.1 (the DNS server).

Response from DNS server:

    00000000  33 8a 81 80 00 01 00 02  00 00 00 00 03 77 77 77 3....... .....www
    00000010  06 67 72 6f 6b 69 74 02  63 61 00 00 01 00 01 c0 .grokit. ca......
    00000020  0c 00 05 00 01 00 00 07  08 00 16 03 67 68 73 0c ........ ....ghs.
    00000030  67 6f 6f 67 6c 65 68 6f  73 74 65 64 03 63 6f 6d googleho sted.com
    00000040  00 c0 2b 00 01 00 01 00  00 00 44 00 04 4a 7d 1c ..+..... ..D..J}.
    00000050  79    

Let's break this down.

The DNS request starts at "03 77 77 77...". The '77' are of course ascii for 'www':

        >>> hex(ord('w'))
        '0x77'

... so the DNS request starts by sending the FQDN you are trying to resolve. The DNS answer has the following format:

        / NAME /
        +--+--+--+--+
        | TYPE      |
        +--+--+--+--+
        | CLASS     |
        +--+--+--+--+
        | TTL       |
        +--+--+--+--+
        | RDLENGTH  |
        +--+--+--+--+
        | RDATA     |
        +--+--+--+--+

[More info here](http://www.ccs.neu.edu/home/amislove/teaching/cs4700/fall09/handouts/project1-primer.pdf). So the data that interests us is RDATA.


## Simple DNS Script in Python

@@DO

# Epilogue

Now you understand the first step necessary for your browser to go from that easy to remember URL to the actual computer that contains the information. You have been using this mechanism dozens of times a day for decades, now you know how it works :).

# Appendix: DNS Root Servers

    Hostname            IP Addresses                      Manager
    a.root-servers.net  198.41.0.4, 2001:503:ba3e::2:30   VeriSign, Inc.
    b.root-servers.net  192.228.79.201                    University of Southern California (ISI)
    c.root-servers.net  192.33.4.12, 2001:500:2::c        Cogent Communications
    d.root-servers.net  199.7.91.13, 2001:500:2d::d       University of Maryland
    e.root-servers.net  192.203.230.10                    NASA (Ames Research Center)
    f.root-servers.net  192.5.5.241, 2001:500:2f::f       Internet Systems Consortium, Inc.
    g.root-servers.net  192.112.36.4                      US Department of Defence (NIC)
    h.root-servers.net  128.63.2.53, 2001:500:1::803f:235 US Army (Research Lab)
    i.root-servers.net  192.36.148.17, 2001:7fe::53       Netnod
    j.root-servers.net  192.58.128.30, 2001:503:c27::2:30 VeriSign, Inc.
    k.root-servers.net  193.0.14.129, 2001:7fd::1         RIPE NCC
    l.root-servers.net  199.7.83.42, 2001:500:3::42       ICANN
    m.root-servers.net  202.12.27.33, 2001:dc3::35        WIDE Project

DNS queries are issued as UDP requests on port 53. Nowadays, other protocols such as TCP are supported by most DNS servers, but the principle of the service is the same.

Tool to use to play with DNS: nslookup.
