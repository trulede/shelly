
from ... import Device


class Actions:
    def __init__(self, device: Device) -> None:
        self._device = device

    def reload(self) -> None:
        if 'settings' not in self._device.api_state:
            self._device.api_state['settings'] = {}
        if 'actions' not in self._device.api_state['settings']:
            self._device.api_state['settings']['actions'] = {}
        self._device.api_state['settings']['actions'] = self._device.api_get('settings/actions')
