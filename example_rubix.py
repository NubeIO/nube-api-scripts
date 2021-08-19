from rubix import rubix_session, discover, rubix_network, rubix_point, rubix_schedule
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

"""
Discover Connections to edge devices (Rubix-API)
"""
d = discover.Discover(connection=cx)
print(d.discover_all())
global_uuid = "XRRzciQUbpR4WMV9bPEESP"

"""
NETWORKS
"""

