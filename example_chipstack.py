from config.load_config import get_config_host
from chirpstack import chirpstack, device

host = get_config_host().get("host")
port = get_config_host().get("port")
user = get_config_host().get("user")
password = get_config_host().get("password")
url = f"http://{host}:{port}"

print(f"{host}:{port}")

cs = chirpstack.Chirpstack(
    chirpstack_url=url,
    chirpstack_user="admin",
    chirpstack_pass="password"
)

cd = device.Devices(chirpstack_connection=cs)
devices = cd.get_device(dev_eui="a81758fffe056177")


"""
ADD A NEW DEVICE
"""
new = cd.create_and_activate()
new.description = "This is my device"
new.deveui = "c9014a013d89fa5c"
new.name = "My-device-32222"
new.profile_id = "08b4a5e4-552f-4a1e-aba6-dbda739a152e"
new.appid = 1
res = new.create_and_activate()
print(res)

