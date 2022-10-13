
import random
import sys
from cairosvg import svg2png


def scale(start, coords, scale_factor):
    s_start = (start[0]/scale_factor, start[1]/scale_factor)
    s_coords = []
    for c in coords:
        s_coords.append((c[0]/scale_factor, c[1]/scale_factor))
    return(s_start, s_coords)

def translate(start, coords, xShift, yShift):
    s_start = (start[0] + xShift, start[1] + yShift)
    return(s_start, coords)

def translate_absolute(start, coords, xShift, yShift):
    s_start = (xShift, yShift)
    return(s_start, coords)

if __name__ == "__main__":

    colors = ['#440000', "#782ab5", "#004444", '#444400', "#000000", "#782ab5", "#222222", "#782ab5", "#222222", "#000000"]
    butterfly_files = ["butterfly1.svg", "butterfly2.svg", "butterfly3.svg",
                        "butterfly4.svg", "butterfly5.svg", "butterfly6.svg",
                        "butterfly5.svg", "butterfly8.svg", "butterfly9.svg"]
    to_replace = ('#00ff00', '#00ff00', '#ff0000')

    j = 0
    for b in butterfly_files:

        with open(b, 'r') as template_file:
            orig_svg_str = template_file.read()
            
            for i in range(10):
                c1 = colors[i]
                c2 = colors[(i+1)%5]
                c3 = colors[(i+2)%5]


                svg_str = orig_svg_str.replace(to_replace[0], c1)
                svg_str = svg_str.replace(to_replace[1], c2)
                svg_str = svg_str.replace(to_replace[2], c3)

                base_size = 10
                for i in range(4):
                    scale = (random.random() * 2) + 0.8
                    jitter = random.random() * 10
                    s = base_size * scale + jitter
                    svg2png(bytestring=svg_str,write_to=f"butterflies/butterfly_{j}.png",output_width=(s))
                    j+=1



