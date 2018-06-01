import urllib
import hashlib
def openSite(str_url):
        return urllib.urlopen(str_url)

def main():
        print "Enter a website to monitor for updates: "
        site = raw_input()
        text = openSite(site)
        writeToFile(text, site)

def writeToFile(text, site):
        m = hashlib.md5()
        for line in text:
                m.update(line)
        fileName = "list.txt"
        file = open(fileName, "a+")
        lines = file.readlines()
        for i in range(0, len(lines)):
                if lines[i][0:len(lines[i]) - 1] == site + "\n":
                        print "That website is already being monitored."
                        if lines[i + 1] != m.hexdigest():
                                print "But it has changed the last time we read it!"
                                return
        file.write(site + "\n")
        file.write(m.hexdigest() + "\n")
        file.close()
if __name__ == "__main__":
        main()
