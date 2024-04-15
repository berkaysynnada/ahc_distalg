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

*Termination*: The algorithm guarantees that wave propagation will terminate, as each node propagates the wave only once, and loops are prevented, ensuring finite steps for wave propagation across the network.

*Spanning Tree Construction*: The algorithm ensures the construction of a valid spanning tree, as each node identifies a single parent, preventing cycles, and every node is reached, ensuring connectivity.


**Complexity**:

- Time Complexity: The time complexity is O(D), where D is the network diameter, representing the longest distance between any two nodes in the network. This accounts for the maximum number of steps required for wave propagation from the source to the most distant node.

- Message Complexity: The message complexity is O(N + E), similar to the number of edges, as each edge is used at most twice (once in each direction) for wave propagation.

- Space Complexity: The space requirement at each node is minimal, only needing to store the parent node's identifier and a visited flag, resulting in O(1) space complexity per node.


**Limitations:**

The Waves Tree Algorithm, while effective for spanning tree construction and message broadcasting, might encounter challenges in highly dynamic networks where frequent topology changes can necessitate continuous tree reconstructions. Additionally, in very large networks, the time to construct a spanning tree might be affected by the network's diameter.

Exploring the Waves Tree Algorithm offers insights into efficient distributed network management, emphasizing the importance of scalable, robust solutions for global coordination in distributed systems.