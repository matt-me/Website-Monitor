import urllib
import hashlib
def opensite(str_url):
    return urllib.urlopen(str_url)


def main():
    print "Enter a website to monitor for updates: "
    site = raw_input()
    text = opensite(site)
    addsite(text, site, "../")


def addsite(text, site, path):
    m = hashlib.md5()
    for line in text:
        m.update(line)
        filename = "data/list.txt"
        myfile = open(path + filename, "a+")
        lines = myfile.readlines()
        for i in range(0, len(lines)):  # type: int
            if lines[i][0:len(lines[i]) - 1] == site + "\n":
                print "That website is already being monitored."
                if lines[i + 1] != m.hexdigest():
                    print "But it has changed the last time we read it!"
                    return
    myfile.write(site + "\n")
    myfile.write(m.hexdigest() + "\n")
    myfile.close()


if __name__ == "__main__":
    main()
