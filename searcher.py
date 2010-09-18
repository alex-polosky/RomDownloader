import urllib

from engine import DownloadLink

S = urllib.URLopener()

class Crawler():

    baseurl = 'http://romhustler.net/roms/'
    splittext = \
        [
            '''\
<p>Some titles on the list might not have a download link available. This is because these specific titles are <span class="important">ESA protected</span>. We <span class="important">cannot</span> offer any downloads for games that fall under ESA protection, thank you for understanding.</p>


<ul class="special">\
'''
        ]

    def splitter(self, link):
        #print(link)
        f = S.open(link)
        data = f.read()
        f.close()
        games = []
        try:
            data = data.split(self.splittext[0])[1].split(self.splittext[1])[0]
            data = data.split('\n')
        except:
            data = []
        try:
            for x in data:
                if x != '':
                    listing = x.split('<li><a href=')[1]
                    listing = listing.split('">')
                    listing[0] = 'http://romhustler.net' + listing[0].split('"')[1]
                    listing[1] = listing[1].split('</a></li>')[0]
                    games.append(listing)
        except IndexError:
            games = []
        return games

    def search(self, game, listings):
        games = []
        for x in listings:
            if game.lower() in x[1].lower():
                games.append(x)
        return games

    def partsplitter(self, games):
        urls = {'game name goes here': ['urls', 'go here']}
        for x in games:
            n = x[1].split(' part ')
            if n[0] not in urls:
                urls[n[0]] = [x[0]]
            elif n[0] in urls:
                urls[n[0]] += [x[0]]
        if urls['game name goes here'] == ['urls', 'go here']: del urls['game name goes here']
        games = []
        items = []
        for x in urls:
            items.append(x)
            items.sort()
        for x in items:
            l = []
            for y in urls[x]:
                l.append(y)
            games.append([l, x])
        return games

    def __init__(self, game, system, debug=0):
        self.abbrs = DownloadLink.abbrs
        self.abbrs2 = DownloadLink.abbrs2
        if system in self.abbrs.keys():
            #print((self.baseurl+system.lower()+'/'+game[0].lower()))
            listings = self.splitter(self.baseurl+system.lower()+'/'+game[0].lower())
        elif system in self.abbrs2.keys():
            #print((self.baseurl+self.abbrs2[system].lower()+'/'+game[0].lower()))
            listings = self.splitter(self.baseurl+self.abbrs2[system].lower()+'/'+game[0].lower())
        if debug == 0:
            games = self.search(game, listings)
            self.multi = 0
            if system in ['3do', 'psx', 'segacd']:
                #games = self.partsplitter(games)
                self.multi = 1
            games = self.partsplitter(games)
            self.games = games

