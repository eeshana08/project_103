import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_modfifed(self, event):
        print(f"Hi, looks like {event.src_path} has been modifed!")

    def on_moved(self, event):
        print(f"Looks like {event.src_path} has been moved!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

event_handler = FileEventHandler()

observer = Observer()

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()