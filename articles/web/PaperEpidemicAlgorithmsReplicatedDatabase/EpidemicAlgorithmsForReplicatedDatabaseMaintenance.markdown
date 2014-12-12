
# Epidemic Algorithms for Replicated Database Maintenance

The paper presents a way to efficiently maintain consistency for data replicated across many sites. It is the earliest known "gossip" algorithm paper.

The problem to solve is, given a system with N nodes, how do you make a change at a single node propagate to all other nodes?

An obvious answer is to simply broadcast from the changed node to all nodes. But this simply will not scale for large Ns (the node that broadcasts the change has to establish N connections and send N times, which could take an unreasonable amount of time while most of the nodes stay idle when they could be helping out). Also, how do you ensure that all nodes correctly got the update? The challenge is to be highly reliable whilst scaling gracefully as the number of nodes in the system grows.

Gracefully scaling as the number of node increases means:

- Low time for an update to reach all sites.
- Small amount of bandwidth consumed (low bound: N x size of change).
- Can be certain that all nodes will eventually get the change.

The novelty of the paper is to use the mathematic foundation underlying the theory of epidemics (which is well established) to distributed systems database replication.

**Keywords**: gossip, gossip protocols, distributed computing, distributed databases, randomized algorithms.

**Link to paper**: [http://dl.acm.org/citation.cfm?id=41841](http://dl.acm.org/citation.cfm?id=41841), [full pdf](http://www.textfiles.com/bitsavers/pdf/xerox/parc/techReports/CSL-89-1_Epidemic_Algorithms_for_Replicated_Database_Maintenance.pdf).

## Some (Naive) Strategies 

One way mentioned in the introduction is to broadcast the change to all servers, which simply does not scale: any change result in N messages to be sent for the node whose data changed, which is prohibitive since N is very large.

Another way is to introduce a topology linking the nodes. Let's say the N servers are arranged in a ring, then upon an update, node[i] sends the message to node[i+1] until the last node is reached. The last node then sends an ACK to node[0]. If the last node does not receive the ACK after a period of time, it tries to re-send. This is much better for the changed node since only 1 message needs to be sent. Note that there is still, in total, N+1 messages sent in the system, but at least the work is _distributed_ against all nodes -- it can be done without having a node being overloaded and most nodes doing nothing. The obvious problem with this approach is that if one node is down in the ring, the whole thing fails. You can introduce different topologies (e.g skip-lists, trees, ...) which mitigates problems, but fixed topologies can quickly become complex and it is hard to guarantee delivery to every single node in complex topologies.

The insight of the paper is that using _randomized algorithm_ (selecting nodes at random and syncing information) achieves both efficiency gain (only syncing with 1 node per period of time at maximum) and fast convergence as the probability that the information has not converged diminishes exponentially as time increases. 

## Strategies Introduced by the Paper 

### Direct Mail (Simple Broadcast)

The direct mail strategy is a simple broadcast model. As mentioned previously, this suffers from having to send N messages from the same server for every update.

Another problem is that the change is not propagated to all nodes in the following two scenarios:

1.) In a large system, it is reasonable to expect that not all nodes know about all other nodes -- some nodes have somewhat older information about the members of the network. If a node-A does not know about node-B, node-B will never get the update. 

2.) Since N is large, is it necessary to store the messages in a queue while the N messages are sent. If a crash occurs in that node before the queue is entirely sent, then some nodes will not get the message. If a target node is unreachable for the whole time it takes to empty the queue, the nodes that were unreachable will not get the message. You end-up in a system when a portion of nodes got the update, and a portion did not. You need to find a way to resolve those differences.

### Anti-Entropy (Simple Epidemic)

Each server runs the following algorithm:

- At every time interval t, pick a _random_ server and __resolve differences__ with that server (sync information).

This is extremely simple and elegant. 

**Number of messages / synchronizations**: At every time period t, every node is only (in a statistical sense) syncing with 2 nodes: 1 that it picked at random, and 1 incoming sync request since the N other nodes select the current node with probability 1/N.

**Time to reach all nodes**: At t0, the state change in a node. At t1, this node _at least_ syncs with 1 node, so 2 nodes have the change. At t2, those two nodes synchronize with at least 2 other nodes, bringing the total of nodes that know about the change to 4. And so it goes to 8, 16, 32, 64... The amount of time before all nodes about the change is log2(N) time periods.

**Failure tolerance**: The information propagates exponentially in the system. If 16 nodes know about a change, and those nodes will randomly get selected for syncing, the only way the information does not get propagated is that if somehow those 16 nodes fail at the same time. So it is possible that the information does not propagate if the initial, or 2 initial, or 4 initial nodes fail at the same time, which is unlikely.

**Topology**: It does not require a specific topology. In addition, if you add or remove nodes dynamically in the system, it does not matter. It is eventually consistent.

However, the cost of resolving difference between two nodes is much higher than sending a message with the single message/value that changed. This can be mitigated by using smart checksumming (e.g: merkle tree) and only sending the differing information over the network.

Anther optimization is to keep a list of recently changed values. It is possible to know the expected amount of time t' before an update is expected to have reached all nodes. All node keep a buffer of the values that changed in the last t' time, and upon resolving differences exchange those values first and do a full sync only if the state is different at the two nodes.

#### Which Random Distribution to Use

A normal distribution works, but using heuristics improves performance, For example, factoring-in which are the closest server to a node for syncing helps reduce propagation delay.

#### How to Deal with Deletion

Introduce the concept of a "dead key/value". Pass this information around as if it is a normal update. You can calculate the amount of time where you know the deletion has propagated with a confidence value of X sigmas (let's say at time t-del), then when timestamp of a dead key/value - t-now > t-del, wipe the key/value from the node.

#### How to Know Which Values to Keep if Receive Two Conflicting Values?

You have to introduce timestamps, and those timestamps have to be globally conherent. You always keep the value associated with the greatest timestamp.

### Complex Epidemics

@@resume.p.8 -- not done reading --

The principle behid complex epidemics methods is the same as with anti-entrophy, but with a few tweaks that enhance performance at the cost of certainty. The basic idea is that if a node is _pretty sure_ that other nodes have a change, it can stop trying to spread that change. Of course, this makes it possible that an update does not reach all nodes. In real system, then anti-anthropy is used in conjuction with complex epidemics (at a slower, low-cost pace) to guarantee the complete spread of information while benefiting from the saving of using more complex heuristics.

The first change to make is to keep track of the data to 'spread' instead of synchronizing the whole database between nodes. In key-value terms, every node keeps a list of keys that it things should be spread further. The second change is to incorporate _feedback_ in the spread of information. When a node synchronize with another nodes, it keeps increments a key's counter every time the other node already knew about the information. After this counter reaches _k_, the node considers that the change has spread and removes that key from the "key to spread" list.








