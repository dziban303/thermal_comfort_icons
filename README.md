# Home Assistant Thermal Comfort Icons
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

Official icon pack designed for [Thermal Comfort](https://github.com/dolezsa/thermal_comfort).

## Temperatures

### Heat Index
![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/thermometer-fire.svg) `heat-index`

### Dew Point
![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/thermometer-water.svg) `dew-point`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/thermometer-water-opacity.svg) `dew-point-alternative`

### Frost Point
![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/thermometer-snowflake.svg) `frost-point`

### Simmer Index
![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/thermometer-power-sleep.svg) `simmer-index`

## Perception

### Thermal Perception
![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/hand-thermometer.svg) `thermal-perception-hand`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/hand-thermometer-sun.svg) `thermal-perception-hand-alternative`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/hand-thermometer-water.svg) `dew-point-perception-hand`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/hand-thermometer-fire.svg) `heat-point-perception-hand`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/human-male-thermometer.svg) `thermal-perception`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/human-male-thermometer-sun.svg) `thermal-perception-alternative`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/human-male-thermometer-water.svg) `dew-point-perception`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/human-male-thermometer-fire.svg) `heat-point-perception`

### Simmer Zone
![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/hand-thermometer-power-sleep.svg) `simmer-zone`

![Preview](https://raw.githubusercontent.com/dziban303/thermal_comfort_icons/master/svg/human-male-thermometer-power-sleep.svg) `simmer-zone-human`

## Install

### Using HACS (recommended)
This icon pack can be installed using HACS. After installation, add the JavaScript resource to your Lovelace configuration:

```yaml
resources:
  - type: module
    url: /hacsfiles/dziban303/thermal_comfort_icons/thermal_comfort_icons.js
```

If you use `configuration.yaml`, use the new module URL in the `frontend` section:

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/dziban303/thermal_comfort_icons/thermal_comfort_icons.js
```

### Manual
Copy the `thermal_comfort_icons.js` file into `<config>/www/` where `<config>` is your Home Assistant config directory (the directory where your `configuration.yaml` resides).

Add the following to the `frontend` section of your `configuration.yaml`:

```yaml
frontend:
  extra_module_url:
    - /local/thermal_comfort_icons.js
```

Or add the following to your Lovelace raw configuration editor, or `ui-lovelace.yaml` in YAML mode:

```yaml
resources:
  - type: module
    url: /local/thermal_comfort_icons.js
```

Restart Home Assistant.

## Using

### Directly

Icons can be found with home assistants icon picker.

The icons use the prefix `tc:`.

### With Thermal Comfort

see https://github.com/dolezsa/thermal_comfort#custom-icons

## FAQ
Q: The icon ain't showing, it's just white space where it should be. What's up with that?

A: Probably related to cache. Try opening your instance in a incognito/private Window and see if your icon shows then. If yes, it's cache related. If not, spellcheck.

## Thanks
Based on [hass-bha-icons](https://github.com/hulkhaugen/hass-bha-icons) from @hulkhaugen
