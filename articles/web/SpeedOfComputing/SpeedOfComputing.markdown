
# Speed Of Computing

Goal: accumulate all reference material to answers questions such as: "You are running a web service that does X, how many servers do you need?".

## Example Question

You run a web service where 1000 users upload a 700 kB picture every second (assume that nothing else happen on this system). How many frontend and backend machines do you need?

### Tentative Answer

The bandwidth required is 1000 * 700 * (2**10) = 0.667 GBps = 5.34 Gbps.
Since a frontend instance will likely handle ~ 1Gbps, you need 6 instances at the very least.

Now, you can assume that those frontend instances will pass that data to backend machines. Since you can expect a much higher throughput in machine-to-machine data transfer (given the they are in the same cloud), you only need 1 backend instance to handle that load (assuming 10Gbps transfer data rate).

However, that backend will need to store that data. Assuming sequential writes, you can write 1 picture in ~2 ms (remember that if you cannot assume sequential writes, every seek on a non-SSD drive will take ~10ms). This means that you need at least two backend instances in order to handle the write speed. You probably need to shard the data across many more machines if you do not want to run out of space, but 2 machines can handle the _load_.

## Reference Table: Speed of A Computer

        L1 cache reference                            0.5 ns
        Branch mispredict                             5   ns
        L2 cache reference                            7   ns                        (14x L1 cache)
        Mutex lock/unlock                            25   ns
        Main memory reference                       100   ns                        (20x L2 cache, 200x L1 cache)
        Creating a new thread                     5,000   ns
        
        Send 1K bytes over 1 Gbps network        10,000   ns    0.01 ms  100  MB/s
        
        Read 1 MB sequentially from memory      250,000   ns    0.25 ms  4    GB/s
        
        Round trip within same datacenter       500,000   ns    0.5  ms
        
        Read 1 MB sequentially from SSD                                  200  MB/s
        Write 1 MB sequentially to SSD                                   150  MB/s
        Read 4K randomly from SSD                                        65   MB/s
        Write 4K randomly from SSD                                       20   MB/s
        
        Write 1 MB sequentially to HD        10,000,000   ns   10    ms  100  MB/s
        Read 1 MB sequentially from HD       20,000,000   ns   20    ms  50   MB/s  (80x memory, 20X SSD)
        Read 4K randomly from HD                180,000   ns    0.18 ms  0.75 MB/s
        
        Intra rack Datacenter operation                         0.5  ms?
        Inter-rack datacenter operation                         5    ms?
        Disk seek                                              10    ms             (20x datacenter roundtrip)
        Send packet US-West->US-East->US-West                  30    ms
        Send packet CA->Netherlands->CA                       150    ms


Table credit: 

- [https://gist.github.com/jboner/2841832](https://gist.github.com/jboner/2841832)
- [http://norvig.com/21-days.html#answers](http://norvig.com/21-days.html#answers)
- [SDD read/write speed](http://www.tomshardware.com/reviews/ssd-upgrade-hdd-performance,3023-6.html)
- [SDD read/write speed 2](http://hdd.userbenchmark.com/Seagate-Barracuda-720014-3TB/Rating/1374)

A funny thing that has been pretty much constant since the beginning of computing is that "you can read the whole content of the computer's memory in about 1 second". It was true in the 1970s, and it is still true today (note that the size of the memory has grown exponentially).

## Reference Table: How Much Traffic Can Machine X Handle

        Public IP Amazon EC2 Instance                    1  Gbps
        Private machine-to-machine Amazon EC2 Instance   10 Gbps

Those numbers could be slightly off (see references below). Please do update me if wrong :).
        
- [ServerFault](http://serverfault.com/questions/570879/1-73-gbps-at-best-on-an-amazon-ec2-10-gigabit-instance)
- [WowZa](http://www.wowza.com/forums/showthread.php?34985-Maxing-out-a-c3-8xlarge-instance-500-1000-or-2000-simultaneous-viewers/page2)

## Reminder: SI Units

**Time:**

        Second      (s)   1
        Millisecond (ms)  1e-3
        Microsecond (μs)  1e-6
        Nanosecond  (ns)  1e-9
        Picosecond  (ps)  1e-12

**Data:**

        Byte       (b)   1       2^0
        Kilobyte   (kB)  1e3     2^10
        Megabyte   (MB)  1e6     2^20
        Gigabyte   (GB)  1e9     2^30
        Terabyte   (TB)  1e12    2^40
        Petabyte   (PB)  1e15    2^50

Fun distinctions:

- b is **bit** (1 bit), B is **byte** (8 bits). 'b' or bit is rarely used, prefer B / bytes. The exception is in networking, where the speed is usually expressed in bits, such as 1Gbps (1 gigabit per second = 1e9 bits / s).
- kB = 1000 bytes or 1024 bytes depending on context. 1000 is the proper SI quantity, in computing 1024 is generally used (since it is a power of 2). In doubt, kB = 1024 bytes.
- kb ~= 125 bytes (1000 bits). Generally speaking, _avoid using kb_, use kB instead.
        
## Visualization Chart

![speed_chart.png](../../static/speed_chart.png)
[Image Credit](https://gist.github.com/hellerbarde/2843375)

