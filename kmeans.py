import random


xrange = 10
yrange = 10
def create_obj(xrange, yrange):
    object = []
    len = 0
    while len < 4:
        len = random.randint(0, 10)
    print(len)
    for i in range(0, len):
        coord = [random.randint(-xrange, xrange), random.randint(-yrange, yrange)]
        object.append(coord)
    return object

obj = create_obj(xrange, yrange)

for coord in obj:
    print(coord)

