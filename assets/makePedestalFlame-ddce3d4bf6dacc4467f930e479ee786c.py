import sys
from cairosvg import svg2png
import xml.etree.cElementTree as ET


if __name__ == "__main__":



    files = ["pedestalFlame1.svg", "pedestalFlame2.svg", "pedestalFlame3.svg"]
    colors = ["#c89aed", "#7b7be8", "#ffff00", "#00ff00"]

    k = 0
    for f in files:
        with open(f, 'r') as template_file:
            orig_svg_str = template_file.read()
            c = 0
            for col in colors:
                print(c)
                svg_str = orig_svg_str.replace('#ff0000', col)
                svg2png(bytestring=svg_str,write_to=f'png/pedestalFlame_{k}_{c}.png',output_width=100)
                svg2png(bytestring=svg_str,write_to=f'png/pedestalFlame_{k}_{c}_big.png',output_width=150)
                c+=1



        k+=1
        
               

        
