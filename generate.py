import os

# Standard Piet Palette
colors = {
    'LR': (255, 192, 192), 'NR': (255, 0, 0),   'DR': (192, 0, 0),
    'LY': (255, 255, 192), 'NY': (255, 255, 0), 'DY': (192, 192, 0),
    'LG': (192, 255, 192), 'NG': (0, 255, 0),   'DG': (0, 192, 0),
    'LC': (192, 255, 255), 'NC': (0, 255, 255), 'DC': (0, 192, 192),
    'LB': (192, 192, 255), 'NB': (0, 0, 255),   'DB': (0, 0, 192),
    'LM': (255, 192, 255), 'NM': (255, 0, 255), 'DM': (192, 0, 192),
    'W':  (255, 255, 255), 'B':  (0, 0, 0)
}

palette = {
    'S1': (10, 20, 40),    'S2': (20, 50, 90),    'S3': (40, 90, 140),
    'S4': (70, 140, 170),  'S5': (100, 180, 180), 'S6': (130, 210, 170),
    'S7': (170, 230, 160), 'S8': (210, 240, 140), 'S9': (240, 220, 80),
    'S10': (255, 150, 50)
}

def apply_math_logic(image, bg_color, cw=1, ch=1):
    def fill(r, c, col):
        for i in range(r*ch, (r+1)*ch):
            for j in range(c*cw, (c+1)*cw):
                image[i][j] = col

    # Background
    for r in range(10):
        for c in range(12): fill(r, c, bg_color)

    # Init
    fill(0, 0, colors['LR']); fill(0, 1, colors['NR'])
    fill(0, 2, colors['LG']); fill(0, 3, colors['NG'])
    fill(0, 4, colors['W'])
    
    # Loop entry
    fill(0, 5, colors['LR']); fill(0, 6, colors['LB']); fill(0, 7, colors['LG'])
    
    # Push 10
    fill(0, 8, colors['NY']); fill(0, 9, colors['NY']); fill(0, 10, colors['NY'])
    for j in range(1, 8): fill(j, 10, colors['NY'])
    fill(8, 10, colors['DY'])
    
    # out(c) and swap
    fill(8, 9, colors['NR']); fill(8, 8, colors['NR']); fill(8, 7, colors['NR'])
    fill(8, 6, colors['DR']); fill(8, 5, colors['LR'])
    fill(7, 5, colors['NB']); fill(6, 5, colors['NM'])
    for j in range(1, 6): fill(j, 5, colors['W'])

    # Bumpers
    fill(0, 11, colors['B']); fill(9, 10, colors['B']); fill(8, 4, colors['B'])

def save_ppm(filename, image, width, height):
    with open(filename, "w") as f:
        f.write(f"P3\n{width} {height}\n255\n")
        for row in image:
            for c in row: f.write(f"{c[0]} {c[1]} {c[2]} ")
            f.write("\n")

def generate():
    # 1. Aesthetic
    w, h = 377, 233
    aesthetic = [[(255, 255, 255) for _ in range(w)] for _ in range(h)]
    def draw_rect(img, rx, ry, rw, rh, col):
        for j in range(ry, ry+rh):
            for i in range(rx, rx+rw):
                if 0 <= i < w and 0 <= j < h: img[j][i] = col
    draw_rect(aesthetic, 0, 0, 233, 233, palette['S1'])
    draw_rect(aesthetic, 233, 0, 144, 144, palette['S2'])
    draw_rect(aesthetic, 288, 144, 89, 89, palette['S3'])
    draw_rect(aesthetic, 233, 178, 55, 55, palette['S4'])
    draw_rect(aesthetic, 233, 144, 34, 34, palette['S5'])
    draw_rect(aesthetic, 267, 144, 21, 21, palette['S6'])
    draw_rect(aesthetic, 275, 165, 13, 13, palette['S7'])
    draw_rect(aesthetic, 267, 170, 8, 8, palette['S8'])
    draw_rect(aesthetic, 267, 165, 5, 5, palette['S9'])
    draw_rect(aesthetic, 272, 165, 3, 3, palette['S10'])
    apply_math_logic(aesthetic, palette['S1'])
    save_ppm("fib_aesthetic.ppm", aesthetic, w, h)

    # 2. Minimalist
    mw, mh = 12, 10
    mini = [[colors['B'] for _ in range(mw)] for _ in range(mh)]
    apply_math_logic(mini, colors['B'])
    save_ppm("fib_minimal.ppm", mini, mw, mh)

    # 3. Logic Grid (Upscaled)
    scale = 40
    gw, gh = mw * scale, mh * scale
    grid = [[(50, 50, 50) for _ in range(gw)] for _ in range(gh)]
    # We apply logic with 'codel' size of scale, but keep 1px gap for grid
    def fill_grid(r, c, col):
        for i in range(r*scale + 1, (r+1)*scale - 1):
            for j in range(c*scale + 1, (c+1)*scale - 1):
                grid[i][j] = col
    
    # Manual apply to grid to handle the custom fill
    # Background
    for r in range(10):
        for c in range(12): fill_grid(r, c, colors['B'])
    fill_grid(0, 0, colors['LR']); fill_grid(0, 1, colors['NR'])
    fill_grid(0, 2, colors['LG']); fill_grid(0, 3, colors['NG'])
    fill_grid(0, 4, colors['W'])
    fill_grid(0, 5, colors['LR']); fill_grid(0, 6, colors['LB']); fill_grid(0, 7, colors['LG'])
    fill_grid(0, 8, colors['NY']); fill_grid(0, 9, colors['NY']); fill_grid(0, 10, colors['NY'])
    for j in range(1, 8): fill_grid(j, 10, colors['NY'])
    fill_grid(8, 10, colors['DY'])
    fill_grid(8, 9, colors['NR']); fill_grid(8, 8, colors['NR']); fill_grid(8, 7, colors['NR'])
    fill_grid(8, 6, colors['DR']); fill_grid(8, 5, colors['LR'])
    fill_grid(7, 5, colors['NB']); fill_grid(6, 5, colors['NM'])
    for j in range(1, 6): fill_grid(j, 5, colors['W'])
    fill_grid(0, 11, colors['B']); fill_grid(9, 10, colors['B']); fill_grid(8, 4, colors['B'])
    
    save_ppm("fib_logic_grid.ppm", grid, gw, gh)

generate()
os.system("sips -s format png fib_aesthetic.ppm --out fib_aesthetic.png")
os.system("sips -s format png fib_minimal.ppm --out fib_minimal.png")
os.system("sips -s format png fib_logic_grid.ppm --out fib_logic_grid.png")
os.system("rm *.ppm")
