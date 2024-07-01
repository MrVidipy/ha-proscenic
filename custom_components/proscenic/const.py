"""Constants for the proscenic integration."""
from homeassistant.components.vacuum import (
    DOMAIN as VACUUM_DOMAIN,
    STATES as VACUUM_STATES
)

DOMAIN = "proscenic"
DEFAULT_NAME = "Proscenic Vacuum cleaner"
DATA_KEY = f"{VACUUM_DOMAIN}.{DOMAIN}"

CONF_LOCAL_KEY = "local_key"
CONF_REMEMBER_FAN_SPEED = "remember_fan_speed"

ATTR_MOP_EQUIPPED = "mop_equipped"
ATTR_CLEANING_TIME = "cleaning_time"
ATTR_ERROR = "error"

# in seconds
REMEMBER_FAN_SPEED_DELAY = 6

STATE_MOPPING = "mopping"

STATES = VACUUM_STATES.append(STATE_MOPPING)
