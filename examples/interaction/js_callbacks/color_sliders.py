''' An interactive plot of colors. This example demonstrates adding widgets and
``CustomJS`` callbacks that can update a plot.

.. bokeh-example-metadata::
    :apis: bokeh.plotting.figure.rect, bokeh.plotting.figure.text, bokeh.layouts.column, bokeh.layouts.row, bokeh.models.sources.ColumnDataSource, bokeh.models.callbacks.CustomJS, bokeh.models.widgets.sliders.Slider, bokeh.themes.Theme # noqa: E501
    :refs: :ref:`ug_interaction_js_callbacks_customjs`
    :keywords: hover, javascript callback, theme, tooltip

'''
import colorsys

import yaml

from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import curdoc, figure, show
from bokeh.themes import Theme


# for plot 2: create colour spectrum of resolution N and brightness I, return as list of decimal RGB value tuples
def generate_color_range(N, I):
    HSV_tuples = [ (x*1.0/N, 0.5, I) for x in range(N) ]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    for_conversion = []
    for RGB_tuple in RGB_tuples:
        for_conversion.append((int(RGB_tuple[0]*255), int(RGB_tuple[1]*255), int(RGB_tuple[2]*255)))
    hex_colors = [ rgb_to_hex(RGB_tuple) for RGB_tuple in for_conversion ]
    return hex_colors, for_conversion

# convert RGB tuple to hexadecimal code
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

# convert hexadecimal to RGB tuple
def hex_to_dec(hex):
    red = ''.join(hex.strip('#')[0:2])
    green = ''.join(hex.strip('#')[2:4])
    blue = ''.join(hex.strip('#')[4:6])
    return (int(red, 16), int(green, 16), int(blue,16))

# plot 1: create a color block with RGB values adjusted with sliders

# initialise a white block for the first plot
hex_color = rgb_to_hex((255, 255, 255))

# initialise the text color as black. This will be switched to white if the block color gets dark enough
text_color = '#000000'

# create a data source to enable refreshing of fill & text color
source = ColumnDataSource(data=dict(color=[hex_color], text_color=[text_color]))

# create first plot, as a rect() glyph and centered text label, with fill and text color taken from source
p1 = figure(x_range=(-8, 8), y_range=(-4, 4),
            width=600, height=300,
            title='move sliders to change', tools='')

p1.rect(0, 0, width=18, height=10, fill_color='color',
        line_color = 'black', source=source)

p1.text(0, 0, text='color', text_color='text_color',
        alpha=0.6667, text_font_size='48px', text_baseline='middle',
        text_align='center', source=source)

red_slider = Slider(title="R", start=0, end=255, value=255, step=1)
green_slider = Slider(title="G", start=0, end=255, value=255, step=1)
blue_slider = Slider(title="B", start=0, end=255, value=255, step=1)

# the callback function to update the color of the block and associated label text
# NOTE: the JS functions for converting RGB to hex are taken from the excellent answer
# by Tim Down at http://stackoverflow.com/questions/5623838/rgb-to-hex-and-hex-to-rgb
callback = CustomJS(args=dict(source=source, red=red_slider, blue=blue_slider, green=green_slider), code="""
    function componentToHex(c) {
        const hex = c.toString(16)
        return hex.length == 1 ? "0" + hex : hex
    }
    function rgbToHex(r, g, b) {
        return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b)
    }
    function toInt(v) {
       return v | 0
    }
    const color = source.data['color']
    const text_color = source.data['text_color']
    const R = toInt(red.value)
    const G = toInt(green.value)
    const B = toInt(blue.value)
    color[0] = rgbToHex(R, G, B)
    text_color[0] = '#ffffff'
    if ((R > 127) || (G > 127) || (B > 127)) {
        text_color[0] = '#000000'
    }
    source.change.emit()
""")

red_slider.js_on_change('value', callback)
blue_slider.js_on_change('value', callback)
green_slider.js_on_change('value', callback)

# plot 2: create a color spectrum with a hover-over tool to inspect hex codes

brightness = 0.8 # change to have brighter/darker colors
crx = list(range(1,1001)) # the resolution is 1000 colors
cry = [ 5 for i in range(len(crx)) ]
crcolor, crRGBs = generate_color_range(1000,brightness) # produce spectrum

# make data source object to allow information to be displayed by hover tool
crsource = ColumnDataSource(data=dict(x=crx, y=cry, crcolor=crcolor, RGBs=crRGBs))

# create second plot
p2 = figure(x_range=(0,1000), y_range=(0,10),
            width=600, height=150,
            tools='hover', title='hover over color')

color_range1 = p2.rect(x='x', y='y', width=1, height=10,
                       color='crcolor', source=crsource)

# set up hover tool to show color hex code and sample swatch
p2.hover.tooltips = [
    ('color', '$color[hex, rgb, swatch]:crcolor'),
    ('RGB levels', '@RGBs')
]

# theme everything for a cleaner look
curdoc().theme = Theme(json=yaml.load("""
attrs:
    Plot:
        toolbar_location: null
    Grid:
        grid_line_color: null
    Axis:
        axis_line_color: null
        major_label_text_color: null
        major_tick_line_color: null
        minor_tick_line_color: null
""", Loader=yaml.SafeLoader))

layout = row(
    column(red_slider, green_slider, blue_slider),
    column(p1, p2)
)

show(layout)
