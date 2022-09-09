import sys, os
import xml.sax
import re

class FrameHandler(xml.sax.ContentHandler ):
    def __init__(self, b_xml, f_xml, washout):
        self.b_xml = b_xml
        self.f_xml = f_xml
        self.out_svg = 'NA'
        self.washout = washout

        self.front_added = False
        self.back_added = False
        self.done_defs = False
        self.silent_levels = 0

    # Call when an element starts
    def startElement(self, tag, attributes):
        
        attributes = dict(attributes)

        print("start")
        print(self.silent_levels)
        if tag == 'g' and 'id' in attributes and attributes['id'] in ('Frame', 'BG'):
            self.silent_levels += 1

        elif self.silent_levels > 0 and tag == 'g':
            self.silent_levels += 1

        elif self.silent_levels == 0:
            a_list = []
            for k in attributes:
                if self.washout:
                    attributes[k] = re.sub("#[a-fA-F0-9]{6}", '#FFFFFF', str(attributes[k]))
                a_list.append(f'{k}="{attributes[k]}"')
            print(f"<{tag} {' '.join(a_list)}>", file=self.out_svg)
        print(f"<{tag}>")
        print(self.silent_levels)


    def endElement(self, tag):
            print("end")
            print(self.silent_levels)
            if self.silent_levels == 0:
                if tag == 'svg':
                    print(self.f_xml, file=self.out_svg)
                    
                print(f"</{tag}>")
                print(f"</{tag}>", file=self.out_svg)
            elif tag == 'g' and self.silent_levels > 0:
                self.silent_levels -= 1
            print(self.silent_levels)

            if tag == 'defs':
                self.done_defs = True
            

            if not self.back_added and self.done_defs:
                print(self.b_xml, file=self.out_svg)
                self.back_added = True

    def characters(self, chars):
        if self.silent_levels == 0:
            if self.washout:
                chars = re.sub("#[a-fA-F0-9]{6}", '#000000', chars)
                chars = re.sub("#[a-fA-F0-9]{3}", '#000', chars)

            print(chars)
            print(chars, file=self.out_svg)



if __name__ == "__main__":

    b_xml = open("back_chunk.xml", 'r').read()
    f_xml = open("front_chunk.xml", 'r').read()
    m_xml = open("back_chunk_cloud.xml", 'r').read()
    p_xml = open("profile_frame_chunk.xml", 'r').read()
    
    dir = 'portraits'

    for i in range(80,101):
        target_svg = "%02i.svg" % (i+1)
        out_fname = "%02iw.svg" % (i+1)
        out_fname_mystery = "%02im.svg" % (i+1)
        out_fname_profile = "%02ip.svg" % (i+1)

        with open(os.path.join(dir, target_svg), 'r') as infile, \
             open(os.path.join(dir, out_fname), 'w') as outfile:
    
            fh = FrameHandler(b_xml, f_xml, False)
            fh.out_svg = outfile
            xml.sax.parse(infile, fh)

        with open(os.path.join(dir, target_svg), 'r') as infile, \
             open(os.path.join(dir, out_fname_profile), 'w') as outfile:
    
            fh = FrameHandler("", p_xml, False)
            fh.out_svg = outfile
            xml.sax.parse(infile, fh)

        with open(os.path.join(dir, target_svg), 'r') as infile, \
             open(os.path.join(dir, out_fname_mystery), 'w') as outfile_m:

            fh = FrameHandler(m_xml, "", True)
            fh.out_svg = outfile_m
            xml.sax.parse(infile, fh)

        
