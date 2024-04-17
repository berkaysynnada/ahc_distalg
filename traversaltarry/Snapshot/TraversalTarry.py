from random import choice
import uuid
from enum import Enum
from typing import List

# Import relevant modules
from ...Experimentation.Topology import Topology
from ...GenericModel import GenericModel, GenericMessageHeader, GenericMessagePayload, GenericMessage
from ...Generics import *

# Define custom message types using Enum for clarity and type safety
class WaveMessageTypes(Enum):
    FORWARD = "@tarrys/forward"
    START = "@tarrys/start"

# Define a specialized message header that includes a token
class WaveMessageHeader(GenericMessageHeader):
    def __init__(self, *args, token, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token

# Message payload structure remains simple as it just carries the payload
class WaveMessagePayload(GenericMessagePayload):
    pass

# Class to represent neighbors in Tarry's traversal algorithm
class TarryNeighbor:
    def __init__(self, id, invoked):
        self.id = id
        self.invoked = invoked

# Main class for Tarry's traversal logic in a distributed system component
class TarrysTraverse(GenericModel):
    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, num_worker_threads=1, topology=None):
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, num_worker_threads, topology)
        self.token_neighbor_mapping = {}
        self.token_parent_mapping = {}

    # Method to handle messages received from lower layers
    def on_message_from_bottom(self, eventobj: Event):
        msg = eventobj.eventcontent
        hdr = msg.header
        message_source = hdr.messagefrom
        payload = msg.payload.messagepayload

        # Process only FORWARD and START message types
        if hdr.messagetype in [WaveMessageTypes.FORWARD, WaveMessageTypes.START]:
            token = hdr.token
            if hdr.messagetype == WaveMessageTypes.START:
                self.token_parent_mapping[token] = -1

            parent_for_token = self.token_parent_mapping.get(token, None)
            if parent_for_token is None:
                self.token_parent_mapping[token] = message_source
                parent_for_token = message_source

            next_target = None

            uninvoked_neighbors = [n for n in self.get_neighbor_mapping_for_token(token) if not n.invoked and n.id != parent_for_token]
            if uninvoked_neighbors:
                neigh = choice(uninvoked_neighbors)
                neigh.invoked = True
                next_target = neigh.id
            else:
                if parent_for_token == -1:
                    logger.debug("->".join(payload))
                    logger.debug(f"TRAVERSING IS COMPLETED IN {str(len(payload))} hops")
                    logger.debug(f"Graph had {self.topology.G.number_of_edges()} edges")
                    return
                else:
                    next_target = parent_for_token

            payload.append(str(self.componentinstancenumber))
            message = self.prepare_message(WaveMessageTypes.FORWARD, next_target, token, payload)
            self.send_down(Event(self, EventTypes.MFRT, message))

    # Method to start the traversal process
    def start_traverse(self):
        token = self.create_token()
        self.send_self(Event(self, EventTypes.MFRB, self.prepare_message(WaveMessageTypes.START, self.componentinstancenumber, token, [])))

    # Helper method to generate a unique token
    def create_token(self):
        return str(uuid.uuid4())

    # Prepares the initial map of neighbors with their invoked status as False
    def prepare_neighbor_map(self):
        neighbor_list = self.topology.get_neighbors(self.componentinstancenumber)
        return [TarryNeighbor(n, False) for n in neighbor_list]

    # Retrieves or initializes the neighbor mapping for a given token
    def get_neighbor_mapping_for_token(self, token: str) -> List[TarryNeighbor]:
        mapping = self.token_neighbor_mapping.get(token)
        if mapping is None:
            mapping = self.prepare_neighbor_map()
            self.token_neighbor_mapping[token] = mapping
        return mapping

    # Prepares a message to be sent to a neighbor
    def prepare_message(self, message_type: WaveMessageTypes, neighbor: int, token: str, payload: str = None) -> GenericMessage:
        header = WaveMessageHeader(message_type, self.componentinstancenumber, neighbor, neighbor, token=token)
        payload = WaveMessagePayload(payload)
        return GenericMessage(header, payload)
