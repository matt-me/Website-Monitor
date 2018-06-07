import urllib
import hashlib

def main():
    updatesitelist("../")


def updatesitelist(args):
    myfile = open(args + "data/list.txt", "r")
    changedlist = []
    lines = myfile.readlines()
    for i in range(0, len(lines), 2):
        site = urllib.urlopen(lines[i])
        h = hashlib.md5()
        for line in site:
            h.update(line)
        if h.hexdigest().strip() != lines[i + 1].strip():
            lines[i + 1] = h.hexdigest() + "\n"
            changedlist.append(lines[i])
    myfile.close()
    myfile = open(args + "data/list.txt", "w+")
    for line in lines:
        myfile.write(line)
    myfile.close()
    if len(changedlist) > 0:
        print "The following items have changed:"
        print changedlist
        return changedlist
    print "No changes to report."
    return


if __name__ == "__main__":
    main()