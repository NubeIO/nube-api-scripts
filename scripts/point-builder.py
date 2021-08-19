from rubix import rubix_session
from config.load_config import get_config_host

host = get_config_host().get("host")
port = get_config_host().get("port")
user = get_config_host().get("user")
password = get_config_host().get("password")
url = f"http://{host}:{port}"

print(f"{host}:{port}")

"""
CONNECTION
"""
cx = rubix_session.RubixSession(
    host=url,
    user=user,
    password=password
)

device_start_address = 1

sensors = [
    "9EAB96B4",
    "8AAB95D2",
]

sensors_voc = [
    "1003-VOC",
    "1018-VOC",
    "B03-VOC",
    "G002-VOC",
]

point_names = ['temp', 'humidity']

device_count = len(sensors)
for i in range(device_count):
    for ii, r in enumerate(point_names):
        name = f"{sensors[i]}_{r}".replace('-', '_')
        point_obj = {
            "object_type": "analogOutput",
            "object_name": name,
            "use_next_available_address": True,
            "relinquish_default": 1,
            "priority_array_write": {
                "_1": None,
                "_2": None,
                "_3": None,
                "_4": None,
                "_5": None,
                "_6": None,
                "_7": None,
                "_8": None,
                "_9": None,
                "_10": None,
                "_11": None,
                "_12": None,
                "_13": None,
                "_14": None,
                "_15": None,
                "_16": None
            },
            "event_state": "lowLimit",
            "units": "noUnits",
            "description": "description",
            "enable": True,
            "fault": False,
            "data_round": 0,
            "data_offset": 0

        }
        url = f"http://{host}:{port}/api/bacnet/points"
        res = cx.connection.patch(url, json=point_obj)
        print(res.status_code)


