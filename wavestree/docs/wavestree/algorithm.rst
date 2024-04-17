.. include:: substitutions.rst

|wavestree|
=========================================



Background and Related Work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Waves Tree Algorithm is an innovative approach in the realm of distributed computing, designed to efficiently manage and coordinate tasks across a network. This algorithm is particularly effective for constructing spanning trees, essential for operations like broadcasting messages and aggregating network-wide information. By enabling such tasks, the Waves Tree Algorithm plays a crucial role in enhancing the network's connectivity, data dissemination efficiency, and overall system robustness.

|wavestree| 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Waves Tree Algorithm is pivotal in distributed systems, facilitating crucial tasks such as constructing spanning trees for efficient message broadcasting and information aggregation. This algorithm employs a wave-based mechanism, where messages, or "waves," propagate from one or more source nodes throughout the network, ensuring comprehensive coverage and dynamic spanning tree construction without centralized control.

**Waves Tree Algorithm:**

The algorithm leverages the distributed nature of the network, where each node acts independently based on local information, to propagate waves and construct a spanning tree effectively.

1. **Wave Initiation:**  One or more nodes initiate the wave propagation by sending messages to their immediate neighbors, marking the beginning of the spanning tree construction.

2. **Wave Propagation:** Upon receiving a wave message, a node:

- Acknowledges its parent in the spanning tree (the node from which it received the first wave).
- Forwards the wave to its unvisited neighbors, expanding the tree.
- Avoids creating loops by not sending wave messages back to the sender or any node already incorporated into the spanning tree.

3. **Spanning Tree Completion:** The propagation continues until all nodes have been reached and incorporated into the spanning tree, ensuring that the tree covers the entire network.

**Implementation Details:**

Each node in the network maintains a record of its connections and their visited status. When a node receives the token, it:

1. Marks itself as visited.
2. Records the sender as its parent in the spanning tree.
3. Broadcasts the wave message to its unvisited neighbors, excluding the parent.


**Example**

Imagine a network where Node A initiates the wave. It sends wave messages to its neighbors, Node B and Node C. As they receive the wave, B and C mark A as their parent and propagate the wave further. This process repeats across the network, resulting in a spanning tree rooted at Node A, with branches extending to all other nodes.


**Algorithmic Properties:**
    
*Scalability*: The algorithm scales effectively with the network size, as each node only needs to communicate with its immediate neighbors.

*Efficiency*: By avoiding redundant messages and loops, the algorithm ensures efficient network traversal and spanning tree construction.

*Robustness*: The distributed nature of the algorithm enhances the network's fault tolerance, as the spanning tree can adapt to changes in the network topology.


**Correctness:**

*Termination (Liveness)*: The Waves Tree Algorithm guarantees termination due to its design ensuring each node propagates the wave message exactly once. Initially, one or more nodes start the wave propagation by sending messages to their immediate neighbors. As each node receives a wave message, it marks itself as visited and forwards the wave only to unvisited neighbors. This mechanism ensures that no node sends the wave message more than once, thus, every node eventually stops sending messages. The network's connectivity guarantees that all nodes will receive the wave message, ensuring the spanning tree is completed and the algorithm terminates.

*Safety*: Safety in the Waves Tree Algorithm is maintained by preventing the formation of loops and ensuring that no node is included more than once in the spanning tree. This is achieved through:

- Unique Parent Selection: Each node that receives a wave message for the first time acknowledges only the first sender as its parent in the spanning tree, which prevents multiple paths to the same node in the tree and avoids cycle formation.
- Visited Marking: Each node marks itself as visited once it processes the first received wave message and does not accept any further wave messages for propagation. This mechanism ensures that no node acts on outdated or redundant information, which could lead to loops or multiple entries for a node in the tree.

*Correctness*: To ensure the correctness of the Waves Tree Algorithm, we need to verify that the resulting spanning tree includes all nodes and contains no cycles. Each node in the network receives a wave message from exactly one parent, which it acknowledges as its entry into the spanning tree. This parent-child relationship prevents cycles since each node records only one incoming link from the tree and does not resend the wave back to the sender. Furthermore, because the messages are sent to every unvisited neighbor and each node becomes visited only once, every node in the network is eventually reached and included in the spanning tree. This structure confirms that the algorithm constructs a feasible and complete spanning tree as intended.


**Complexity**:

- Time Complexity: The time complexity is O(D), where D is the network diameter, representing the longest distance between any two nodes in the network. This accounts for the maximum number of steps required for wave propagation from the source to the most distant node.

- Message Complexity: The message complexity is O(N + E), similar to the number of edges, as each edge is used at most twice (once in each direction) for wave propagation.

- Space Complexity: The space requirement at each node is minimal, only needing to store the parent node's identifier and a visited flag, resulting in O(1) space complexity per node.


**Limitations:**

The Waves Tree Algorithm, while effective for spanning tree construction and message broadcasting, might encounter challenges in highly dynamic networks where frequent topology changes can necessitate continuous tree reconstructions. Additionally, in very large networks, the time to construct a spanning tree might be affected by the network's diameter.

Exploring the Waves Tree Algorithm offers insights into efficient distributed network management, emphasizing the importance of scalable, robust solutions for global coordination in distributed systems.