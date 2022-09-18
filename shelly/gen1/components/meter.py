
from ... import Device


class Meter:
    def __init__(self, device: Device, id: int) -> None:
        self._device = device
        self._id = id

    @property
    def id(self) -> int:
        return self._id

    def reload(self) -> None:
        if 'meter' not in self._device.api_state:
            self._device.api_state['meter'] = {}
        self._device.api_state['meter'][f'{self.id}'] = self._device.api_get(f'meter/{self.id}')
