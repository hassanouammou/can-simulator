from PyQt5.QtCore import QTimer
from engine.can_frame import CANFrame

class NodeDoor:
    def __init__(self, bus, gui):
        self.bus = bus
        self.gui = gui
        self.name = "Door"
        self.open = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(5000)

    def tick(self):
        self.open = not self.open
        frame = CANFrame(0x350, [1 if self.open else 0])
        self.bus.send_frame(frame, self.name)

    def receive(self, frame, source_name=None):
        self.gui.add_message(self.name, frame)
