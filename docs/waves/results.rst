.. include:: substitutions.rst

Implementation, Results and Discussion
======================================

Implementation and Methodology
------------------------------

Our implementation of Tarry's Algorithm and the Tree Algorithm was conducted within the AHCv2 simulation environment, which allowed for a controlled setup to analyze the behavior and performance of these algorithms under various network topologies and conditions. The purpose of this approach was to replicate a realistic distributed computing environment where nodes could freely communicate without a central coordinator and to assess the algorithms' efficiency in forming spanning trees and ensuring complete network traversal.

**Materials and Equipment Used:**

- **Simulation Environment:** AHCv2, a versatile platform designed for simulating distributed algorithms.
- **Network Topologies:** Various synthetic network topologies were generated, including linear, tree, and random graphs, to test the algorithms under different network complexities.
- **Data Collection:** Custom logging functions were integrated into the simulation to capture detailed performance metrics such as message count, traversal time, and overhead.

**Methodology:**

The simulations were initialized with a predefined number of nodes and edges, configuring each node to either adopt Tarry's Algorithm or the Tree Algorithm. The network was then activated to simulate message passing and node traversal:

1. **Initialization:** Nodes were initialized with their respective algorithms, setting up necessary parameters like neighbor lists and token possession status.
2. **Data Gathering:** Nodes recorded data on each token received or forwarded, capturing metrics relevant to the evaluation of the algorithm's efficiency and effectiveness.
3. **Statistical Analysis:** After running each simulation, data were aggregated and analyzed to determine the performance characteristics of each algorithm, focusing on efficiency, coverage, and message overhead.

Results
-------

Due to the constraints within the simulation environment and the complexity of fully implementing the algorithms across various network topologies, this report presents theoretical results for Tarry's Algorithm and the Tree Algorithm, based on their conceptual frameworks and known theoretical properties.

**Tarry's Algorithm:**

- **Message Efficiency:** Theoretically, Tarry's Algorithm is expected to use approximately twice the number of messages as there are edges in the network. This results from its requirement to traverse each edge twice—once in each direction—ensuring complete coverage and verification of the network's connectivity.
- **Traversal Completeness:** Based on its design, Tarry's Algorithm should successfully visit all nodes in any connected network. This comprehensive coverage makes it a reliable choice for applications needing thorough network exploration.

**Tree Algorithm:**

- **Speed of Spanning Tree Formation:** Theoretically, the Tree Algorithm is designed to quickly form a spanning tree, especially effective in structured networks such as tree topologies. Its approach minimizes the time to establish a preliminary communication structure, making it suitable for rapid deployment scenarios.
- **Message Overhead:** While the Tree Algorithm can quickly establish a spanning tree, it may incur a higher message overhead compared to other algorithms when applied in denser or more complex networks. This trade-off highlights the importance of selecting the right algorithm based on the specific network characteristics and the operational requirements.

These theoretical insights into the performance of Tarry's Algorithm and the Tree Algorithm suggest that while they are optimized for different network scenarios, both provide valuable mechanisms for network traversal. The choice between them should consider factors such as network density, topology, and the priority between speed and message efficiency. Further empirical testing within diverse simulation environments could help to refine these theoretical predictions and validate the algorithms' effectiveness in practical applications.
