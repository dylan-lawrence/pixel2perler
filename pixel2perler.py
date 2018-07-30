#convert pixel art to perler colors

from PIL import Image
from operator import itemgetter

from math import sqrt

perler_colors={}
with open("perler_colors.txt","r") as f:
    for line in f:
        line=line.rstrip('\n').split("\t")
        perler_colors[line[0]] = tuple([int(x) for x in line[1].lstrip('"').rstrip('"').split(',')])

im=Image.open("Poké_Ball_summary_IV_Big.png")

for i in range(im.width):
    for j in range(im.height):

        curr=im.getpixel((i,j))

        deltas=[]
        for color in perler_colors:
            rr=perler_colors[color][0]-curr[0]
            rg=perler_colors[color][1]-curr[1]
            rb=perler_colors[color][2]-curr[2]

            deltas.append((color,
                sqrt((rr**2) + (rg**2) + (rb**2))))

        deltas=sorted(deltas,key=itemgetter(1))

        if curr[3] != 0:
            im.putpixel((i,j),perler_colors[deltas[0][0]])

im.show()
