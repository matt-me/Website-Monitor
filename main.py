from wx.adv import NotificationMessage
from scripts import scanChanges
import wx
from time import sleep


def main():
    while 1:
        changes = scanChanges.updatesitelist()
        if changes > 0:
            outputstr = ""
            for change in changes:
                outputstr += change[0:len(change) - 2] + " "
            note = NotificationMessage("Website monitor", "One or more websites have changed: " + outputstr)
            note.Show()
        sleep(60)
if __name__ == "__main__":
    main()

