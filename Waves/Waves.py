from adhoccomputing.GenericModel import GenericModel, GenericMessageHeader, GenericMessage
from adhoccomputing.Generics import Event, EventTypes
from enum import Enum

class WavesMessageTypes(Enum):
    GENERIC_MESSAGE = "GENERIC_MESSAGE"
    TOKEN = "TOKEN"
    ACKNOWLEDGEMENT = "ACKNOWLEDGEMENT"

class WavesComponentModel(GenericModel):
    """
    A common component model for distributed algorithms that can be extended by specific algorithm implementations.
    This class provides basic functionality for managing neighbors and sending messages.
    """
    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, topology=None):
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, 1, topology)
        self.neighbors = set()
        self.message_queue = []  # Queue to store incoming messages if needed

    def add_neighbor(self, neighbor):
        """
        Add a neighbor to this node's set of direct connections.
        """
        self.neighbors.add(neighbor)

    def send_generic_message(self, to_channel, message_type, content=""):
        """
        Send a generic message to a specified neighbor.
        """
        msg = GenericMessage(GenericMessageHeader(message_type, None, None), content)
        self.send_down(Event(self, EventTypes.MESSAGEFROMABOVE, msg), to_channel)

    def receive_message(self, event):
        """
        Handle incoming messages from neighbors. Should be overridden by subclasses for specific behaviors.
        """
        print(f"Received message from {event.fromchannel}: {event.eventcontent}")
        # Default behavior could be to echo the message back or to log it
        self.message_queue.append(event)

    def process_messages(self):
        """
        Process messages from the queue, simulating message handling in a distributed system.
        """
        while self.message_queue:
            message = self.message_queue.pop(0)
            # Example processing logic: echo the message back to sender
            self.send_generic_message(message.fromchannel, WavesMessageTypes.ACKNOWLEDGEMENT, "Received your message")

    def initiate_token_passing(self):
        """
        Example method to demonstrate initiating a token-passing or wave algorithm in the network.
        """
        if self.neighbors:
            # Send a token to the first neighbor (simple example)
            first_neighbor = next(iter(self.neighbors))
            self.send_generic_message(first_neighbor, WavesMessageTypes.TOKEN, "Starting token pass")

    def handle_token(self, event):
        """
        Handle a token received from a neighbor, decide what to do with it based on the algorithm.
        """
        print(f"Token received from {event.fromchannel}")
        # Decide to pass the token to the next neighbor, if any
        for neighbor in self.neighbors:
            if neighbor != event.fromchannel:  # Don't send back to the sender
                self.send_generic_message(neighbor, WavesMessageTypes.TOKEN, "Passing token")
                break

    def finalize_algorithm(self):
        """
        Any cleanup or final actions after the distributed algorithm completes.
        """
        print("Finalizing algorithm operations.")
