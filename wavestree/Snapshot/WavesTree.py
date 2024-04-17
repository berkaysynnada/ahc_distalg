#!/usr/bin/env python
import time
from itertools import chain

# Import relevant modules
from ...Experimentation.Topology import Topology
from ...GenericModel import GenericModel, GenericMessageHeader, GenericMessagePayload, GenericMessage
from ...Generics import *

class TreeNode(GenericModel):
    """
    TreeNode class that simulates a node in a tree-based distributed algorithm,
    managing the process of creating a spanning tree within a network topology.
    """

    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, num_worker_threads=1, topology=None):
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, num_worker_threads, topology)
        self.unvisitedNeighbours = []

    def on_init(self, eventobj: Event):
        """
        Initializes the TreeNode and logs its creation.
        """
        logger.debug(f"Initializing {self.componentname}.{self.componentinstancenumber}")

    def on_message_from_bottom(self, eventobj: Event):
        """
        Handles incoming messages from connected nodes and processes the message to further the spanning tree construction.
        """
        # Identify the channel that corresponds to the event source
        channel = next((ch for ch in self.unvisitedNeighbours if eventobj.eventsource in chain(*ch.connectors.values())), None)
        
        if channel:
            self.unvisitedNeighbours.remove(channel)
            
            # Decide next action based on the number of unvisited neighbors
            if len(self.unvisitedNeighbours) == 0:
                self.decide()
            elif len(self.unvisitedNeighbours) == 1:
                self.parent = self.unvisitedNeighbours[0]
                logger.debug(f"{self.componentname}.{self.componentinstancenumber} sends message to {self.parent.componentname}.{self.parent.componentinstancenumber}")
                self.parent.trigger_event(Event(self, EventTypes.MFRT, eventobj.eventcontent))

    def startTreeAlgorithm(self):
        """
        Initiates the tree construction algorithm by checking and managing the status of connected neighbors.
        """
        self.unvisitedNeighbours = self.connectors[ConnectorTypes.DOWN]
        if len(self.connectors[ConnectorTypes.DOWN]) == 1:
            self.parent = self.unvisitedNeighbours[0]
            logger.debug(f"{self.componentname}.{self.componentinstancenumber} sends message to {self.parent.componentname}.{self.parent.componentinstancenumber}")
            self.send_down(Event(self, EventTypes.MFRT, None))
            self.unvisitedNeighbours = []

    def decide(self):
        """
        Finalizes the decisions when no unvisited neighbors are left and logs the decision time.
        """
        logger.debug(f"{self.componentname}.{self.componentinstancenumber} decides.")
        logger.debug(f"End Time: {time.time()}")
