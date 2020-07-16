from ConnectingPage import ConnectingPage

class ConnectingClientPage(ConnectingPage):
    
    def __init__(self, parent, controller):
        self.controller = controller
        self._config(parent, controller)

    @classmethod
    def _connected(cls):        
        pass
