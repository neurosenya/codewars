import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def draw_rectangle(a, b):
    rectangle = [(b/2, a/2), (b/2, -a/2), (-b/2, -a/2), (-b/2, a/2)]
    rotation_base = np.array([[np.cos(np.pi/4), np.cos(np.pi/4)],
                          [-np.sin(np.pi/4), np.sin(np.pi/4)]])
    vecs = np.array([[b/2, a/2], [b/2, -a/2], [-b/2, -a/2], [-b/2, a/2]]).transpose()
    rot_vecs = np.dot(rotation_base, vecs)
    fig, ax = plt.subplots()
    plt.figsize = (8, 6)
    ax.add_patch(mpatches.Polygon(list(rot_vecs.transpose()), fill=False, lw=1.6,  color="red"))
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.yticks(list(range(-a-2, a+2, 1)))
    plt.xticks(list(range(-b-2, b+2, 1)))
    plt.xlim(-b-2, b+2)
    plt.ylim(-a-2, a+2)
    plt.title('Rectangle - %s by %s' % (a, b), fontsize=14)
    plt.grid()
    plt.show()
#a = list(map(int, input().split()))
#draw_rectangle(a[0], a[1])
