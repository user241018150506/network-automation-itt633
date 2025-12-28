
# devices.py

devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.11", # ESW1
        "username": "admin",
        "password": "password",
        "secret": "cisco",
        "trunk_ports": ["FastEthernet0/0", "FastEthernet0/1"]
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.12", # ESW2
        "username": "admin",
        "password": "password",
        "secret": "cisco",
        "trunk_ports": ["FastEthernet0/0"]
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.13", # ESW3
        "username": "admin",
        "password": "password",
        "secret": "cisco",
        "trunk_ports": ["FastEthernet0/1"]
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.14", # ESW4
        "username": "admin",
        "password": "password",
        "secret": "cisco",
        "trunk_ports": ["FastEthernet0/0"]
    }
]
