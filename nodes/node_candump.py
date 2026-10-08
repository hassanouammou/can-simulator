class NodeCanDump:
    def __init__(self, bus, gui):
        self.bus = bus
        self.gui = gui
        self.name = "CanDump"

    def receive(self, frame, source_name=None):
        self.gui.add_message(self.name, frame)
