# Different os's are:
# posix, nt, dos, os2, mac, ce
import os
from sys import stdout
import urllib

# An example array string
#a = "var link_enc=new Array('h','t','t','p',':','/','/','d','o','w','n','l','o','a','d','.','r','o','m','h','u','s','t','l','e','r','.','n','e','t','/','d','o','w','n','l','o','a','d','/','8','8','5','6','2','d','6','0','4','8','8','2','0','3','9','b','d','c','3','2','e','c','6','2','5','7','a','3','e','1','9','2','/','4','c','0','2','e','a','b','b','/','p','s','x','/','F','1','%','2','0','W','o','r','l','d','%','2','0','G','r','a','n','d','%','2','0','P','r','i','x','%','2','0','%','5','B','U','%','5','D','%','2','0','%','5','B','S','L','U','S','-','0','1','0','3','6','%','5','D','.','p','a','r','t','0','1','.','r','a','r');link = '';for(i=0;i<link_enc.length;i++){link+=link_enc[i];}"

class DownloadLink():

    abbrs = \
     {
         '3do':'3do',
         'atari2600':'Atari 2600',
         'atari5200':'Atari 5200',
         'atari7800':'Atari 7800',
         'jag':'Atari Jaguar',
         'lynx':'Atari Lynx',
         'col':'Coleco Colecovision',
         'cps1':'CPS1',
         'cps2':'CPS2',
         'fba':'Final Burn Alpha',
         'gba':'Gameboy Advance',
         'gbc':'Gameboy Color',
         'gg':'GameGear',
         'vectrex':'GCE Vectrex',
         'genesis':'Genesis',
         'mame':'MAME',
         'intellivision':'Mattel Intellivision',
         'mtx':'Memotech MTX512',
         'sam':'MGT Sam Coupe',
         'msx1':'MSX1',
         'msx2':'MSX2',
         'neogeo':'NeoGeo',
         'neogeocd':'NeoGeoCD',
         'ngp':'NeoGeo Pocket',
         'nes':'Nes',
         'n64':'Nintendo 64',
         'ds':'Nintendo DS',
         'pcengine':'PCEngine',
         '32x':'Sega 32X',
         'segacd':'Sega CD',
         'dreamcast':'Sega Dreamcast',
         'sms':'Sega Master System',
         'saturn':'Sega Saturn',
         'snes':'Snes',
         'psp':'Sony PSP',
         'psx':'Sony Playstation',
         'tg16':'Turbo Grafx16',
         'WonderSwan':'Wonder Swan',
         'Zinc':'Zinc',
     }

    abbrs2 = {}
    abbrsnames = {}
    for x in abbrs.items():
        abbrs2[x[1]] = x[0]
        abbrsnames[x[0]] = x[1]
        abbrs[x[0]] = x[1].replace(' ', '')
        
    def geturl(self, link):
        link = link.split('var link_enc=new Array(')[1]
        link = link.split(");link = '';for(i=0;i<link_enc.length;i++){link+=link_enc[i];}")[0]
        link = link.split(',')
        for x in range(0, len(link)):
            link[x] = link[x].split("'")[1]
        return ''.join(link)

    def download(self, source, dest=None, size=2048*2, src='cmd'):
        if (dest == None):
            dest = source.split('/')[-1].replace('%20', ' ').replace('%27', "'").replace('%5B', '[').replace('%5D', ']')
            for x in range(30, 100):
                dest = dest.replace('%'+hex(x).replace('0x', ''), chr(x))
        f = urllib.URLopener().open(source)
        total = int(f.info().dict['content-length'])
        if (src == 'cmd'):
            if os.path.isfile(dest):
                print('\nDestination file already exists\nChange name?')
                while True:
                    try:
                        ans = raw_input("Y or N?> ")
                        if ans.lower() not in ['yes', 'y', 'no', 'n']:
                            raise BaseException
                        break
                    except BaseException:
                        print("Not a valid choice")
                    except:
                        print("Invalid choice")
                if ans in ['yes', 'y']:
                    while True:
                        try:
                            dest = raw_input("=> ")
                            break
                        except:
                            print("Invalid")
                elif ans in ['no', 'n']:
                    pass
                print("")
        f2 = open(dest, 'wb')
        if (src == 'cmd'):
            print '%0.2f MB' %(total / 1048576.0)
            #print "[=========================] 99%"
            print "[                         ] 00%"
            per = 0
            count = 0
            chunk = None
            #print count, total, per
            while True:
                chunk = f.read(size)
                count += 1
                if (
                    ((25.0 * count)/total) * 100 != per
                    ):
                    per = ((25.0 * count)/total) * 100
                    stdout.write(('\b'*32)+(' '*32)+('\b'*32))
                    stdout.write('['+('='*int(25 * (per/100.0)))+(' '*int(25 * ((100-per)/100.0)))+'] ')
                    stdout.write('PR%')
                if (chunk == ''):
                    break
                f2.write(chunk)
            f.close()
            f2.close()
            print ""
        elif (src == 'gui'):
            return f, f2, total / 1048576.0

    def __init__(self, link, system=None, dest=None, size=1024*8):
        if (system == None):
            system = link.split('/')[-3]
        # Fetch the download link
        if (system in self.abbrs.keys()):
            #print('dlink = self.getlink' + self.abbrs[system] + '("' + link + '")')
            exec('dlink = self.getlink' + self.abbrs[system] + '("' + link + '")')
        elif ((system in self.abbrs.values()) and (system in self.abbrs2.keys())):
            #print('dlink = self.getlink' + self.abbrs2[system] + '("' + link + '")')
            exec('dlink = self.getlink' + system + '("' + link + '")')
        else:
            raise BaseException, "System not accepted"
        # Open the download link to get the 2nd download page link
        #print(dlink)
        f = urllib.URLopener().open(dlink)
        data = f.read()
        f.close()
        # Fetch the file download link
        flink = self.geturl(data)
        # Download the file
        #print(flink)
        self.download(flink, dest, size)

if __name__ == '__main__':
    DL = DownloadLink(raw_input("Enter the url here:\n=> "))
