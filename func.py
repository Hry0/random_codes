import os
import sys
import codecs
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3

TEXT_ENCODING = 'utf8'
SET_OTHER_ID3_TAGS = False
 
if (len(sys.argv) > 1):
    fpath = sys.argv[1]
else:
    fpath = os.path.abspath(os.path.dirname(sys.argv[0]))

for fn in os.listdir(fpath):

    fname = os.path.join(fpath, fn)
    if fname.lower().endswith('.mp3'):
        
        lyrics = None
        
        lyrfname = fname[:-3] + 'txt'
        lyrics = open(lyrfname).read().strip()

        # try to find the right encoding
        for enc in ('utf8','iso-8859-1','iso-8859-15','cp1252','cp1251','latin1'):
            try:
                lyrics = lyrics.decode(enc)
                print enc,
                break
            except:
                pass
        
        # create ID3 tag if not exists
        try: 
            tags = ID3(fname)
        except ID3NoHeaderError:
            print "Adding ID3 header"
            tags = ID3()

        # remove old unsychronized lyrics
        if len(tags.getall(u"USLT::'en'")) != 0:
            print "Removing Lyrics."
            tags.delall(u"USLT::'en'")
            tags.save(fname)
            
        #tags.add(USLT(encoding=3, lang=u'eng', desc=u'desc', text=lyrics))
        # apparently the description is important when more than one 
        # USLT frames are present
        tags[u"USLT::'eng'"] = (USLT(encoding=3, lang=u'eng', desc=u'desc', text=lyrics))
        