.. include:: substitutions.rst

|Tarry's Traversal Algorithm|
=========================================


Tarry's Algorithm is a classic traversal method used in undirected graphs to create a spanning tree and ensure that every node is visited exactly once. This algorithm is particularly significant for its efficiency in managing token circulation and its straightforward implementation in distributed systems without central coordination.

**Principles and Mechanism:**

Tarry's Algorithm is based on a simple token-passing mechanism that adheres to specific traversal rules to explore every part of an undirected network. The token travels through each channel twice, once in each direction, thus covering the entire network and ensuring the algorithm's completeness.

1. **Token Initiation:** The traversal begins at a designated initiator node, which starts with the token and sends it to one of its neighbors.
2. **Token Circulation:** Upon receiving the token, each node marks itself as visited. It then passes the token to an adjacent unvisited neighbor if available. If all neighbors have been visited, the token is returned to the neighbor from which it was received.
3. **Traversal Rules:** 
    - A node never forwards the token through the same channel twice in the same direction.
    - A node forwards the token back to its parent only if there are no other unvisited neighbors available.

**Implementation Steps:**

Below are the implementation steps for Tarry's Algorithm, which can be adapted to various distributed system architectures:

.. code-block:: RST
    :linenos:
    :caption: Tarry's Algorithm Pseudocode

    Algorithm TarrysAlgorithm
    Begin
        if node is initiator:
            send token to an arbitrary neighbor
        endif

        while token is received from neighbor:
            mark self as visited
            if there are unvisited neighbors:
                choose an unvisited neighbor and send the token
            else:
                return token to sender
            endif
        endwhile
    End

**Example Scenario:**

Consider a simple network with four nodes arranged in a square: A, B, C, and D. Node A starts with the token and sends it to Node B. Node B, upon receiving the token, marks itself as visited and passes it to Node C. Node C does the same and sends it to Node D. Finally, Node D, after visiting itself, finds no unvisited neighbors and sends the token back to Node C, which then returns it to Node B, and finally back to Node A, completing the traversal.

**Evaluation and Benefits:**

Tarry's Algorithm ensures that every node and channel is adequately explored, making it highly reliable for network diagnostics and maintenance tasks in distributed systems. The algorithm's rule to never traverse the same channel twice in the same direction minimizes the message overhead, making it efficient in terms of network resource utilization.

However, the requirement that each channel be traversed twice, once in each direction, can increase the time complexity in larger or denser networks. Despite this, Tarry's Algorithm remains a foundational approach for network traversal in undirected graphs due to its simplicity and effectiveness.


|Tree Algorithm|
=========================================

The Tree Algorithm is a decentralized wave algorithm designed for creating spanning trees in undirected and acyclic networks. This algorithm is notable for its simplicity and efficiency, ensuring that exactly two nodes in the network make a decision without centralized coordination.

**Principles and Mechanism:**

The Tree Algorithm operates based on the principle of waiting for messages from all neighbors except one before making a decision. This approach helps in effectively determining the structure of the spanning tree with minimal communication overhead.

1. **Initial Conditions:** Each node waits to receive messages from all its neighbors except one. This exception is the neighbor that will eventually become the node's parent in the spanning tree.
2. **Parent Selection:** Once a node has received messages from all but one of its neighbors, it selects the neighbor from which it has not received a message as its parent and sends a message to this neighbor.
3. **Decision Making:** Upon receiving a message from its parent, a node finalizes its decision. In each execution of the algorithm, exactly two nodes make a decision and consider each other as their parent, thus forming the roots of two disjoint trees.

**Implementation Steps:**

Below are the steps to implement the Tree Algorithm in a network of distributed nodes:

.. code-block:: RST
    :linenos:
    :caption: Tree Algorithm Pseudocode

    Algorithm TreeAlgorithm
    Begin
        foreach node in network:
            Listen for messages from all neighbors except one
            if messages received from all but one neighbor:
                Select the neighbor with no message as parent
                Send message to selected parent
            endif
            if message received from parent:
                Finalize decision
            endif
        endfor
    End

**Example Scenario:**

Imagine a network topology like a star, where a central node (A) is connected to several outer nodes (B, C, D). Node B receives messages from Nodes C and D but not from A. Node B then selects A as its parent and sends a message to A. Similarly, Nodes C and D select A after receiving messages from B and D, respectively, and each other. Node A, upon receiving messages from all its children, becomes the root of the tree.

**Evaluation and Benefits:**

The Tree Algorithm is particularly efficient for networks where the topology does not contain cycles, as it ensures that all channels are utilized only once. This minimizes the communication cost and speeds up the decision-making process. The algorithm guarantees that two nodes will always end up as decision makers, providing a clear termination condition and making it suitable for networks requiring robust and quick formation of spanning trees.

However, the Tree Algorithm is not suitable for networks containing cycles, as it can lead to deadlocks where nodes wait indefinitely for messages from their neighbors. Furthermore, its performance and correctness are highly dependent on the network being acyclic, limiting its applicability to specific types of network topologies.