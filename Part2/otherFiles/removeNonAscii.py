non-ascii characters
#!/usr/bin/env python
nonascii = bytearray(range(0x80, 0x100))
with open('commoncrawl.txt','rb') as infile, open('commoncrawl_final.txt','wb') as outfile:
    for line in infile: # b'\n'-separated lines (Linux, OSX, Windows)
        outfile.write(line.translate(None, nonascii))
