from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

from logger import log_event


class FileMonitorHandler(FileSystemEventHandler):

    def on_created(self, event):

        if not event.is_directory:
            filename = os.path.basename(event.src_path)

            log_event(
                event_type="File Created",
                target_name=filename,
                risk="LOW"
            )


    def on_modified(self, event):

        if not event.is_directory:
            filename = os.path.basename(event.src_path)

            log_event(
                event_type="File Modified",
                target_name=filename,
                risk="LOW"
            )


    def on_deleted(self, event):

        if not event.is_directory:
            filename = os.path.basename(event.src_path)

            log_event(
                event_type="File Deleted",
                target_name=filename,
                risk="MEDIUM"
            )


    def on_moved(self, event):

        if not event.is_directory:
            filename = os.path.basename(event.dest_path)

            log_event(
                event_type="File Renamed / Moved",
                target_name=filename,
                risk="LOW"
            )


def monitor_files(folder_path):

    event_handler = FileMonitorHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        folder_path,
        recursive=False
    )

    observer.start()

    print(f"\nMonitoring Folder: {folder_path}\n")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()