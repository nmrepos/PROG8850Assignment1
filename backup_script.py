import os
import datetime
import subprocess

# Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "testdb"


# Unique filename with timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"{DB_NAME}_backup_{timestamp}.sql"

# Command to dump database
backup_command = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_filename}"

# Execute backup
try:
    subprocess.run(backup_command, shell=True, check=True)
    print(f"Backup successful: {backup_filename}")
except subprocess.CalledProcessError as e:
    print(f"Backup failed: {e}")
