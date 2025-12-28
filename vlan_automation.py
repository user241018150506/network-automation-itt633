from netmiko import ConnectHandler
from devices import devices

# VLANs we want to create
vlans = {
    10: "MANAGEMENT",
    20: "FINANCE",
    30: "HR",
    40: "SERVER"
}

for device in devices:
    print(f"\nConnecting to {device['host']}")

    net_connect = ConnectHandler(**device)
    net_connect.enable()

    config_commands = []

    for vlan_id, vlan_name in vlans.items():
        config_commands.append(f"vlan {vlan_id}")
        config_commands.append(f"name {vlan_name}")
        config_commands.append("exit")

    output = net_connect.send_config_set(config_commands)
    print(output)

    print("\nVLAN verification:")
    verify = net_connect.send_command("show vlan brief")
    print(verify)

    net_connect.disconnect()