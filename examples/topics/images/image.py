import numpy as np

from bokeh.plotting import figure, show

x = np.linspace(0, 10, 250)
y = np.linspace(0, 10, 250)
xx, yy = np.meshgrid(x, y)
d = np.sin(xx)*np.cos(yy)

p = figure(width=400, height=400)
p.x_range.range_padding = p.y_range.range_padding = 0

p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="Sunset11", level="image")
p.grid.grid_line_width = 0.5

show(p)
