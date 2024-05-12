import os
import sys
import logging
import networkx as nx
import matplotlib.pyplot as plt

# Ensure the Waves and TarryWaves modules can be imported from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Waves.TarryWaves import TarryComponentModel
from adhoccomputing.Generics import Event, EventTypes, GenericMessage, GenericMessageHeader
from adhoccomputing.Experimentation.Topology import Topology
from adhoccomputing.Networking.LogicalChannels.GenericChannel import GenericChannel

def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def create_network_topology(num_nodes):
    """ Creates a circular network topology for simplicity. """
    G = nx.cycle_graph(num_nodes)
    nx.draw(G, with_labels=True, node_color='lightblue')
    plt.show()
    return G

def initialize_nodes(graph, topology):
    """ Initializes TarryComponentModel nodes based on the graph topology. """
    nodes = {}
    for node_id in graph.nodes():
        node = TarryComponentModel("TarryNode", node_id, topology=topology)
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

def simulate_algorithm(start_node):
    """ Simulates the start of Tarry's algorithm from the given start node. """
    initial_token = GenericMessage(GenericMessageHeader(WavesMessageTypes.GENERIC_MESSAGE, None, None), "Initial Token")
    start_event = Event(start_node, EventTypes.MESSAGEFROMPEER, initial_token)
    start_node.on_message_from_peer(start_event)

def main():
    setup_logging()
    logging.info("Starting the Tarry's Algorithm Test")

    num_nodes = 5  # Example: simple 5-node ring
    topology = Topology()

    graph = create_network_topology(num_nodes)
    nodes = initialize_nodes(graph, topology)
    connect_nodes(nodes, graph)

    # Start the simulation from a random node
    import random
    start_node_id = random.choice(list(nodes.keys()))
    logging.info(f"Starting Tarry's Algorithm from node {start_node_id}")
    simulate_algorithm(nodes[start_node_id])

    logging.info("Tarry's Algorithm simulation complete")

if __name__ == "__main__":
    main()
