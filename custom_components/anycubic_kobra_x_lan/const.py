DOMAIN = "anycubic_kobra_x_lan"

CONF_HOST = "host"
CONF_PC_DEVICE_ID = "pc_device_id"
CONF_POLLING_INTERVAL = "polling_interval"

DEFAULT_NAME = "Anycubic Kobra X LAN"
DEFAULT_POLLING_INTERVAL = 30
MIN_POLLING_INTERVAL = 10
MAX_POLLING_INTERVAL = 3600

PLATFORMS = ["sensor", "binary_sensor", "button", "camera", "light", "number", "switch"]

# The printer serves its camera as HTTP-FLV on this port once it has been
# told to startCapture over MQTT.
CAMERA_STREAM_PORT = 18088
CAMERA_START_DEBOUNCE_SECONDS = 10
# Restart the stream after a reconnect if it was viewed this recently.
CAMERA_RESUME_WINDOW_SECONDS = 600

QUERY_TYPES = [
    "status",
    "info",
    "tempature",
    "fan",
    "light",
    "peripherie",
    "multiColorBox",
]
