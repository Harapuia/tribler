import threading

global thumbnail_sem
thumbnail_sem = threading.BoundedSemaphore()
global app_ending
app_ending = False
global nfcCallback
nfcCallback = None
global skelly
skelly = None
global videopref
videopref = "INTERNAL"
global triblerfun
triblerfun = False
