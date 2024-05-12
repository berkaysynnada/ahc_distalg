from .Waves import WavesComponentModel, WavesMessageTypes
from adhoccomputing.Generics import Event, EventTypes

class TarryComponentModel(WavesComponentModel):
    """
    Implementation of Tarry's Algorithm as a traversal algorithm for undirected networks.
    This algorithm ensures each channel is traversed twice, once in each direction,
    ultimately concluding at the initiator.
    """
    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, topology=None):
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, topology)
        self.visited = False
        self.parent = None
        self.token_sent_channels = set()

    def on_message_from_peer(self, event: Event):
        """
        Handles messages received from peer components according to Tarry's rules.
        Processes messages to control the traversal of the token.
        """
        message = event.eventcontent
        sender = event.fromchannel

        if message.header.messagetype == WavesMessageTypes.GENERIC_MESSAGE:
            if not self.visited:
                self.visited = True
                self.parent = sender
                self.pass_token_to_neighbors(sender)
            elif self.all_neighbors_visited() and sender == self.parent:
                self.finalize_algorithm()

    def pass_token_to_neighbors(self, exclude_channel):
        """
        Passes the token to all unvisited neighbors except the parent, unless there's no other option.
        """
        unvisited_neighbors = [n for n in self.neighbors if n not in self.token_sent_channels]
        if not unvisited_neighbors and self.parent is not None:
            unvisited_neighbors = [self.parent]
        
        for neighbor in unvisited_neighbors:
            if neighbor != exclude_channel or (neighbor == self.parent and len(unvisited_neighbors) == 1):
                self.send_generic_message(neighbor, WavesMessageTypes.GENERIC_MESSAGE, "Token")
                self.token_sent_channels.add(neighbor)

    def all_neighbors_visited(self):
        """
        Check if all neighbors have been visited.
        """
        return all(neighbor in self.token_sent_channels for neighbor in self.neighbors)

    def finalize_algorithm(self):
        """
        Finalizes the algorithm upon completion. 
        Notifies when the token returns to the initiator after traversing all channels.
        """
        if self.componentinstancenumber == 0:  # Assuming component 0 is the initiator
            print(f"Algorithm completed at the initiator {self.componentinstancenumber}.")
        else:
            self.send_generic_message(self.parent, WavesMessageTypes.GENERIC_MESSAGE, "Returning Token")

    def initiate_token(self):
        """
        Initiates the token passing process if this node is the initiator.
        """
        if self.visited == False:
            self.visited = True
            self.pass_token_to_neighbors(None)

    def handle_acknowledgement(self, event):
        """
        Handles acknowledgements from nodes confirming token receipt.
        """
        print(f"Acknowledgement received from {event.fromchannel}: {event.eventcontent}")

    def process_incoming_messages(self):
        """
        Processes incoming messages and determines action based on message type.
        """
        while self.message_queue:
            event = self.message_queue.pop(0)
            if event.eventcontent.header.messagetype == WavesMessageTypes.GENERIC_MESSAGE:
                self.on_message_from_peer(event)
            elif event.eventcontent.header.messagetype == WavesMessageTypes.ACKNOWLEDGEMENT:
                self.handle_acknowledgement(event)
