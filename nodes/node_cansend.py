from engine.can_frame import CANFrame

class NodeCanSend:
    def __init__(self, bus, gui):
        self.bus = bus
        self.gui = gui
        self.name = "CanSend"

    def send(self, frame_id, data):
        frame = CANFrame(frame_id, data)
        self.bus.send_frame(frame, self.name)
        self.gui.add_message(self.name, frame)

    def receive(self, frame, source_name=None):
        pass
