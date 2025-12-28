
# main.py
from netmiko import ConnectHandler
from devices import devices

def configure_trunking(device_list):
    for device in device_list:
        try:
            print(f"\n>>> Connecting to {device['host']}...")
            
            # Extract trunk ports before send to ConnectHandler
            ports = device.pop("trunk_ports") 
            
            net_connect = ConnectHandler(**device)
            net_connect.enable()
            
            config_commands = []
            for port in ports:
                print(f"    Configuring {port} as Trunk...")
                config_commands.extend([
                    f"interface {port}",
                    "switchport trunk encapsulation dot1q",
                    "switchport mode trunk",
                    "no shutdown",
                    "exit"
                ])
            
            output = net_connect.send_config_set(config_commands)
            print(output)
            
            # Save configuration
            net_connect.send_command("write memory")
            net_connect.disconnect()
            print(f"Done with {device['host']}.")

        except Exception as e:
            print(f"Error connecting to {device['host']}: {e}")


# "start" button kalau code ni run kat specific file
if __name__ == "__main__":
    configure_trunking(devices)
