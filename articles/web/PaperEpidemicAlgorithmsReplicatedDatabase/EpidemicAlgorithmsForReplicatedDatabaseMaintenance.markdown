
# Epidemic Algorithms for Replicated Database Maintenance

The paper presents a way to efficiently maintain consistency for data replicated across many sites. It is the earliest known "gossip" algorithm.

The problem to solve is, given N sites, one of them receives change in their data. This change must eventually be replicated to the N sites. Which is the best way to proceed? An obvious answer is to simply broadcast from the changed node to all nodes. But this simply will not scale if you have N >> 10k nodes in your system (the node that broadcasts the change has to establish N connections and send N times, which could take an unreasonable amount of time while most of the nodes stay idle when they could be helping out). Also, how do you ensure that all nodes correctly got the update? The challenge is to be highly reliable whilst scaling gracefully as the number of nodes in the system (N) grows.

Gracefully scaling as the number of site (N) increases means:

- Low time for an update to reach all sites.
- Small amount of bandwidth consumed (low bound: N x size of change).

The novelty of the paper is to use the mathematic foundation underlying the theory of epidemics (which is well established) to distributed systems database replication.

**Keywords**: gossip, gossip protocols, distributed computing, distributed databases, randomized algorithms.

**Link to paper**: [http://dl.acm.org/citation.cfm?id=41841](http://dl.acm.org/citation.cfm?id=41841), [full pdf](http://www.textfiles.com/bitsavers/pdf/xerox/parc/techReports/CSL-89-1_Epidemic_Algorithms_for_Replicated_Database_Maintenance.pdf).

## Some (Naive) Strategies 

One way mentioned in the introduction is to broadcast the change to all servers, which simply does not scale: any change result in N messages to be sent for the node whose data changed, which is prohibitive since N is very large.

Another way is to introduce a topology in our servers. Let's say the N servers are arranged in a ring, then upon an update, node[i] sends the message to node[i+1] until the last node is reached, which sends an ACK to node[0]. This is much better for the changed node since only 1 message needs to be sent. Note that there is still, in total, N+1 messages sent in the system, but at least the work is _distributed_ against all nodes -- it can be done without having a node being overloaded and most nodes doing nothing. The obvious problem with this approach is that if one node is down in the right, the whole thing fails. You can introduce different topologies (e.g skip-lists, trees) which mitigates that, but fixed topologies can quickly become complex and have messages that fail to reach all nodes.

The insight of the paper is that using _randomized algorithm_ (selecting nodes at random and syncing information) achieves both efficiency gain (only syncing with 1 node per period of time at maximum) and fast convergence as the probability that the information has not converged diminishes exponentially as time increases. 

## Strategies Introduced by the Paper 

### Direct Mail (Simple Broadcast)

The direct mail strategy is a simple broadcast model. As mentioned previously, this suffers from having to send N messages from the same server for every update.

Another problem is that the update is not very reliable for the two following reasons:

1.) In a large system, it is reasonable to expect that not all nodes know about all other nodes -- some nodes have somewhat older information about the members of the network. If a node-A does not know about node-B, node-B will never get the update. 

2.) Since N is large, is it necessary to store the messages in a queue while the N messages are sent. If a crash occurs in that node before the queue is entirely sent, then some nodes will not get the message. If a target node is unreachable for the whole time it takes to empty the queue, the nodes that were unreachable will not get the message.

### Anti-Entropy (Simple Epidemic)

Each server runs the following algorithm:

- At every time interval t, pick a _random_ server and resolve differences with that server (sync information).

This is extremely simple and elegant. 

**Number of messages / synchronizations**: At every time period t, every node is only (in a statistical sense) syncing with 2 nodes: 1 that it picked at random, and 1 incoming sync request since the N other nodes select the current node with probability 1/N.

**Time to reach all nodes**: At t0, the state change in a node. At t1, this node _at least_ syncs with 1 node, so 2 nodes have the change. At t2, those two nodes synchronize with at least 2 other nodes, bringing the total of nodes that know about the change to 4. And so it goes to 8, 16, 32, 64... The amount of time before all nodes about the change is log2(N) time periods.

**Failure tolerance**: The information propagates exponentially in the system. If 16 nodes know about a change, and those nodes will randomly get selected for syncing, the only way the information does not get propagated is that if somehow those 16 nodes fail at the same time. So it is possible that the information does not propagate if the initial, or 2 initial, or 4 initial nodes fail at the same time, which is unlikely. Failure of the first node to send the information cannot be helped in any case, so the failure tolerance is high.

**Topology**: It supports all topologies. In addition, if you add or remove nodes dynamically in the system, it does not matter. It is eventually consistent.

However, the cost of resolving difference between two nodes is much higher than sending a message with the single message/value that changed. This can be mitigated by using smart checksumming (e.g: merkle tree) and only sending the differing information over the network.

Anther optimization is to keep a list of recently changed values. It is possible to know the expected amount of time t' before an update reaches all nodes. All node keep a buffer of the values that changed in the last t' time, and upon resolving differences exchange only those values and do a full sync only if the state is different at the two nodes.

#### Which Random Distribution to Use

A normal distribution works, but using heuristics improves performance, For example, factoring-in which are the closest server to a node for syncing helps reduce propagation delay.

#### How to Deal with Deletion

Simply introduce the concept of a "dead key/value". Pass this information around as if it is a normal update. You can calculate the amount of time where you know the deletion has propagated with a confidence value of X sigmas (let's say at time t-del), then when timestamp of a dead key/value - t-now > t-del, wipe the key/value from the node.

#### How to Know Which Values to Keep if Receive Two Conflicting Values?

You have to introduce timestamps, and those timestamps have to be globally conherent. You always keep the value associated with the greatest timestamp.

### Complex Epidemics

The principle behid complex epidemics methods is the same as with anti-entrophy, but with a bunch of optimizations thrown in. 

For example, you can stop synchronizing a change when you are confident most people got it and other people are spreading that change. You can never be 100% confident, but complex epidemics relies on a form of anti-entrophy where you have strong guarantees to run at a slower pace to make sure that eventually all the information become consistent.

@@resume.p.8 -- not done reading --
