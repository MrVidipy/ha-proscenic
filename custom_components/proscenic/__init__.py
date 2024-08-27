import .const import *
from .vacuum_proscenic import ProscenicVacuum

async def async_setup_entry(hass, entry):
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = dict(entry.data)

    config = dict(entry.data)
    conf_sleep = entry.options.get(CONF_SLEEP, DEFAULT_CONF_SLEEP)

    auth = {
        CONF_DEVICE_ID: config[CONF_DEVICE_ID],
        CONF_TOKEN: config[CONF_TOKEN],
        CONF_USER_ID: config[CONF_USER_ID],
        CONF_AUTH_CODE: config[CONF_AUTH_CODE],
        CONF_TARGET_ID: get_or_default(config, CONF_TARGET_ID, config[CONF_DEVICE_ID])
    }

    ip = get_or_default(config, CONF_HOST, None)
    mode = get_or_default(config, CONF_CONNECTION_MODE, LOCAL_MODE)
    device = ProscenicVacuum(auth, ip, mode, loop = hass.loop, config = {CONF_SLEEP: conf_sleep})

    hass.data[DOMAIN][entry.entry_id]['device'] = device

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, 'vacuum')
    )
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, 'camera')
    )
    return True
