from src.worldLines import *

C = 299792458

# Create an array of time coordinates.
cts = np.linspace(0, 3, 2)*C

# Created worldlines.
worldline = InertialWorldLine(cts, C*0.9)
worldline2 = InertialWorldLine(cts, C*0.5)
worldline3 = InertialWorldLine(cts, 0)

# Animation parameters
frames = 100
Lorentz_interval = C*0.5/frames

fig = plt.figure()
ax = fig.add_subplot()

# Configure initial plot
# Even though this is exaclty the same as in the update function remving it causes issues
ax.plot(cts, cts, linestyle="dotted", color="orange")
ax.plot(-cts, cts, linestyle="dotted", color="orange")
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xlim([-3*C, 3*C])
ax.set_ylim([0, 3*C])

# Redraw the graph fro each frame.
def update(frame):
    # Transform and plot worldlines
    ax.cla()
    worldline.Lotentz_Transform(Lorentz_interval)
    worldline2.Lotentz_Transform(Lorentz_interval)
    worldline3.Lotentz_Transform(Lorentz_interval)
    ax.plot(worldline.xs, worldline.cts)
    ax.plot(worldline2.xs, worldline2.cts)
    ax.plot(worldline3.xs, worldline3.cts)
    print(frame)

    ax.plot(cts, cts, linestyle="dotted", color="orange")
    ax.plot(-cts, cts, linestyle="dotted", color="orange")
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xlim([-3 * C, 3 * C])
    ax.set_ylim([0, 3 * C])
    return plt.plot(worldline.xs, worldline.cts)

ax = fig.add_subplot()
ani = FuncAnimation(fig, update, frames=frames, interval=50)
plt.show()
ani.save('animations/animation.mp4', writer='ffmpeg')