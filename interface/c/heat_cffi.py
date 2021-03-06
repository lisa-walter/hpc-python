import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from _evolve import ffi, lib

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'


def iterate(field, field0, a, dx, dy, timesteps, image_interval):
    """Run fixed number of time steps of heat equation"""

    dx2 = dx**2
    dy2 = dy**2

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    dt = dx2*dy2 / ( 2*a*(dx2+dy2) )

    field_ptr = ffi.cast("double *", ffi.from_buffer(field))
    field0_ptr = ffi.cast("double *", ffi.from_buffer(field0))
    nx, ny = field.shape

    for m in range(1, timesteps+1):
        lib.evolve(field_ptr, field0_ptr, nx, ny, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)

def init_fields(filename):
    # Read the initial temperature field from file
    field = np.loadtxt(filename)
    field0 = field.copy() # Array for field of previous time step
    return field, field0

def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))


