import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    u = [polygons[i+1][0]-polygons[i][0], polygons[i+1][1]-polygons[i][1], polygons[i+1][2]-polygons[i][2]]
    v = [polygons[i+2][0]-polygons[i][0], polygons[i+2][1]-polygons[i][1], polygons[i+2][2]-polygons[i][2]]
    cross = [u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]]
    return cross
