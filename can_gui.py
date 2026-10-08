from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QListWidget,
    QLineEdit, QPushButton, QLabel
)
from PyQt5.QtCore import QTimer
import time
import queue

class CanGUI(QMainWindow):
    def __init__(self, cansend_node):
        super().__init__()
        self.cansend_node = cansend_node
        self.msg_queue = queue.Queue()
        self.frame_count = 0
        self.last_time = time.time()

        self.setWindowTitle("CAN Simulator - Advanced GUI")

        central = QWidget()
        self.setCentralWidget(central)
        main = QVBoxLayout()
        central.setLayout(main)

        top = QHBoxLayout()
        main.addLayout(top)

        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels(
            ["Time", "ID", "Data", "DLC", "ACK", "Error", "Source"]
        )
        top.addWidget(self.table)

        self.nodes = QListWidget()
        self.nodes.addItems(["ABS", "Engine", "Dashboard", "Door", "CanDump", "CanSend"])
        top.addWidget(self.nodes)

        bottom = QHBoxLayout()
        main.addLayout(bottom)

        self.entry = QLineEdit()
        self.entry.setPlaceholderText("cansend 0x123 [1,2,3]")
        bottom.addWidget(self.entry)

        self.send_btn = QPushButton("Send")
        bottom.addWidget(self.send_btn)

        self.status = QLabel("Frames/sec: 0")
        main.addWidget(self.status)

        self.send_btn.clicked.connect(self.handle_cmd)
        self.entry.returnPressed.connect(self.handle_cmd)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_view)
        self.timer.start(50)

    def add_message(self, source, frame, extra_text=None):
        self.msg_queue.put((source, frame, extra_text))

    def update_view(self):
        while not self.msg_queue.empty():
            source, frame, extra_text = self.msg_queue.get()
            self.frame_count += 1

            row = self.table.rowCount()
            self.table.insertRow(row)

            t = time.strftime("%H:%M:%S")
            self.table.setItem(row, 0, QTableWidgetItem(t))
            self.table.setItem(row, 1, QTableWidgetItem(hex(frame.id)))
            self.table.setItem(row, 2, QTableWidgetItem(extra_text or str(frame.data)))
            self.table.setItem(row, 3, QTableWidgetItem(str(frame.dlc)))
            self.table.setItem(row, 4, QTableWidgetItem("ACK" if frame.ack else "NO ACK"))
            self.table.setItem(row, 5, QTableWidgetItem(str(frame.error)))
            self.table.setItem(row, 6, QTableWidgetItem(source))

            self.table.scrollToBottom()

        now = time.time()
        dt = now - self.last_time
        if dt >= 1:
            fps = self.frame_count / dt
            self.status.setText(f"Frames/sec: {fps:.1f}")
            self.frame_count = 0
            self.last_time = now

    def handle_cmd(self):
        cmd = self.entry.text()
        self.entry.clear()

        if cmd.startswith("cansend"):
            try:
                parts = cmd.split()
                frame_id = int(parts[1], 16)
                data = [int(x) for x in parts[2].strip("[]").split(",")]
                self.cansend_node.send(frame_id, data)
            except:
                pass
