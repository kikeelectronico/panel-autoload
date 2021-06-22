# panel-autoload

Panel autoload loads a web page on a Chromecast device automatically when the Chromecast enter in Ambient Mode.

# Parameters

*NAME:* The name of the target Chromecast.

*TRIGGER_APP:* The name of the app that trigger the autoload. Backdrop is the Ambient Mode default app.

*WEB_PANEL:* The URL to the web page that must be loaded.

*TEST:* Never Gonna Give You Up music video.

*LOOP:* Run indefinitely


# How to install and run on Debian and similar OS

1. Install the dependencies
```
sudo pip3 install -r requirements.txt
```
2. Change the working directory in *panel-autolaod.service*.

3. Move the service to the system directory
```
sudo cp panel-autoload.service /lib/systemd/system
```
4. Reload the daemon
```
sudo systemctl daemon-reload
```
5. Enable the service
```
 sudo systemctl enable panel-autoload.service
```
6. Start the service
```
 sudo systemctl start panel-autoload.service
```


# Run manually

```
python3 main.py
```