from ConnectingPage import ConnectingPage

class ConnectingHostPage(ConnectingPage):
    def __init__(self, parent, controller):
        self._config(parent, controller)

    def _connected(self):
        print("x")