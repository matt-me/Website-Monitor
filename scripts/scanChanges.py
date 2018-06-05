import time
import urllib
import hashlib
def updateSiteList():
    #every once in a while
    file = open("list.txt", "r")
    changed = []
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        site = urllib.urlopen(lines[i])
        h = hashlib.md5()
        for line in site:
            h.update(line)
        if h.hexdigest().strip() != lines[i + 1].strip():
            lines[i + 1] = h.hexdigest() + "\n"
            changed.append(lines[i])
    file.close()
    file = open("list.txt", "w+")
    if len(changed) > 0:
            print "Found changes in the following webpages:"
            for line in changed:
                    print line
    for line in lines:
        file.write(line)
