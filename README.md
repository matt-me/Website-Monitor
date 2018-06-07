This program is a set of scripts that scans a list of websites for changes in the background. It keeps those changes in the directory the program is run in a file called "list.txt"

Installation
=============
The following is required to run this program:
- Windows 10/8/7 (For the main desktop notifier)
- Python 2.7
- wxPython 4.0.1

wxPython
---------
You can install wxPython using pip
    pip install wxPython
Usage
=======
Command line scripts
---------------------
"addWebsite.py" - allows you to add a website to the list of monitored websites
"scanChanges.py - this checks each website for changes and prints whether they have changed or not
Run the two scripts as so

    ./addWebsite.py

    ./scanChanges.py

Windows Desktop Notifier
-------------------------
"main.py" - Run this to continutally check the websites on the list for updates every minute. If one changes, a notification will popup in the notification manager of windows alerting of the changed site.

    ./main.py
