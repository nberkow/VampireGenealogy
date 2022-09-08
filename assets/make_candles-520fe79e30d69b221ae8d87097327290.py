import sys
from cairosvg import svg2png
import xml.etree.cElementTree as ET


if __name__ == "__main__":


    colors = ["#FFFFFF", "#b83521", "#a8a347", "#7b7be8", "#00AA00", "#0000AA"]

    k = 0
    for s in list(range(6)):
        with open(f"candles/candle{s}.svg", 'r') as template_file:
            orig_svg_str = template_file.read()
            col1 = colors[s]
            
            for i in range(5):
                col2 = colors[(s + i + 1) % 6]
                print(col1, col2)
                svg_str = orig_svg_str.replace('#ff0000', col1)
                svg_str = svg_str.replace('#00ffff', col2)
                svg2png(bytestring=svg_str,write_to=f'png/candles/fear{k}.png',output_width=17)

                svg_str = orig_svg_str.replace('#ff0000', col2)
                svg_str = svg_str.replace('#00ffff', col1)
                svg2png(bytestring=svg_str,write_to=f'png/candles/power{k}.png',output_width=17)
                    

                k+=1
        
               

        
