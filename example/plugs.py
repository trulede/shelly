# Copyright 2022 by Ila Rule.

from shelly import PlugS

plug = PlugS(ip='192.168.0.211')

plug.auto_off(60*60)
plug.schedule([
    '0730-0123456-on', '0930-0123456-off',
    '1130-0123456-on', '1330-0123456-off',
    '1530-0123456-on', '1730-0123456-off',
    '1930-0123456-on', '2130-0123456-off',
])
plug.led_disable(power=False, status=True)
