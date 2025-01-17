import os
import shutil
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='backup.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_current_time():
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def create_backup(source_dirs, backup_dir):
    """
    Create backup copies of important files and folders.
    
    :param source_dirs: List of directories to back up
    :param backup_dir: Directory where backups will be stored
    """
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    for source in source_dirs:
        if os.path.exists(source):
            try:
                dest = os.path.join(backup_dir, f"{os.path.basename(source)}_{get_current_time()}")
                shutil.copytree(source, dest)
                logging.info(f"Backup successful for {source} to {dest}")
            except Exception as e:
                logging.error(f"Failed to back up {source}. Error: {str(e)}")
        else:
            logging.warning(f"Source directory does not exist: {source}")

def main():
    # List of directories to back up
    source_directories = [
        r'C:\Users\YourUsername\Documents\ImportantFiles',
        r'C:\Users\YourUsername\Pictures\ImportantPhotos'
    ]
    
    # Directory where backups will be stored
    backup_directory = r'C:\Backup'

    # Schedule backup every 24 hours
    while True:
        create_backup(source_directories, backup_directory)
        logging.info("Waiting 24 hours until the next backup.")
        time.sleep(24 * 60 * 60)  # Sleep for 24 hours

if __name__ == '__main__':
    main()