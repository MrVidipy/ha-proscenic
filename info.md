[![License][license-shield]](LICENSE.md)

# Proscenic Home Assistant component

## This is a fork based on [edenhaus work](https://github.com/edenhaus/ha-prosenic/tree/master)

A full featured Homeassistant component to control Proscenic vacuum cleaner locally without the cloud.
This component is based on the underlying tinytuya library available [here](https://github.com/jasonacox/tinytuya).

## Towards Homeassistant official integration

My personal goal is to make this component fully compliant with Homeassistant, so
that it may be added as the official library to handle Proscenic vacuum cleaners.
However, before pushing a PullRequest to the official Homeassistant repository, I would like to share it to some users.
In this way we can test it massively, check it for any bug and make it **robust enough** to be seamlessly integrated
with Homeassistant.

## Installation

You can install this component manually.

1.  Clone the git master branch
2.  Unzip/copy the proscenic direcotry within the `custom_components` directory of your homeassistant installation.
    The `custom_components` directory resides within your homeassistant configuration directory.
    In other words, the configuration directory of homeassistant is where the configuration.yaml file is located.
    After a correct installation, your configuration directory should look like the following.
    `└── ... └── configuration.yaml └── secrects.yaml └── custom_components └── proscenic └── __init__.py └── const.py └── ...`

        **Note**: if the custom_components directory does not exist, you need to create it.

## Component setup

Once the component has been installed, you need to configure it in order to make it work.

First we need to find out the _device_id_, _ip address_ and _local key_ of your proscenic vacuum cleaner.

Todo that you need to follow the Tuya Device Preparation Section of tinytuya :

https://github.com/jasonacox/tinytuya?tab=readme-ov-file#tuya-device-preparation


### Configuration via editing configuration.yaml

1. Enable the component by editing the configuration.yaml file (within the config directory as well).
   Edit it by adding the following lines:

   ```yaml 
      vacuum: 
      - platform: "prosenic"
        host: "YOUR_HOST_IP"
        device_id: "YOUR_DEVICE_ID"
        local_key: "YOUR_LOCAL_KEY"
        remember_fan_speed: false #Optional, default false 
   ```
   **Note!** If you have already configured other vacuum robot, add your configuration there.

1. Reboot hassio (check for any errors in the logs)
1. Congrats! You're all set! It should appear in Entities

## Additional Information

Currently this integration is only tested with a Proscenic 850T, because I only have this one.
Please give me feedback, if it works with other models too.

The integration is communicating locally only, so you can block the access of your vacuum robot to the internet.

If you find a problem/bug or you have a feature request, please open an issue.

## What's next?

- Better error handling
- Automated test
