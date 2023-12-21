import random

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = sc.parallelize(range(0, 1000000000)) \
             .filter(inside).count()
print("Pi is roughly %f" % (4.0 * count / 1000000000))

