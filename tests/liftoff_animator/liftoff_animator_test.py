#!/usr/bin/python3

##
# @file rocket_animator.py
# @author Paul Daum
##

import sys, os
sys.path.append(os.path.realpath('../../'))
sys.path.append(os.getcwd())

from models.liftoff_model.liftoff_model import liftoff_model
from models.liftoff_model.liftoff_trajectory import liftoff_trajectory
from models.liftoff_model.liftoff_animator import liftoff_animator

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np


# Load a trajectory
spacecraft = liftoff_model()
trajectory = liftoff_trajectory(T=600.0, N=100)
trajectory.fromXML('trajectory.xml')

trajectory.us[1,:] = np.pi/4 * np.ones((1,100))

# Create an animator
animator = liftoff_animator(trajectory=trajectory)

# Run the animator
animator.run(10)

'''
fig = plt.figure()
ax = fig.add_subplot(111)

body = patches.Rectangle(
    xy = (-1,-1),
    width = 2,
    height = 2,
    fill = True
)
ax.add_patch(body)

plt.show()'''