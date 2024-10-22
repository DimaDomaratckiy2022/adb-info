import subprocess
import os
import sys

def adb_command(command):
    adb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'adb')

    result = subprocess.run([adb_path] + command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result.stdout.strip()

def get_device_info():
    device_info = {}
    adb_devices = adb_command(['devices'])
    if not adb_devices:
        print("No connected devices found.")
        return

    system_info = adb_command(['shell', 'getprop'])
    if system_info:
        for line in system_info.splitlines():
            key_value = line.split(": ", 1)
            if len(key_value) == 2:
                device_info[key_value[0].strip()] = key_value[1].strip()

    with open('device_info.txt', 'w', encoding='utf-8') as file:
        for key, value in device_info.items():
            file.write(f"{key}: {value}\n")

    print("Device information saved to device_info.txt")

if __name__ == "__main__":
    get_device_info()
