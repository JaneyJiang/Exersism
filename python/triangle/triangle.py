def is_equilateral(sides):
    if not is_triangle(sides) or len(set(sides)) != 1:
        return False
    return True


def is_isosceles(sides):
    if not is_triangle(sides):
        return False
    if len(set(sides)) <= 2:
        return True
    return False

def is_scalene(sides):
    if not is_triangle(sides) or is_isosceles(sides):
        return False
    return True

def is_triangle(sides):
    if len(sides) != 3:
        return False
    max_side = max(sides)
    slice_sides = sides.copy()
    slice_sides.remove(max_side)
    if max_side >= sum(slice_sides):
        return False
    return True
