.. include:: substitutions.rst

|traversaltarry|
=========================================



Background and Related Work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Tarry Algorithm is a classic method from graph theory adapted for distributed computing to ensure every connection in a network is visited once. It's a depth-first search approach where a token circulates through the network from node to node. Nodes pass the token to an unvisited neighbor or backtrack if none are available, ensuring all connections are covered without needing a central control or complete network knowledge. This simplicity and efficiency make the Tarry Algorithm well-suited for distributed systems.

|traversaltarry| 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tarry's Algorithm is a fundamental tool in distributed systems for network traversal, ensuring that each connection within the network is explored precisely once. This capability is crucial for tasks like network diagnostics, maintenance, and optimizing distributed protocols. The algorithm operates on the principle of a depth-first search, adapted to the decentralized nature of distributed systems, where nodes lack global knowledge of the network's structure.

**Tarry's Algorithm:**

Tarry's Algorithm orchestrates network traversal by employing a token-passing mechanism, where a token is circulated among nodes to guide the traversal process. This approach ensures that every node and its connections are visited without the need for central coordination or comprehensive network knowledge beforehand.

1. **Token Circulation:** Initiated by a designated node, the token is passed along the network's connections, adhering to a depth-first traversal pattern.

2. **Decision-Making at Nodes:** Upon receiving the token, a node determines its next action based on the state of its connections:

- If there exists an unvisited connection, the token is forwarded to the corresponding neighbor.
- If all connections are marked as visited, the token is returned along its incoming path, enabling the algorithm to backtrack and explore alternate routes.

3. **Traversal Completion:** The process continues until the token returns to the initiator node after having traversed all available paths, signaling the completion of the network traversal.

**Implementation Details:**

Each node in the network maintains a record of its connections and their visited status. When a node receives the token, it:

1. Marks the incoming connection as visited.
2. Chooses an unvisited neighbor to pass the token to, if available.
3. If no unvisited neighbors exist, sends the token back to the sender.


**Example**

Consider a network with nodes A, B, and C connected in a triangle. Starting from Node A, the token is passed to B, then to C, and back to A, marking each connection as visited. This example illustrates how Tarry's Algorithm ensures complete and efficient network traversal without revisiting nodes or connections unnecessarily.


**Algorithmic Properties:**
    
*Efficiency*: The algorithm efficiently traverses the network by ensuring each connection is visited once, minimizing redundant operations.

*Decentralization*: Each node operates based on local information, eliminating the need for a centralized controller or global network knowledge.

*Completeness*: The depth-first search approach guarantees that all nodes and connections are explored, ensuring thorough network coverage.


**Correctness:**

*Termination (Liveness)*: Tarry's Algorithm guarantees termination, meaning that the network traversal will complete within a finite amount of time. This is ensured by the algorithm's depth-first search approach, where each node forwards the token to an unvisited neighbor or backtracks when no such neighbors exist. Since the network is finite and each connection is visited only once, the token will eventually return to the initiator node, marking the end of the traversal.

*Feasibility*: The algorithm ensures that each node and connection is visited exactly once, adhering to the principles of a depth-first traversal. This is achieved through the marking of connections as "visited" upon token passage, preventing cycles and redundant visits. The depth-first nature also ensures that the traversal is feasible in distributed environments, where global knowledge of the network is not available.


**Complexity**:

- Time Complexity: The time complexity of Tarry's Algorithm depends on the network's size and topology. In the worst case, where the network forms a deep tree-like structure, the algorithm's time complexity is O(N + E), where N is the number of nodes and E is the number of edges. This accounts for visiting each node and traversing each edge exactly once. In denser networks, backtracking might increase traversal time, but the overall complexity remains bounded by the total number of edges.

- Message Complexity: The message complexity, or the total number of token transmissions, is also O(N + E) in the worst case. Each edge is traversed twice (once in each direction), and each node participates in the token passing at least once. The use of backtracking might increase the number of messages, but each message corresponds to an edge traversal, keeping the total number within the bound of 2E.

- Space Complexity: Each node needs to keep track of its visited connections, requiring storage proportional to its degree (the number of immediate neighbors). In total, the space complexity across the entire network is O(E), as each edge contributes to the degree of two nodes.


**Limitations:**

While Tarry's Algorithm is effective for network traversal, its efficiency can vary with network size and topology. The reliance on token passing introduces communication overhead, and the depth-first nature may lead to longer traversal times in dense networks.

By understanding and implementing Tarry's Algorithm, we gain valuable insights into distributed network traversal, contributing to the development of more robust and efficient distributed systems.