import sys
from cairosvg import svg2png
import xml.etree.cElementTree as ET


base_tones = [
    "#000051",
    "#175a13",
    "#98131c",
    "#bf8600",
    "#5a133b",
]



if __name__ == "__main__":

    #colors = ["#aa0011", "#371f76", "#ffd0aa"]
    #glagolitic = 'ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰉⰊⰋⰌⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰟⰠⰡⰢ'


    light =    ['#9984d4','#d5a6bd','#e8eba0', ]
    primary =  ['#FF00FF','#ff0202','#FFFF00', '#00FF00']
    dark =     ['#230c33','#3E0303','#652900', "#006400"]

    colors = ['#9984d4','#FF00FF','#230c33']
    to_replace = ('#00ff00', '#00ffff', '#ff0000')
    template_files = ['template1.svg', 'template2.svg','template3.svg',
                      'template4.svg', 'template5.svg','template6.svg',
                      'template7.svg', 'template8.svg', 'template9.svg']


    color_lists = [
        
    ]

    for i in range(3):
        color_lists.append([light[i], primary[(i+2)%3], dark[(i+1)%3]])

    c = 0
    for colors in color_lists:
        for t in range(8):
            with open(template_files[t], 'r') as template_file:
                orig_svg_str = template_file.read()
                
                for i in range(3):

                    c1 = colors[i]
                    c2 = colors[(i+1)%3]
                    c3 = colors[(i+2)%3]

                    print(c1, c2, c3)
                    svg_str = orig_svg_str.replace(to_replace[0], c1)
                    svg_str = svg_str.replace(to_replace[1], c2)
                    svg_str = svg_str.replace(to_replace[2], c3)
                    svg2png(bytestring=svg_str,write_to=f"icons/icon{t}{i}{c}.png")
        c+=1 

