# Shelly

Shelly device automation via HTTP API, without Shelly Cloud or Smartphone App.


## Devices

### Shelly Plugs

```python
from shelly import PlugS

plug = PlugS(ip='192.168.33.1')
plug.on()
plug.off()
```
