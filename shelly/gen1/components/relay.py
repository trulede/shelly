
from ... import Device


class Relay:
    def __init__(self, device: Device, id: int) -> None:
        self._device = device
        self._id = id
        self._schedule_rules = []   # max 20 Schedule.

    @property
    def id(self) -> int:
        return self._id

    def reload(self) -> None:
        if 'relay' not in self._device.api_state:
            self._device.api_state['relay'] = {}
        self._device.api_state['relay'][f'{self.id}'] = self._device.api_get(f'relay/{self.id}')

        if 'settings' not in self._device.api_state:
            self._device.api_state['settings'] = {}
        if 'relay' not in self._device.api_state['settings']:
            self._device.api_state['settings']['relay'] = {}
        self._device.api_state['settings']['relay'][f'{self.id}'] = self._device.api_get(f'settings/relay/{self.id}')

    def on(self) -> None:
        self._device.api_post(f'relay/{self.id}', {'turn': 'on'})
        self.reload()

    def off(self) -> None:
        self._device.api_post(f'relay/{self.id}', {'turn': 'off'})
        self.reload()
