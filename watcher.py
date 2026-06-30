from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import DOWNLOADS_FOLDER
from organizer import organize

class DownloadHandler(FileSystemEventHandler):
  def on_created(self, event):
    if event.is_directory:
      return
    
    print(f"New file detected: {event.src_path}")
    
    organize()

observer = Observer()
observer.schedule(
  DownloadHandler(),
  str(DOWNLOADS_FOLDER),
  recursive=False
)

observer.start()

print(f"Watching for new files in {DOWNLOADS_FOLDER}...")

try:
  while True:
    pass
except KeyboardInterrupt:
  observer.stop()

observer.join()