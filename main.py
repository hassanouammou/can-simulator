from PyQt5.QtWidgets import QApplication
import sys

from engine.can_bus import CANBus
from nodes.node_abs import NodeABS
from nodes.node_engine import NodeEngine
from nodes.node_dashboard import NodeDashboard
from nodes.node_door import NodeDoor
from nodes.node_candump import NodeCanDump
from nodes.node_cansend import NodeCanSend

from can_gui import CanGUI

app = QApplication(sys.argv)

bus = CANBus()

cansend = NodeCanSend(bus, None)
gui = CanGUI(cansend)
cansend.gui = gui

abs_node = NodeABS(bus, gui)
engine_node = NodeEngine(bus, gui)
dashboard_node = NodeDashboard(bus, gui)
door_node = NodeDoor(bus, gui)
candump_node = NodeCanDump(bus, gui)

bus.connect_node(abs_node)
bus.connect_node(engine_node)
bus.connect_node(dashboard_node)
bus.connect_node(door_node)
bus.connect_node(candump_node)
bus.connect_node(cansend)

gui.show()
sys.exit(app.exec_())
