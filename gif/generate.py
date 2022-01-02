# Copyright Austin Arrington, 2022

# Note --> This file uses Samila to generate random images, and then assembles them into GIFs
# using imageio ... change the duration parameter (line 36) to adjust the animation speed 

# Installation Notes 
# download Samila library (https://pythonawesome.com/generative-art-generator-with-python/)
# https://github.com/sepandhaghighi/samila/archive/v0.2.zip
# pip3 install -r requirements.txt
# python3 setup.py install
# pip3 install samila==0.2

import random
import math
import matplotlib.pyplot as plt
from samila import GenerativeImage
from samila import Projection
import imageio

def f1(x,y):
    result = random.uniform(-1,1) * x**2 - math.sin(y**2) + abs(y-x)
    return result

def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

images = []
frames = [1,2,3,4,5,6,7,8,9,10]
for frame in frames:
    g = GenerativeImage(f1,f2)
    g.generate()
    g.plot(color='yellow',bgcolor="black",projection=Projection.POLAR)
    g.seed
    plt.savefig('/Users/Austin.Arrington/Desktop/ML/generated/gen'+str(frame)+'.png', bbox_inches='tight')
    images.append(imageio.imread('/Users/Austin.Arrington/Desktop/ML/generated/gen'+str(frame)+'.png'))

# play with the duration parameter to adjust animation 
imageio.mimsave('/Users/Austin.Arrington/Desktop/ML/generated/movie.gif', images, duration=0.2)
