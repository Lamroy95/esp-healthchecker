## Device description
The device is named Healthchecker. The front panel has two sections: **control panel** and **service status panel**.  

Control panel consists of:
- Power switch
- Internet connection indicator
- Alarm switch
- Alarm volume control
- Night mode switch (3 positions)

Service status panel consists of:
- 7-segment display with current time
- Six rows with switch, green light, red light and LCD.

Each row in service panel represents a service state. Service name as well as status are displayed on LCD.  
Green light is on when service is healthy, red light when service is dead. Sound alarm also goes off when service dies.
Here are some LCD text examples:
```
[Red light off, green light on]
Google. google.com
Healthy. 154ms

[Red light on, green light off]
Some API. exampleapi.com
Dead
```

## User should be able to:  
_Device control panel_  
- Turn the device on/off. Power leds should be green/red when device is on/off.
- See internet access state. Internet leds should be green/red when device is/isn't connected to the internet.
- Turn the sound alarm on/off with push-release button. Alarm leds should be green/red when alarm is on/off.
- Adjust sound alarm volume with volume control thingy :D
- Turn the "Night mode" on/off/auto. Night mode leds should be green/red when the night mode is on/off.

_Service status panel_  
- Turn each service "row" on/off. When service is on/off, corresponding green light indicator and LCD backlight should be enabled/disabled. When service row is disabled, underlying healthcheck might be still going, but alarm won't go off and red light won't turn on if service is not healthy.
- 2

*Night mode - LCDs' backlight, service status green indicators are turned off. Auto night mode enables/disables "lights" according to the luminance sensor.
Red status indicators are always enabled when service is unreachable.