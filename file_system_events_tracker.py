import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "c:\Users\P M\Desktop\class 102\dir-project-102"

# Event Handler Class
class FileSystemEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! someone deleted {event.src_path}!")

# Initialize Event Handler Class
event_handler = FileSystemEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stopped!")
    observer.stop()