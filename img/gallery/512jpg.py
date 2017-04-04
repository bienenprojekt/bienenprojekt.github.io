import os, sys
import Image

size = 300, 200

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumb.jpg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "jpeg")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile