'''
____________CALCULATION PART______________
Input: a, b - side lengths of a rectangle rotated 45 deg to clockwise.
a, b -- even integers
Output: points with integer coordinates inside the given rectangle
        including on its sides
1) Rotate base vectors by 45 deg clockwise
2) Apply lintranform of (a/2, 0) and (0, b/2)
3) Find coordinates of 3 other points
4) Calculate integer points in rectangle
    - go by y-axis with int step:
        - in range(lb, rb) ccount int
'''
import numpy as np
from draw_rectangle import draw_rectangle

def make_line(c0, c1):
    m = round((c1[1] - c0[1]) / (c1[0] - c0[0]))
    b = c0[1] - m*c0[0]
    def line_eq(x):
        return m*x + b
    return line_eq

def rectangle_rotation(a, b):
    rotation_base = np.array([[np.cos(np.pi/4), np.cos(np.pi/4)],
                          [-np.sin(np.pi/4), np.sin(np.pi/4)]])
    vecs = np.array([[b/2, a/2], [b/2, -a/2], [-b/2, -a/2], [-b/2, a/2]]).transpose()
    rot_vecs = np.dot(rotation_base, vecs)
    x, y = 1, 3
    if a < b:
        x, y = y, x
    low_x, high_x = int(rot_vecs[0, 2]), int(rot_vecs[0, 0])
    # making equation for sides of a rectangle
    line1, line2 = make_line(rot_vecs[:,3], rot_vecs[:,0]), make_line(rot_vecs[:,0], rot_vecs[:,1])
    line3, line4 = make_line(rot_vecs[:,1], rot_vecs[:,2]), make_line(rot_vecs[:,2], rot_vecs[:,3])
    rect_ints = 0
    for col in range(int(low_x), int(high_x) + 1):
        if  col <= rot_vecs[0, x]:
            upb, lowb = line4(col), line3(col)
        elif col <= rot_vecs[0, y]:
            if a > b:
                upb, lowb = line4(col), line2(col)
            elif a < b:
                upb, lowb = line1(col), line3(col)
        else:
            upb, lowb = line1(col), line2(col)

        if lowb > upb:
            lowb, upb = upb, lowb
        rect_ints += round(np.floor(upb) - np.floor(lowb))
    return rect_ints
a = list(map(int, input().split()))
print(rectangle_rotation(a[0], a[1]))
draw_rectangle(a[0], a[1])

