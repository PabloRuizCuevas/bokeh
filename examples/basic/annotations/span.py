import time
from datetime import datetime as dt

from bokeh.models import Span
from bokeh.plotting import figure, show
from bokeh.sampledata.daylight import daylight_warsaw_2013

p = figure(x_axis_type="datetime", y_axis_type="datetime")
p.title.text = "2013 Sunrise and Sunset times in Warsaw"
p.yaxis.axis_label = 'Time of Day'

p.line(daylight_warsaw_2013.Date, daylight_warsaw_2013.Sunset,
       line_color='#0072B2', line_dash='solid', line_width=2,
       legend_label="Sunset")
p.line(daylight_warsaw_2013.Date, daylight_warsaw_2013.Sunrise,
       line_color='#0072B2', line_dash='dotted', line_width=2,
       legend_label="Sunrise")

start_date = time.mktime(dt(2013, 3, 31, 2, 0, 0).timetuple())*1000
daylight_savings_start = Span(location=start_date,
                              dimension='height', line_color='#009E73',
                              line_dash='dashed', line_width=3)
p.add_layout(daylight_savings_start)

end_date = time.mktime(dt(2013, 10, 27, 3, 0, 0).timetuple())*1000
daylight_savings_end = Span(location=end_date,
                            dimension='height', line_color='#F0E442',
                            line_dash='dashed', line_width=3)
p.add_layout(daylight_savings_end)

show(p)
