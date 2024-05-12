from .Waves import WavesComponentModel, WavesMessageTypes
from adhoccomputing.Generics import Event, EventTypes, GenericMessage, GenericMessageHeader

class TreeComponentModel(WavesComponentModel):
    """
    A Tree Algorithm model for undirected, acyclic networks that follows the wave algorithm.
    This model ensures exactly two processes decide and consider each other as their parent,
    establishing a tree structure across the network.
    """
    def __init__(self, componentname, componentinstancenumber, context=None, configurationparameters=None, topology=None):
        super().__init__(componentname, componentinstancenumber, context, configurationparameters, topology)
        self.received_from = set()  # Set of neighbors from which messages have been received
        self.decided = False  # Flag to check if the decision has been made
        self.parent = None

    def on_message_from_peer(self, event: Event):
        """
        Handles messages received from peer components by implementing the logic to wait for messages from all neighbors except one before making a decision.
        """
        message = event.eventcontent
        sender = event.fromchannel

        self.received_from.add(sender)
        if len(self.received_from) == len(self.neighbors) - 1 and not self.decided:
            self.make_decision()

    def make_decision(self):
        """
        Decides on the parent if all but one neighbor have sent their messages.
        """
        remaining_neighbor = (self.neighbors - self.received_from).pop()
        self.parent = remaining_neighbor
        self.send_decision_message(remaining_neighbor)

    def send_decision_message(self, to_channel):
        """
        Sends a decision message to the specified neighbor, finalizing the parent decision.
        """
        self.decided = True
        decision_msg = GenericMessage(GenericMessageHeader(WavesMessageTypes.GENERIC_MESSAGE, None, None), "Decision")
        self.send_down(Event(self, EventTypes.MESSAGEFROMABOVE, decision_msg), to_channel)
        print(f"Process {self.componentinstancenumber} decides with {to_channel} as parent.")

    def reset_decision(self):
        """
        Resets the decision-making process in case of a network change or for reinitialization.
        """
        self.decided = False
        self.received_from.clear()
        self.parent = None

    def propagate_decision(self):
        """
        Propagates the decision to all neighbors, ensuring that the tree structure is acknowledged.
        """
        for neighbor in self.neighbors:
            if neighbor != self.parent:
                self.send_generic_message(neighbor, WavesMessageTypes.DECISION_ACKNOWLEDGE)

    def handle_acknowledgement(self, event):
        """
        Processes acknowledgements from neighbors confirming their acceptance of the decision.
        """
        sender = event.fromchannel
        print(f"Acknowledgement received from {sender}: decision accepted.")

    def process_incoming_messages(self):
        """
        Processes incoming messages and determines actions based on message types.
        """
        while self.message_queue:
            event = self.message_queue.pop(0)
            if isinstance(event.eventcontent, GenericMessage):
                if event.eventcontent.header.messagetype == WavesMessageTypes.GENERIC_MESSAGE:
                    self.on_message_from_peer(event)
                elif event.eventcontent.header.messagetype == WavesMessageTypes.DECISION_ACKNOWLEDGE:
                    self.handle_acknowledgement(event)
