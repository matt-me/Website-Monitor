from wx.adv import NotificationMessage
from scripts import scanChanges
from time import sleep
import wx


def main():
    app = wx.App()
    while 1:
        changes = scanChanges.updatesitelist("")
        if len(changes) > 0:
            outputstr = ""
            for change in changes:
                outputstr += change[0:len(change) - 1] + " "
            note = NotificationMessage("Website monitor", "One or more websites have changed: " + outputstr).Show()
        sleep(60)
if __name__ == "__main__":
    main()

