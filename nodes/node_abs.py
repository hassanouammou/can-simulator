from PyQt5.QtCore import QTimer
from engine.can_frame import CANFrame

class NodeABS:
    def __init__(self, bus, gui):
        self.bus = bus
        self.gui = gui
        self.name = "ABS"

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)  # 1 trame/sec

    def tick(self):
        frame = CANFrame(0x100, [10, 5])
        self.bus.send_frame(frame, self.name)

    def receive(self, frame, source_name=None):
        self.gui.add_message(self.name, frame)
