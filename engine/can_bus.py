class CANBus:
    def __init__(self):
        self.nodes = []

    def connect_node(self, node):
        self.nodes.append(node)

    def send_frame(self, frame, source_name=None):
        frame.ack = True
        frame.error = None

        for node in self.nodes:
            node.receive(frame, source_name)
