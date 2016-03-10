from ..utils import Enum

class Alert(object):
    category_t = Enum({
                          'error_notification':         0x1,
                          'peer_notification':          0x2,
                          'port_mapping_notification':  0x4,
                          'storage_notification':       0x8,
                          'tracker_notification':       0x10,
                          'debug_notification':         0x20,
                          'status_notification':        0x40,
                          'progress_notification':      0x80,
                          'ip_block_notification':      0x100,
                          'performance_warning':        0x200,
                          'dht_notification':           0x400,
                          'dht_notification':           0x400,
                          'session_log_notification':   0x2000,
                          'torrent_log_notification':   0x4000,
                          'peer_log_notification':      0x8000,
                          'incoming_request_notification':  0x10000,
                          'dht_log_notification':           0x20000,
                          'dht_operation_notification':     0x40000,
                          'port_mapping_log_notification':  0x80000,
                          'picker_log_notification':        0x100000,
                          'all_categories':                 0x7fffffff
                          })
    def timestamp(self):
        pass
    def type(self):
        pass
    def what(self):
        pass
    def message(self):
        pass
    def category(self):
        pass

alert = Alert()
