class NodeDashboard:
    def __init__(self, bus, gui):
        self.bus = bus
        self.gui = gui
        self.name = "Dashboard"

    def receive(self, frame, source_name=None):
        if frame.id == 0x100:
            msg = f"ABS: vitesse={frame.data[0]}, slip={frame.data[1]}"
        elif frame.id == 0x200:
            rpm = frame.data[0] * 256 + frame.data[1]
            msg = f"RPM moteur: {rpm}"
        elif frame.id == 0x350:
            msg = "Porte ouverte" if frame.data[0] == 1 else "Porte fermée"
        else:
            msg = str(frame.data)

        self.gui.add_message(self.name, frame, extra_text=msg)
