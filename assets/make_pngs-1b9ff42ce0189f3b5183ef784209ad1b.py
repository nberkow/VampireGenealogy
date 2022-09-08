import sys
from cairosvg import svg2png

if __name__ == "__main__":
    
    for i in range(80):
        froot = "portraits/%02i" % (i+1)
        with open(froot + "w.svg", 'r') as w_file,\
             open(froot + "p.svg", 'r') as p_file,\
             open(froot + "m.svg", 'r') as m_file:

             svg_str = w_file.read()
             svg2png(bytestring=svg_str, write_to=f"%sw.png" % (froot), output_width=95)

             svg_str = p_file.read()
             svg2png(bytestring=svg_str,write_to=f"%sp.png" % (froot), output_width=250)

             svg_str = m_file.read()
             svg2png(bytestring=svg_str,write_to=f"%sm.png" % (froot), output_width=95)

