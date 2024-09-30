[app]

source.dir = .

# (str) Title of your application
title = NightSafe

# (str) Package name
package.name = nightsafe

# (str) Package domain (should be unique, reverse domain notation)
package.domain = org.eldinsmash

# (str) Source code file for main application
source.include_exts = py,png,jpg,kv,atlas

# (str) The main entry point file for the application
main.py

# (list) Application version
version = 1.0

# (list) Supported orientations
orientation = portrait

# (str) Full name of the author
author = Salim

# (str) Description of the app
description = NightSafe provides real-time tracking and safety features for night-time outings.

# (str) Your email
author.email = vaishnav@gmail.com

# (str) Icon of your application (512x512 px)
icon.filename = resources/icons/nightsafe_icon.png

# (list) Presplash of the app (optional, 480x800 px)
presplash.filename = resources/images/presplash.png

# (str) Supported platforms
# Change to android for building APK or ios for iOS builds
supported_platforms = android

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions required by the app
# Ensure these match the app's actual needs
android.permissions = INTERNET, ACCESS_FINE_LOCATION, SEND_SMS

# (bool) Android backup (true to allow app data backup)
android.allow_backup = True

# (int) Android min API level
android.minapi = 21

# (int) Android target API level
android.api = 33

# (list) Requirements for the app (list of libraries to include)
requirements = python3,kivy,kivy-garden.mapview,requests

# (str) Custom command to build the APK
# You can add build options or leave default
buildozer -v android debug

# (list) Screensize definitions
screen_dpi = 160,240,320,480,640

[buildozer]

# (str) Log level (info, warning, debug, error)
log_level = 2

# (bool) Enable verbose logging
verbose = True
