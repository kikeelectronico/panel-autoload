import pychromecast
import os
import time

NAME = "Chromecast Salón"
TRIGGER_APP = "Backdrop"
WEB_PANEL = "http://192.168.10.2:81"
TEST = False

# Get the actual app
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[NAME], retry_wait=0, discovery_timeout=2)
if len(chromecasts) > 0:
  cast = chromecasts[0]
  cast.wait()

  # It is the trigger app?
  if cast.status.display_name == TRIGGER_APP:
    os.system("catt -d \"" + NAME + "\" set_default")
    if TEST:
      os.system("catt cast \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"")
    else:
      os.system("catt cast_site \"" + WEB_PANEL + "\"")
pychromecast.discovery.stop_discovery(browser)
