import math
import sys

def generate_gable(span=20.0, height=3.0):
    print("# Nodos")
    print(f"cache.AddNode(1, 0.0, 0.0, 0.0)")
    print(f"cache.AddNode(2, {span:.1f}, 0.0, 0.0)")
    print(f"cache.AddNode(3, {span/2:.1f}, {height:.1f}, 0.0)")
    print("\n# Barras con sección")
    print('cache.AddBar(1, 1, 3, "IPE 200", "S235")')
    print('cache.AddBar(2, 3, 2, "IPE 200", "S235")')
    print('cache.AddBar(3, 1, 2, "IPE 200", "S235")')

def generate_mono_pitch(span=20.0, height_left=5.0, height_right=2.0):
    print("# Nodos")
    print(f"cache.AddNode(1, 0.0, 0.0, 0.0)")
    print(f"cache.AddNode(2, {span:.1f}, 0.0, 0.0)")
    print(f"cache.AddNode(3, 0.0, {height_left:.1f}, 0.0)")
    print(f"cache.AddNode(4, {span:.1f}, {height_right:.1f}, 0.0)")
    print("\n# Barras con sección")
    print('cache.AddBar(1, 1, 3, "IPE 200", "S235")')
    print('cache.AddBar(2, 2, 4, "IPE 200", "S235")')
    print('cache.AddBar(3, 3, 4, "IPE 200", "S235")')

def generate_arched(span=20.0, height=3.0, n_segments=10):
    r = ((span / 2) ** 2 + height ** 2) / (2 * height)
    print("# Nodos")
    for i in range(n_segments + 1):
        node_id = i + 1
        x = i * (span / n_segments)
        dx = x - span / 2
        y = math.sqrt(r ** 2 - dx ** 2) - (r - height)
        print(f"cache.AddNode({node_id}, {x:.1f}, {y:.1f}, 0.0)")
    print("\n# Barras con sección")
    for i in range(n_segments):
        bar_id = i + 1
        print(f'cache.AddBar({bar_id}, {i + 1}, {i + 2}, "IPE 200", "S235")')

def generate_pratt(span=20.0, height=3.0, panels=5):
    l = span / panels
    print("# Nodos")
    node_id = 1
    bottom = {}
    for i in range(panels + 1):
        x = i * l
        y = 0.0
        print(f"cache.AddNode({node_id}, {x:.1f}, {y:.1f}, 0.0)")
        bottom[i] = node_id
        node_id += 1
    top = {}
    for i in range(panels + 1):
        x = i * l
        y = height
        print(f"cache.AddNode({node_id}, {x:.1f}, {y:.1f}, 0.0)")
        top[i] = node_id
        node_id += 1
    print("\n# Barras con sección")
    bar_id = 1
    for i in range(panels):  # bottom chord
        print(f'cache.AddBar({bar_id}, {bottom[i]}, {bottom[i+1]}, "IPE 200", "S235")')
        bar_id += 1
    for i in range(panels):  # top chord
        print(f'cache.AddBar({bar_id}, {top[i]}, {top[i+1]}, "IPE 200", "S235")')
        bar_id += 1
    for i in range(1, panels):  # verticals
        print(f'cache.AddBar({bar_id}, {top[i]}, {bottom[i]}, "IPE 200", "S235")')
        bar_id += 1
    for i in range(panels):  # diagonals (Pratt: top to bottom next)
        print(f'cache.AddBar({bar_id}, {top[i]}, {bottom[i+1]}, "IPE 200", "S235")')
        bar_id += 1

def generate_warren(span=20.0, height=3.0, panels=5):
    l = span / panels
    print("# Nodos")
    node_id = 1
    bottom = {}
    for i in range(panels + 1):
        x = i * l
        y = 0.0
        print(f"cache.AddNode({node_id}, {x:.1f}, {y:.1f}, 0.0)")
        bottom[i] = node_id
        node_id += 1
    top = {}
    for i in range(panels):
        x = (i + 0.5) * l
        y = height
        print(f"cache.AddNode({node_id}, {x:.1f}, {y:.1f}, 0.0)")
        top[i] = node_id
        node_id += 1
    print("\n# Barras con sección")
    bar_id = 1
    for i in range(panels):  # bottom chord
        print(f'cache.AddBar({bar_id}, {bottom[i]}, {bottom[i+1]}, "IPE 200", "S235")')
        bar_id += 1
    for i in range(panels - 1):  # top chord
        print(f'cache.AddBar({bar_id}, {top[i]}, {top[i+1]}, "IPE 200", "S235")')
        bar_id += 1
    for i in range(panels):  # diagonals zig-zag
        print(f'cache.AddBar({bar_id}, {bottom[i]}, {top[i]}, "IPE 200", "S235")')
        bar_id += 1
        print(f'cache.AddBar({bar_id}, {top[i]}, {bottom[i+1]}, "IPE 200", "S235")')
        bar_id += 1

