import threading

from process_monitor import monitor_processes
from file_monitor import monitor_files


WATCH_FOLDER = "watched_folder"


if __name__ == "__main__":

    process_thread = threading.Thread(
        target=monitor_processes,
        daemon=True
    )

    file_thread = threading.Thread(
        target=monitor_files,
        args=(WATCH_FOLDER,),
        daemon=True
    )

    process_thread.start()
    file_thread.start()

    print("\nMini Endpoint Protection Monitor Running...\n")

    process_thread.join()
    file_thread.join()