import sys

def draw_arc(iter, iter_max, template, quatrafoil_chunk, coords, scale_factor):
    
    print(path_chunk.format(**coords))
    print(quatrafoil_chunk.format(**coords))

    if iter < iter_max:

        parent_internal_width = (coords["arc_dx"] * 2) - coords["calc_stroke_width"] 
        new_coords = {}
        for k in coords:
            new_coords[k] = coords[k]

        new_coords["calc_stroke_width"] = coords["calc_stroke_width"]/scale_factor
        new_coords["arc_dx"] = (parent_internal_width/4)  - (new_coords["calc_stroke_width"])/2
        new_coords["arc_dy"] = coords["arc_dy"] * (new_coords["arc_dx"]/coords["arc_dx"])
        new_coords["start_x"] += (new_coords["calc_stroke_width"] + coords["calc_stroke_width"])/2
        radius = (new_coords["arc_dy"]**2 + new_coords["arc_dx"]**2)**0.5

        new_coords["rx"]  = radius
        new_coords["ry"]  = radius
        new_coords["qrx"] = radius/20
        new_coords["qry"] = radius/20
        new_coords['q_start_x'] = new_coords["start_x"] + (new_coords["arc_dx"]/1.1)
        new_coords['q_start_y'] = new_coords["q_start_x"]
        new_coords['qf_dist'] = new_coords["arc_dx"] / 5


        draw_arc(iter+1, iter_max, template, quatrafoil_chunk, new_coords, scale_factor)

        new_coords["start_x"] += parent_internal_width/2 
        new_coords['q_start_x'] = new_coords["start_x"] + (new_coords["arc_dx"]/1.1)
        new_coords['qf_dist'] = new_coords["arc_dx"] / 5
        draw_arc(iter+1, iter_max, template, quatrafoil_chunk, new_coords, scale_factor)
    


if __name__ == "__main__":

    print("""<svg width="1000" height="1000" xmlns="http://www.w3.org/2000/svg">
    <rect
     style="opacity:1;vector-effect:none;fill:#4d4d4d;fill-opacity:1"
     width="800"
     height="480"
     x="0"
     y="0"
     />
     """)
            
    
    path_chunk = """<path d="M {start_x} {start_y}
    v -{vertical}
    a {rx} {ry} 0 0 1 {arc_dx} -{arc_dy}
    a {rx} {ry} 0 0 1 {arc_dx} {arc_dy}
    v {vertical}"
        stroke-width="{stroke_width}" stroke="{fill}" fill-opacity="0"/>"""

    quatrafoil_chunk = """<path d="M {q_start_x} {q_start_y}
    a {qrx} {qry} 0 0 1 {qf_dist} 0
    a {qrx} {qry} 0 0 1 0 {qf_dist}
    a {qrx} {qry} 0 0 1 -{qf_dist} 0
    a {qrx} {qry} 0 0 1 0 -{qf_dist}
    z"
    stroke-width="{stroke_width}" stroke="{fill}" fill-opacity="0"/>"""

    radius = 800
    arc_dx = 536
    arc_dy = (radius**2 - arc_dx**2)**0.5
    
    calc_stroke_width = 10
    visual_stroke_width = 100
    stroke_width_scale_factor = 1.4

    coords = {
        "start_x" : 0,
        "start_y" : 480,
        "vertical": 100,
        "rx" : radius,
        "ry" : radius,
        "qrx" : radius/20,
        "qry" : radius/20,
        "arc_dx" : arc_dx,
        "arc_dy" : arc_dy,
        "stroke_width" : visual_stroke_width,
        "calc_stroke_width" : calc_stroke_width,
        "fill" : "#404040"
    }
    coords['q_start_x'] = coords["start_x"] + (coords["arc_dx"]/1.1)
    coords['q_start_y'] = coords["start_x"]
    coords['qf_dist'] = coords["arc_dx"] / 5

    colors = ["#4d4d4d", "#404040"]
    for x in range(10):
        draw_arc(0, 7, path_chunk, quatrafoil_chunk, coords, stroke_width_scale_factor)
        coords["stroke_width"] /= 2
        coords["fill"] = colors[x % 2]


    print("""</svg>""")


    


