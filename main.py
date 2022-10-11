import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Geo, Bar
from pyecharts.datasets import register_url
import ssl

from pyecharts.globals import ChartType, ThemeType

ssl._create_default_https_context = ssl._create_unverified_context

register_url("https://echarts-maps.github.io/echarts-countries-js/")

if __name__ == '__main__':
    url = "https://coviddata.github.io/coviddata/v1/regions/cases.csv"
    file_url = "C:\\Users\\Administrator.000\\Desktop\\cost_sum_by_state01.csv"
    data = pd.read_csv(file_url, encoding='utf-8', usecols=['state', 'cost_total'])

    data_list = data.dropna().values.tolist()[:-6]
    low, high = min([x[1] for x in data_list]), max([x[1] for x in data_list])

    map = Map(init_opts=opts.InitOpts(width="1600px", height='900px', theme=ThemeType.ROMA))
    c = (
        map
            .add("medical cost",
                 data_list,
                 maptype="美国",
                 zoom=1,
                 is_map_symbol_show=False,
                 itemstyle_opts={
                     "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                     "emphasis": {
                         "areaColor": "rgba(255,255,255, 0.5)",
                     },
                 },
                 )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=high, min_=low),
            #                  title_opts=opts.TitleOpts(
            #                      title="Medical Payment Heatmap in US")
            #                  )
            .set_global_opts(title_opts=opts.TitleOpts(title='Medical Payment Heatmap in US', subtitle='From:google'),
                             visualmap_opts=opts.VisualMapOpts(max_=100000000, is_piecewise=True,
                                                               # pieces=[{"max": 100000, "min": 1, "label": "1-100k",
                                                               #          "color": "#ccffff"},
                                                               #         {"max": 1000000, "min": 100000,
                                                               #          "label": "100k-1m",
                                                               #          "color": "#66ffcc"},
                                                               #         {"max": 5000000, "min": 1000000,
                                                               #          "label": "1m-5m",
                                                               #          "color": "#ffcc00"},
                                                               #         {"max": 50000000, "min": 5000000,
                                                               #          "label": "5m-50m",
                                                               #          "color": "#ff9966"},
                                                               #         {"max": 150000000, "min": 50000000,
                                                               #          "label": "50m-1.5b",
                                                               #          "color": "#ff3300"},
                                                               #         {"max": 1000000000, "min": 150000000,
                                                               #          "label": ">=1.5b",
                                                               #          "color": "#990000"}
                                                               #         ]
                                                               ))
            .render()

    )
