from .abstract import Basic


class Database(Basic):
    tid_description = "tar-port"

    def read(self, alert):
        if alert.target_ip4:
            self._read(alert.target_ip4, alert.detect_time, alert.category_with_target_ports)
