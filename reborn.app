#!/bin/bash
#
# Dumb script to handle the next annoying bugs in MacOS:
# - User can't move to desktops via gestures.
# - Scrolling stop working when using Logi Options software (MX Master mouses)
#
# Changed to app extension to allow running it from the dock.

echo Killing Logi...
pkill -9 Logi
echo Killing Dock...
pkill -9 Dock
echo Done
