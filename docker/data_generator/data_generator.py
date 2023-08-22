import csv
import random
import time
import os

def generate_data(filename, rows=100):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(rows):
            writer.writerow({'timestamp': time.time(), 'value': random.randint(0, 100)})

if __name__ == "__main__":
    mount_path = os.getenv('MOUNT_PATH', '/mount_s3')

    while True:
        timestamp = int(time.time())
        file_name = f"data_{timestamp}.csv"
        file_path = os.path.join(mount_path, file_name)

        generate_data(file_path)
        print(f"Data generated in {file_path}...")
        time.sleep(5) # Generates new data file every 5 seconds
