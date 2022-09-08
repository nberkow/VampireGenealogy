import sys
from cairosvg import svg2png
import xml.etree.cElementTree as ET


if __name__ == "__main__":



    colors = [["#4FC000", "#FF1EA3", "#EAADFA", "#833AB2", "#72B67A", "#FFDD03"],
              ["#CCA840", "#1EA3FF", "#ADFAEA", "#3AB283", "#B67A72", "#FD03FF"]]

    colors = [["#004949","#009292","#ff6db6","#ffb6db", "#490092","#006ddb","#ffff6d"],
              ["#b66dff","#6db6ff","#b6dbff","#920000","#924900","#db6d00","#24ff24"]]

    suffixes = ['fear','power']

    j = 0
    for s in suffixes:
        with open("mini_template_" + s + ".svg", 'r') as template_file:
            i = 0
            orig_svg_str = template_file.read()
            for col in colors[j]:
                svg_str = orig_svg_str.replace('#ff0000', col)
                print(f'mini_icons/{s}_{i}.png')
                try:
                    svg2png(bytestring=svg_str,write_to=f'mini_icons/{s}_{i}.png',output_width=25)
                except:
                    pass
                i+=1
        j+=1
