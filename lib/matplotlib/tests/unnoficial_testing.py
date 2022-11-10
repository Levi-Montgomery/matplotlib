from __future__ import division

import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

fig = plt.figure()

# Button 1
ax = fig.add_axes([0.7, 0.05, 0.1, 0.075])
b1 = widgets.Button(ax, 'B1', text_color='b')
b1.on_clicked(lambda event: print('Clicked'))

# Button 2
ax2 = fig.add_axes([0.7, 0.2, 0.1, 0.075])
b2 = widgets.Button(ax2, 'B2', text_color='r')
b2.on_clicked(lambda event: print('Clicked'))

# Button 3
ax3 = fig.add_axes([0.7, 0.4, 0.1, 0.075])
b3 = widgets.Button(ax3, 'B3', text_color='w')
b3.on_clicked(lambda event: print('Clicked'))

# Button 4
ax4 = fig.add_axes([0.7, 0.6, 0.1, 0.075])
b4 = widgets.Button(ax4, 'B4', text_color='g')
b4.on_clicked(lambda event: print('Clicked'))

# Axes testing 1
ax5 = fig.add_axes([0.2, 0.6, 0.1, 0.075])
ax5.set(xlim=(0, 1), ylim=(0, 1),  # s.t. cursor appears from first click.
            navigate=False, facecolor='r',
            xticks=[], yticks=[])
ax5 = fig.add_axes([0, 0, 1, 1])
ax5.axis('off')

# Axes testing 2
ax6 = fig.add_axes([0.2, 0.4, 0.1, 0.075])
ax6.set(xlim=(0, 1), ylim=(0, 1),  # s.t. cursor appears from first click.
            navigate=False, facecolor='r',
            xticks=[], yticks=[])
ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.spines['bottom'].set_visible(False)
ax6.spines['left'].set_visible(False)

# Axes testing 3
def remove_border(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

ax7 = fig.add_axes([0.2, 0.2, 0.1, 0.075])
ax7.set(xlim=(0, 1), ylim=(0, 1),  # s.t. cursor appears from first click.
            navigate=False, facecolor='g',
            xticks=[], yticks=[])
remove_border(ax7)

# Axes testing 4
ax8 = fig.add_axes([0.2, 0.2, 0.1, 0.075])
ax8.set(xlim=(0, 1), ylim=(0, 1),  # s.t. cursor appears from first click.
            navigate=False, facecolor='#FF9999',
            xticks=[], yticks=[])
circle = plt.Circle((0, 0), 1, color='blue')
ax8.add_patch(circle)
remove_border(ax8)

# Axes testing 5
def round_borders(ax, radius=0.25, padding=0.0):
    color = ax.get_facecolor()
    ax.set_facecolor('w')
    ax.add_patch(plt.Rectangle((padding, radius), 1, 1 - 2 * radius, linewidth=0, edgecolor='w', facecolor=color))
    ax.add_patch(plt.Rectangle((radius, padding), 1 - 2 * radius, 1 , linewidth=0, edgecolor='w', facecolor=color))
    ax.add_patch(plt.Circle((radius + padding, radius + padding), radius, color=color))
    ax.add_patch(plt.Circle(( 1 - (radius + padding), 1 - (radius + padding)), radius, color=color))
    ax.add_patch(plt.Circle((1 - (radius + padding), radius + padding), radius, color=color))
    ax.add_patch(plt.Circle((radius + padding, 1 - (radius + padding)), radius, color=color))


ax9 = fig.add_axes([0.2, 0.8, 0.1, 0.1])
ax9.set(xlim=(0, 1), ylim=(0, 1),  # s.t. cursor appears from first click.
            navigate=False, facecolor='blue',
            xticks=[], yticks=[])
remove_border(ax9)
round_borders(ax9)

# Round Button test
ax10 = fig.add_axes([0.4, 0.8, 0.1, 0.075])
remove_border(ax10)
b10 = widgets.Button(ax10, 'Button', color='blue')
b10.round_borders()
b10.on_clicked(lambda event: print('Clicked'))

# Round Button test
ax11 = fig.add_axes([0.4, 0.6, 0.1, 0.075])
remove_border(ax11)
b11 = widgets.Button(ax11, 'Button', color='blue')
b11.round_borders(radius=0.4)
b11.on_clicked(lambda event: print('Clicked'))

# Text Box test
ax12 = fig.add_axes([0.4, 0.4, 0.1, 0.075])
remove_border(ax12)
t1 = widgets.TextBox(ax12, 'Type:', color='lightgray')
t1.round_borders(radius=0.10)

# Slider test
axs = fig.add_axes([0.1, 0.1, 0.5, 0.04])
amp_slider = widgets.Slider(
    ax=axs,
    label="Test",
    valmin=0,
    valmax=10,
    orientation="horizontal",
    track_color='red'
)

plt.show()
