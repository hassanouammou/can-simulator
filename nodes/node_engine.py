from PyQt5.QtCore import QTimer
from engine.can_frame import CANFrame

class NodeEngine:
    def __init__(self, bus, gui):
        self.bus = bus
        self.gui = gui
        self.name = "Engine"
        self.rpm = 800

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)

    def tick(self):
        self.rpm += 50
        frame = CANFrame(0x200, [self.rpm // 256, self.rpm % 256])
        self.bus.send_frame(frame, self.name)

    def receive(self, frame, source_name=None):
        self.gui.add_message(self.name, frame)