def generate_howe(span=20.0, height=3.0, panels=5):
    l = span / panels
    print("# Nodos")
    node_id = 1
    bottom = {}
    for i in range(panels + 1):
        x = i * l
        y = 0.0
        print(f"cache.AddNode({node_id}, {x:.1f}, {y:.1f}, 0.0)")
        bottom[i] = node_id
        node_id += 1
    top = {}
    for i in range(panels + 1):
        x = i * l
        y = height
        print(f"cache.AddNode({node_id}, {x:.1f}, {y:.1f}, 0.0)")
        top[i] = node_id
        node_id += 1
    print("\n# Barras con sección")
    bar_id = 1
    for i in range(panels):  # bottom chord
        print(f'cache.AddBar({bar_id}, {bottom[i]}, {bottom[i+1]}, "IPE 200", "S235")')
        bar_id += 1
    for i in range(panels):  # top chord
        print(f'cache.AddBar({bar_id}, {top[i]}, {top[i+1]}, "IPE 200", "S235")')
        bar_id += 1
    for i in range(1, panels):  # verticals
        print(f'cache.AddBar({bar_id}, {top[i]}, {bottom[i]}, "IPE 200", "S235")')
        bar_id += 1
    for i in range(panels):  # diagonals (Howe: bottom to top next)
        print(f'cache.AddBar({bar_id}, {bottom[i]}, {top[i+1]}, "IPE 200", "S235")')
        bar_id += 1

def generate_fink(span=20.0, height=3.0):
    print("# Nodos")
    print(f"cache.AddNode(1, 0.0, 0.0, 0.0)")  # left eave
    print(f"cache.AddNode(2, {span:.1f}, 0.0, 0.0)")  # right eave
    print(f"cache.AddNode(3, {span/2:.1f}, {height:.1f}, 0.0)")  # apex
    print(f"cache.AddNode(4, {span/4:.1f}, {height/2:.1f}, 0.0)")  # mid left top
    print(f"cache.AddNode(5, {3*span/4:.1f}, {height/2:.1f}, 0.0)")  # mid right top
    print(f"cache.AddNode(6, {span/2:.1f}, 0.0, 0.0)")  # mid bottom
    print("\n# Barras con sección")
    print('cache.AddBar(1, 1, 4, "IPE 200", "S235")')  # top left 1
    print('cache.AddBar(2, 4, 3, "IPE 200", "S235")')  # top left 2
    print('cache.AddBar(3, 3, 5, "IPE 200", "S235")')  # top right 1
    print('cache.AddBar(4, 5, 2, "IPE 200", "S235")')  # top right 2
    print('cache.AddBar(5, 1, 6, "IPE 200", "S235")')  # bottom left
    print('cache.AddBar(6, 6, 2, "IPE 200", "S235")')  # bottom right
    print('cache.AddBar(7, 4, 6, "IPE 200", "S235")')  # diagonal left
    print('cache.AddBar(8, 5, 6, "IPE 200", "S235")')  # diagonal right

def generate_portal_pitched(span=20.0, col_height=5.0, rise=1.5):
    apex_height = col_height + rise
    print("# Nodos")
    print(f"cache.AddNode(1, 0.0, 0.0, 0.0)")
    print(f"cache.AddNode(2, {span:.1f}, 0.0, 0.0)")
    print(f"cache.AddNode(3, 0.0, {col_height:.1f}, 0.0)")
    print(f"cache.AddNode(4, {span:.1f}, {col_height:.1f}, 0.0)")
    print(f"cache.AddNode(5, {span/2:.1f}, {apex_height:.1f}, 0.0)")
    print("\n# Barras con sección")
    print('cache.AddBar(1, 1, 3, "IPE 200", "S235")')
    print('cache.AddBar(2, 2, 4, "IPE 200", "S235")')
    print('cache.AddBar(3, 3, 5, "IPE 200", "S235")')
    print('cache.AddBar(4, 5, 4, "IPE 200", "S235")')

def generate_portal_flat(span=20.0, col_height=5.0):
    print("# Nodos")
    print(f"cache.AddNode(1, 0.0, 0.0, 0.0)")
    print(f"cache.AddNode(2, {span:.1f}, 0.0, 0.0)")
    print(f"cache.AddNode(3, 0.0, {col_height:.1f}, 0.0)")
    print(f"cache.AddNode(4, {span:.1f}, {col_height:.1f}, 0.0)")
    print("\n# Barras con sección")
    print('cache.AddBar(1, 1, 3, "IPE 200", "S235")')
    print('cache.AddBar(2, 2, 4, "IPE 200", "S235")')
    print('cache.AddBar(3, 3, 4, "IPE 200", "S235")')

if __name__ == "__main__":
    print("## Gable (a dos aguas simple para cobertura)")
    generate_gable()
    print("\n## Mono-pitch (a una agua para cobertura)")
    generate_mono_pitch()
    print("\n## Arqueada (aproximación poligonal para cobertura)")
    generate_arched()
    print("\n## Pratt truss (para cercha)")
    generate_pratt()
    print("\n## Warren truss (para cercha)")
    generate_warren()
    print("\n## Howe truss (para cercha)")
    generate_howe()
    print("\n## Fink truss (para cercha, pitched)")
    generate_fink()
    print("\n## Portal frame pitched (para nave industrial)")
    generate_portal_pitched()
    print("\n## Portal frame flat (para nave industrial)")
    generate_portal_flat()