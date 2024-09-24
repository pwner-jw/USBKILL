# USBKill

USBKill is a security tool designed to monitor USB devices and execute a series of predefined commands if there are any changes in connected USB devices (such as adding or removing devices). This can be useful for protecting against unauthorized access via USB devices, as well as performing automated tasks such as deleting logs, browsing history, and finally shutting down the system.

## Features
- Detects connected/removable USB devices.
- Executes predefined commands listed in a configuration file (`usbkill.conf`).
- Deletes system logs, browsing history, and cookies.
- Recursively deletes a specified folder.
- Shuts down the system as a last step after executing all commands.

## Prerequisites
- **Python 3.x** installed on your system.
- **psutil** library for detecting USB devices.

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/pwner-jw/USBKill.git
cd USBKill
```

### Step 2: Install Dependencies
Install the required Python libraries by running the following command:
```bash
pip install -r requirements.txt
```

### Step 3: Set up the `usbkill.conf` Configuration File
Modify the `usbkill.conf` file according to your needs. This file should include the commands you want to execute when a USB device is connected or removed.

Example content for **Windows**:
```batch
:: --- Delete Logs ---
wevtutil cl System
wevtutil cl Application
wevtutil cl Security
del /s /f /q C:\Windows\System32\winevt\Logs\*.*
del /s /f /q C:\Windows\Temp\*.*
del /s /f /q %TEMP%\*.*
del /s /f /q C:\Windows\Prefetch\*.*
del /s /f /q "C:\ProgramData\Microsoft\Windows Defender\Scans\History\*.log"

:: --- Clear Browsing Data ---
del /s /f /q "%LocalAppData%\Google\Chrome\User Data\Default\Cache\*.*"
del /s /f /q "%LocalAppData%\Google\Chrome\User Data\Default\History"
del /s /f /q "%LocalAppData%\Google\Chrome\User Data\Default\Cookies"

:: --- Delete Disposable Folder ---
rd /s /q "C:\path\to\disposable\folder"

:: --- Shutdown System ---
shutdown /s /f /t 0
```

### Step 4: Run the Script
Once everything is configured, you can run the script using:

```bash
python usbkill.py
```

The script will now monitor for any changes in USB devices and execute the commands from `usbkill.conf` when a USB change is detected.

## Configuration: `usbkill.conf`
The `usbkill.conf` file should contain commands to execute when a USB device is added or removed. Some of the possible actions include:

1. **Delete Logs**: Clear various system logs (e.g., `wevtutil` for Event Logs on Windows).
2. **Clear Browsing Data**: Remove browsing history, cookies, and cache for Chrome, Firefox, and Edge.
3. **Recursively Delete Folder**: Delete sensitive or disposable folders.
4. **Shutdown System**: Securely shut down the system once critical tasks are completed.

### Example Config (Windows)
```batch
wevtutil cl System
wevtutil cl Application
wevtutil cl Security
del /s /f /q C:\Windows\System32\winevt\Logs\*.*
del /s /f /q C:\Windows\Temp\*.*
del /s /f /q %TEMP%\*.*
rd /s /q "C:\path\to\disposable\folder"
shutdown /s /f /t 0
```

### Example Config (Linux)
```bash
rm -rf /var/log/*
rm -rf ~/.cache/*
rm -rf /path/to/disposable/folder
shutdown now
```

## How it Works
1. The script continuously monitors connected USB devices using the `psutil` library.
2. When a change (addition/removal) is detected, it reads the commands from `usbkill.conf`.
3. Each command is executed sequentially, such as clearing logs, deleting folders, and shutting down the system.

## License
This project is licensed under the MIT License.
