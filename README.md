# Shelly

Shelly device automation via HTTP API, without Shelly Cloud or Smartphone App.


## Devices

### Shelly Plugs

```python
from shelly import PlugS

plug = PlugS(ip='192.168.33.1')
plug.on()
plug.off()
# Auto Off (in seconds).
plug.auto_off(3600)
# Set a schedule (HHMM-MTWTFSS-on|off).
plug.schedule(['0730-0123456-on', '0830-0123456-off'])
```
