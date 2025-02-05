''' A demonstration of the Band annotation

.. bokeh-example-metadata::
    :apis: bokeh.models.Band, bokeh.models.ColumnDataSource
    :refs: :ref:`ug_basic_annotations_bands`
    :keywords: band

'''
import numpy as np
import pandas as pd

from bokeh.models import Band, ColumnDataSource
from bokeh.plotting import figure, show

# Create some random data
x = np.random.random(2500) * 140 +20
y = np.random.normal(size=2500) * 2 + 6 * np.log(x)

df = pd.DataFrame(data=dict(x=x, y=y)).sort_values(by="x")

df2 = df.y.rolling(window=300).agg({"y_mean": np.mean, "y_std": np.std})

df = pd.concat([df, df2], axis=1)
df["lower"] = df.y_mean - df.y_std
df["upper"] = df.y_mean + df.y_std

source = ColumnDataSource(df.reset_index())

p = figure(tools="", toolbar_location=None, x_range=(40, 160))
p.title.text = "Rolling Standard Deviation"
p.xgrid[0].grid_line_color=None
p.ygrid[0].grid_line_alpha=0.5

p.scatter(x="x", y="y", marker="dot", size=10, alpha=0.4, source=source)

p.line("x", "y_mean", line_dash=(10, 7), line_width=2, source=source)

band = Band(base="x", lower="lower", upper="upper", source=source,
            fill_alpha=0.3, fill_color="gray", line_color="black")
p.add_layout(band)

show(p)
