import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

with open('10.txt') as file:
    data = file.read().splitlines()
positions = []
velocities = []
for line in data:
    pos = tuple(map(int, line[10:24].split(',')))
    vel = tuple(map(int, line[36:-1].split(',')))
    positions.append(pos)
    velocities.append(vel)
np_positions = np.array(positions).T
np_velocities = np.array(velocities).T

# Flip Y so the text is up the right way
np_positions[1]*=-1
np_velocities[1]*=-1

init_t = 10905
fig, ax = plt.subplots()
sp, = ax.plot(*(np_positions+np_velocities*init_t), marker='o', ls='')
ax.set_xbound(120,190)
ax.set_ybound(-215,-180)
plt.subplots_adjust(left=0.25, bottom=0.25)

axtime = plt.axes([0.25, 0.1, 0.65, 0.03])
time_slider = Slider(
    ax=axtime,
    label='Time [s]',
    valmin=10900,
    valmax=11000,
    valinit=init_t,
    valstep=1,
)

def update(t):
    sp.set_data(*(np_positions+np_velocities*t))
    fig.canvas.draw_idle()

time_slider.on_changed(update)

plt.show()
