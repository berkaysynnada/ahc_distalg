import os
import sys
import logging
import networkx as nx
import matplotlib.pyplot as plt

# Ensure the Waves and TreeWaves modules can be imported from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Waves.TreeWaves import TreeComponentModel
from adhoccomputing.Generics import Event, EventTypes, GenericMessage, GenericMessageHeader
from adhoccomputing.Experimentation.Topology import Topology
from adhoccomputing.Networking.LogicalChannels.GenericChannel import GenericChannel

def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def create_network_topology(num_nodes):
    """ Creates a star network topology for simplicity, where one central node is connected to all others. """
    G = nx.star_graph(num_nodes - 1)
    nx.draw(G, with_labels=True, node_color='lightgreen')
    plt.show()
    return G

def initialize_nodes(graph, topology):
    """ Initializes TreeComponentModel nodes based on the graph topology. """
    nodes = {}
    for node_id in graph.nodes():
        node = TreeComponentModel("TreeNode", node_id, topology=topology)
        nodes[node_id] = node
        topology.add_node(node)
    return nodes

def connect_nodes(nodes, graph):
    """ Connects nodes based on the graph edges using GenericChannel. """
    for edge in graph.edges():
        node1, node2 = edge
        channel = GenericChannel("Channel_{}_{}".format(node1, node2), node1, node2)
        nodes[node1].add_neighbor(node2)
        nodes[node2].add_neighbor(node1)
        topology.add_channel(channel)

def simulate_algorithm(nodes):
    """ Triggers the tree formation from the central node in a star topology. """
    central_node = nodes[0]  # Assuming the central node is node 0 in a star topology
    decision_message = GenericMessage(GenericMessageHeader(WavesMessageTypes.GENERIC_MESSAGE, None, None), "Start Tree Formation")
    central_event = Event(central_node, EventTypes.MESSAGEFROMPEER, decision_message)
    central_node.on_message_from_peer(central_event)

def main():
    setup_logging()
    logging.info("Starting the Tree Algorithm Test")

    num_nodes = 6  # Example: 1 central node + 5 surrounding nodes
    topology = Topology()

    graph = create_network_topology(num_nodes)
    nodes = initialize_nodes(graph, topology)
    connect_nodes(nodes, graph)

    logging.info("Initiating Tree Algorithm from the central node")
    simulate_algorithm(nodes)

    logging.info("Tree Algorithm simulation complete")

if __name__ == "__main__":
    main()
