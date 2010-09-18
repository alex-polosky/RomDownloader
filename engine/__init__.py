from engine import *

for x in DownloadLink.abbrs.items():
    exec('''\
def getlink%s(self, link):
    link = link.split('/')[-2]
    link = 'http://romhustler.net/download/%s/' + link
    return link''' %(x[1], x[0])) in vars(DownloadLink)
