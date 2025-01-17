# WinBackup

WinBackup is a simple Python program that automatically creates backup copies of important files and folders on Windows. It is designed to run continuously, creating backups every 24 hours.

## Features

- Automatically backs up specified directories.
- Logs backup operations for easy monitoring.
- Handles errors gracefully, providing informative logs for troubleshooting.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Ensure Python 3.x is installed on your Windows machine.
2. Clone the repository or download the `winbackup.py` file.

## Usage

1. Open `winbackup.py` in a text editor.
2. Modify the `source_directories` variable to include the paths of directories you want to back up.
3. Modify the `backup_directory` variable to specify where you want the backups to be stored.
4. Open a command prompt and navigate to the directory containing `winbackup.py`.
5. Run the program with the following command:

   ```
   python winbackup.py
   ```

The program will run indefinitely, creating backups every 24 hours. You can stop it by closing the command prompt or pressing `Ctrl+C`.

## Logging

All backup operations are logged in `backup.log` in the same directory as the script. Check this file for information about backup successes and failures.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.