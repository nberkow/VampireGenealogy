import math
import random
from cairosvg import svg2png


def random_color():
    return(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_blend(color_1, color_2):

    blended = [0,0,0]
    for i in range(3):
        p = random.random()
        q = 1 - p
        blended[i] = math.floor((color_1[i] * p) + (color_2[i] * q))
    return((blended[0],blended[1],blended[2],))

def to_hex(color):
    return('#%02x%02x%02x' % color)

def compute_color_diff(c1, c2):
    d = ((c1[0] - c2[0])**2 + (c1[0] - c2[0])**2 + (c1[0] - c2[0])**2)**0.5
    return(d)

def compute_palette_diff(p1, p2):
    d = 0
    for i in range(3):
        d+= compute_color_diff(p1[i], p2[i])
    return(d)

if __name__ == "__main__":
    out_path = "/mnt/c/Users/Narthan/Projects/assets/icons/behives/"
    with open('template6.svg', 'r') as template_file:
        orig_svg_str = template_file.read()

    to_replace = ('#00ff00', '#00ffff', '#ff0000')
    color_sets = {
        'jewel' : [(5,135,138), (7,78,103), (90,23,93), (103,7,78), (221,153,51)],
        'earth' : []
    }

    c1, c2, c3 = ((100, 149, 237), (132, 31, 39), (203, 171, 84))
    used_palettes = []

    for i in range(25):

        svg_str = orig_svg_str.replace(to_replace[0], to_hex(c1))
        svg_str = svg_str.replace(to_replace[1], to_hex(c2))
        svg_str = svg_str.replace(to_replace[2], to_hex(c3))
        used_palettes.append((c1, c2, c3))

        a1, a2, a3 = c1, c2, c3
        pd = 0
        found_new = False
        while not found_new:

            #rc = random_color()
            c1 = random_blend(a1, random_color())
            c2 = random_blend(a2, random_color())
            c3 = random_blend(a3, random_color())

            found_new = True
            for u in used_palettes:
                pd = compute_palette_diff((a1, a2, a3), (c1, c2, c3))
                if pd < 300:
                    found_new = False
        
        
        svg2png(bytestring=svg_str,write_to=f"{out_path}/icon-{to_hex(c1)}-{to_hex(c2)}-{to_hex(c3)}.png")