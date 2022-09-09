import random

def make_wing_set(top_wing, start, coords, absCoord, sharedRandom):

    start, coords = scale(start, coords, (.8 + sharedRandom)/5)

    left, right, top, bottom = get_max_coords(start, coords)
    width, height = right - left, bottom - top

    colors = ["#FF0000","#00FF00","#0000FF"]

    blocks = []
    
    for i in range(3):
        start, coords = scale(start, coords, 2) #) + (.1 * i))
        coords = jitter_coords(coords, 1, 1)
        ts, tc = translate_absolute(start, coords, absCoord[0] - width/2, absCoord[1])
        ts, tc = scale(ts, tc, 1) 
        ts, tc = translate_absolute(ts, tc, absCoord[0] + width/2, absCoord[1])
        blocks.append(sub_coords(top_wing, ts, tc, colors[i]))

        ms, mc = mirrorInPlace(start, coords)
        left, right, top, bottom = get_max_coords(ms, mc)
        width, height = right - left, bottom - top
        ts, tc = translate_absolute(ms, mc, absCoord[0] + width/2, absCoord[1])
        ts, tc = scale(ts, tc, 1) 
        ts, tc = translate_absolute(ts, tc, absCoord[0] + width/2, absCoord[1])
        blocks.append(sub_coords(top_wing, ts, tc))

    return(blocks)

def make_butterfly(top_wing, top_start, top_coords, bottom_wing, bottom_start, bottom_coords, absCenter):

    r = random.random()
    
    blocks1 = make_wing_set(bottom_wing, bottom_start, bottom_coords, absCenter, r) 
    blocks2 = make_wing_set(top_wing, top_start, top_coords, absCenter, r)

    for b in range(len(blocks1)):
        print(blocks1[b])
        print(blocks2[b])


def sub_coords(template, start, coords, col): 
    subbed = {
        "start" :  '%s,%s' % (start[0], start[1]),
        "fill"  : col
    }

    coord_list = []
    for c in coords:
        coord_list.append('%s,%s' % (c[0], c[1]))

    subbed['coords'] = " ".join(coord_list)

    return(template.format(**subbed))



def jitter_coords(coords, alternate, weight):

    jittered = []
    
    i = 0
    for c in coords:
        if i % alternate == 0:
            jittered.append((c[0] + weight/2 - (random.random() * weight), c[1] + weight/2 - random.random() * weight))
        
    return(jittered)

def get_max_coords(start, coords):
    maxX = start[0]
    maxY = start[1]
    minX = start[0]
    minY = start[1]

    x = start[0]
    y = start[1]

    for c in coords:
        x = x + c[0]
    if x > maxX:
         maxX = x
    if x < minX:
        minX = x
    y = y + c[1]
    if y > maxY:
        maxY = y
    if y < minY:
        minY = y

    return(minX, maxX, minY, maxY)

def scale(start, coords, scale_factor):

    s_start = (start[0]/scale_factor, start[1]/scale_factor)
    s_coords = []
    for c in coords:
        s_coords.append((c[0]/scale_factor, c[1]/scale_factor))
    return(s_start, s_coords)

def mirrorInPlace(start, coords):
    left, right, top, bottom = get_max_coords(start, coords)

    s_start = (right, start[1])
    s_coords = []
    for c in coords:
        s_coords.append((-c[0], c[1]))
    return(s_start, s_coords)

def translate(start, coords, xShift, yShift):
    s_start = (start[0] + xShift, start[1] + yShift)
    return(s_start, coords)

def translate_absolute(start, coords, xShift, yShift):
    s_start = (xShift, yShift)
    return(s_start, coords)


if __name__ == "__main__":
    absCenter = 100, 100
    random.seed(110)

    top_start = 16.710892 + absCenter[0], 28.74997 + absCenter[1]
    top_coords = [(-0.880195,-2.04791), (-2.497674,-4.69467), (-4.299363,-6.65651), (-1.80169,-1.96184), (-3.7875911,-3.23876), (-5.4046324,-2.54699), (-0.7490921,0.32046), (-1.0092515,0.89281), (-1.047765,1.61855), (-0.038513,0.72574), (0.1446188,1.60487), (0.2821098,2.53889), (0.1159338,0.78758), (0.1411582,1.62825), (0.237872,2.38513), (0.096714,0.75688), (0.2649172,1.42997), (0.6668087,1.88239), (1.0975367,1.23553), (2.831987,2.39035), (4.6204489,2.98558), (1.788462,0.59524), (3.630937,0.6309), (4.944521,-0.3719), (0.243112,-0.18559), (0.303499,-0.50388), (0.272915,-0.84601), (-0.03058,-0.34214), (-0.15214,-0.70813), (-0.272915,-0.98913)]

    bottom_start = 15.987958 + absCenter[0], 28.49972 + absCenter[1]
    bottom_coords = [(-1.601127,-0.31997), (-3.402884,-0.3122), (-4.953125,0.11577), (-1.5502402,0.42797), (-2.8489649,1.27614), (-3.4440284,2.63695), (-0.2909255,0.6653), (-0.1372829,1.34765), (0.176497,2.05578), (0.3137799,0.70812), (0.7876971,1.44201), (1.1373212,2.21038), (0.355901,0.78216), (0.5920684,1.59628), (0.9226857,2.23728), (0.3306175,0.641), (0.7556845,1.10888), (1.4893855,1.19858), (1.423531,0.17404), (2.636726,-0.77682), (3.579094,-2.11949), (0.942368,-1.34267), (1.613908,-3.07714), (1.95413,-4.47033), (0.156569,-0.64114), (0.264669,-1.5427), (0.171833,-2.31631), (-0.09284,-0.77361), (-0.386612,-1.41927), (-1.033793,-1.54861)]

    top_wing = """<path
    id="path826"
    d="m {start} c {coords} z"
    style="fill:{fill};stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />"""

    bottom_wing = """<path
    id="path828"
    d="m {start} c {coords} z"
    style="fill:{fill}};stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />"""

    
    head = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:cc="http://creativecommons.org/ns#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:svg="http://www.w3.org/2000/svg"
    xmlns="http://www.w3.org/2000/svg"
    id="svg8"
    version="1.1"
    viewBox="0 0 1000 1000"
    height="45mm"
    width="45mm">
    <defs
    id="defs2" />
    <metadata
    id="metadata5">
    <rdf:RDF>
    <cc:Work
    rdf:about="">
    <dc:format>image/svg+xml</dc:format>
    <dc:type
    rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
    <dc:title></dc:title>
    </cc:Work>
    </rdf:RDF>
    </metadata>"""
    print(head)

    #makeButterfly(top_wing, top_start, top_coords, bottom_wing, bottom_start, bottom_coords, absCenter)

    spacer = 100
    for i in range(4):
        for j in range(4):
                c = absCenter[0] + i * spacer, absCenter[1] + j * spacer
                make_butterfly(top_wing, top_start, top_coords, bottom_wing, bottom_start, bottom_coords, c)

    print("</svg>")