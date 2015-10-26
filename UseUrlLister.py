import urllib, UrlLister
file = open("newfile1.txt", "w")
usock = urllib.urlopen("https://www.youtube.com/playlist?list=PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-")
parser = UrlLister.URLLister()
parser.feed(usock.read())



usock.close()
parser.close()
for url in parser.urls: 
    print url
    file.write(url)
    file.write("\n\n")
