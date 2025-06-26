import time
from subprocess import run

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

DOCS_DIR = "docs"


class DocsChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        if event.event_type in ("created", "modified", "deleted", "moved"):
            print(f"Detected change in: {event.src_path} — Reindexing...")
            run(["python", "-m", "src.ingest.index"], check=False)


def start_watch():
    observer = Observer()
    handler = DocsChangeHandler()
    observer.schedule(handler, path=DOCS_DIR, recursive=False)
    observer.start()
    print(f"Watching '{DOCS_DIR}/' for changes. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    start_watch()
