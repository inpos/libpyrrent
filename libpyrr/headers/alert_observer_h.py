from ..utils import Struct
class alert_observer(Struct):
    def __init__(self):
        super(alert_observer, self).__init__()
        self.num_types = 0
        self.flags = 0
        self.types = []
        self.alert_handler = None
    def handle_alert(self, a):
        pass
