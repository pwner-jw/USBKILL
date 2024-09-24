import psutil
import subprocess
import time
import os

def detect_usb_devices():
    """Detects connected removable USB devices."""
    usb_devices = []
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        if 'removable' in partition.opts:  # Detect removable devices
            usb_devices.append(partition.device)

    return usb_devices

def execute_usbkill_commands(config_file):
    """Executes the commands from the specified configuration file."""
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            commands = f.read().splitlines()  # Read commands line by line
            for command in commands:
                if command.strip():  # Ignore empty lines
                    try:
                        print(f"Executing: {command}")
                        subprocess.run(command, shell=True, check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Command failed: {command}. Error: {e}")
    else:
        print(f"Configuration file {config_file} not found!")

if __name__ == "__main__":
    prev_usb_devices = set()
    config_file = "usbkill.conf"  # Path to your configuration file

    while True:
        connected_usb_devices = set(detect_usb_devices())

        if connected_usb_devices != prev_usb_devices:
            print(f"USB device change detected. Current devices: {connected_usb_devices}")
            
            # Execute commands from the config file on USB change
            execute_usbkill_commands(config_file)
            
            # Update previous device state
            prev_usb_devices = connected_usb_devices

        time.sleep(2)  # Polling interval of 2 seconds
