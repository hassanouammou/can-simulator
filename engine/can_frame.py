class CANFrame:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.dlc = len(data)
        self.ack = False
        self.error = None
