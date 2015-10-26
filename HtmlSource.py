import urllib
file = open("newfile.txt", "w")

sock = urllib.urlopen("http://www.marketwatch.com/story/10-most-popular-youtube-videos-of-2014-2014-12-09")
htmlSource = sock.read()
file.write(htmlSource)
file.close()

sock.close()
print htmlSource
