"""Shelly Plug S

Simplified control of a Shelly Plug S via the HTTP API.


Example
-------

    from shelly import PlugS

    plug = PlugS(ip='192.168.33.1')
    plug.on()
    plug.off()
    plug.auto_off(60*5)
    plug.schedule(['0730-0123456-on', '0830-0123456-off'])
    plug.led_disable(power=False, status=True)


Notes
-----

Shelly documentation:

    * [Userguide Shelly Plug S Application](https://shelly.cloud/documents/user_guide/shelly_plug_s_app.pdf)
    * [Userguide Shelly Plug S](https://shelly.cloud/documents/user_guide/shelly_plug_s_multi_language.pdf)
    * [API Documentation](https://shelly-api-docs.shelly.cloud/gen1/#shelly-plug-plugs-overview)


How to reset:

    1.  Press and hold the button for 10 seconds. The light will fast flach blue (indicating AP mode).
    2.  Connect with browser to address 192.168.33.1
    3.  Assign an IP address & gateway, then connect to target WiFi network.


Schedule items are a string with format HHMM-MTWTFSS-on|off (MTWTFSS are days of week, e.g. "0123456").

"""

from typing import Dict, List
from .gen1 import Gen1Device
from .gen1.components import Actions, Meter, Relay


class PlugS(Gen1Device):
    def __init__(self, **kwds) -> None:
        super().__init__(**kwds)
        self._meter = [ Meter(self, x) for x in range(0,1) ]
        self._relay = [ Relay(self, x) for x in range(0,1) ]
        self._actions = Actions(self)
        self.reload()

    def reload(self) -> None:
        super().reload()
        for m in self._meter:
            m.reload()
        for r in self._relay:
            r.reload()
        self._actions.reload()

    @property
    def status(self) -> Dict[str, str]:
        return {}

    def off(self) -> None:
        self._relay[0].off()

    def on(self) -> None:
        self._relay[0].on()

    def auto_off(self, seconds: int) -> None:
        self._relay[0].auto_off(seconds)

    def schedule(self, value: List[str]) -> None:
        self._relay[0].schedule(value)

    def led_disable(self, power: bool, status: bool) -> None:
        self.api_post('settings', {'led_power_disable': power, 'led_status_disable': status})
        super().reload()
