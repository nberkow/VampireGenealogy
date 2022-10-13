import sys
import random
from cairosvg import svg2png

if __name__ == '__main__':

    templates = ["bheart1.svg", "bheart2.svg", "bheart3.svg"]
    outdir = 'bheart'

    colorSets = [
        ["#BA7E8D", "#7b7be8", "#c89aed", "#FFFFFF", "#000000", "#330000", "#003333"],
        ["#394672", "#BA7E8D", "#7b7be8", "#c89aed", "#FFFFFF", "#000000"],
        ["#771b48", "#c89aed", "#394672", "#BA7E8D", "#394672", "#FFFFFF", "#000000"]
    ]

    cs = 0
    for colors in colorSets:
        size = 80
        for k in range(10):
            i = 0
            for t in templates:
                for j in range(3):
                    with open(t, 'r') as svg:
                        svg_content = svg.read()
                        
                        substituted = svg_content.replace("#00ff00", colors[0])
                        substituted = substituted.replace("#00ffff", colors[1])
                        c = substituted.count("#ff0000")
                        toSub = "#ff0000"
                        while c > 0:
                            newCol = random.choice(colors[2:])
                            substituted = substituted.replace(toSub, newCol, c)
                            toSub = newCol
                            c-=1
                            print(newCol)
                        svg2png(bytestring=substituted,write_to=f"bheart/bheart_{cs}{k}{i}{j}.png", output_width=size)
                i+=1
            size /= 1.1
        cs+=1