
from .. import Device


class Gen1Device(Device):
    def __init__(self, **kwds) -> None:
        super().__init__(**kwds)

    def reload(self) -> None:
        super().reload()
        self.api_state['status'] = self.api_get('status')
        self.api_state['settings'] = self.api_get('settings')
