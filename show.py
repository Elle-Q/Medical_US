import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Geo, Bar, Timeline, Grid
from pyecharts.commons.utils import JsCode
from pyecharts.datasets import register_url
import ssl

from pyecharts.globals import ChartType, ThemeType

ssl._create_default_https_context = ssl._create_unverified_context

register_url("https://echarts-maps.github.io/echarts-countries-js/")

data = [
    {
        "year": 2018,
        "data": [
            {"state": 'AS', "value": [12.08, 1, 'AS']},
            {"state": 'Georgia', "value": [44941521.82, 215938, 'Georgia']},
            {"state": 'Pennsylvania', "value": [88538917.68, 263361, 'Pennsylvania']},
            {"state": 'Rhode Island', "value": [6999366.63, 18157, 'Rhode Island']},
            {"state": 'Delaware', "value": [2478933.87, 19366, 'Delaware']},
            {"state": 'Michigan', "value": [67279396.4, 171118, 'Michigan']},
            {"state": 'District of Columbia', "value": [14488078.4, 18885, 'District of Columbia']},
            {"state": 'North Carolina', "value": [55425830.82, 170412, 'North Carolina']},
            {"state": 'Puerto Rico', "value": [3466918.22, 32179, 'Puerto Rico']},
            {"state": 'Texas', "value": [313123714.7, 552998, 'Texas']},
            {"state": 'Idaho', "value": [4118142.4, 16801, 'Idaho']},
            {"state": 'Indiana', "value": [24678049.67, 124483, 'Indiana']},
            {"state": 'Washington', "value": [36945415.28, 53760, 'Washington']},
            {"state": 'Wyoming', "value": [1132344.21, 3309, 'Wyoming']},
            {"state": 'Arkansas', "value": [5986890.04, 59586, 'Arkansas']},
            {"state": 'Mississippi', "value": [7915112.59, 68081, 'Mississippi']},
            {"state": 'Missouri', "value": [51683507.43, 124956, 'Missouri']},
            {"state": 'Nebraska', "value": [8956557.69, 30987, 'Nebraska']},
            {"state": 'Guam', "value": [1270.76, 30, 'Guam']},
            {"state": 'Montana', "value": [1026750.92, 5913, 'Montana']},
            {"state": 'New Mexico', "value": [2807839.57, 15544, 'New Mexico']},
            {"state": 'Ohio', "value": [67663948.34, 221292, 'Ohio']},
            {"state": 'South Dakota', "value": [3953307.09, 8438, 'South Dakota']},
            {"state": 'Colorado', "value": [55421960.08, 71112, 'Colorado']},
            {"state": 'Alaska', "value": [761856.66, 5205, 'Alaska']},
            {"state": 'Nevada', "value": [12744754.69, 50545, 'Nevada']},
            {"state": 'Maine', "value": [2110524.29, 7146, 'Maine']},
            {"state": 'New York', "value": [137772607.2, 415138, 'New York']},
            {"state": 'Alabama', "value": [18363934.9, 139474, 'Alabama']},
            {"state": 'Arizona', "value": [36995452.29, 127652, 'Arizona']},
            {"state": 'New Jersey', "value": [333123714.57, 233610, 'New Jersey']},
            {"state": 'Tennessee', "value": [47391018.11, 161694, 'Tennessee']},
            {"state": 'Vermont', "value": [880533.5, 981, 'Vermont']},
            {"state": 'Utah', "value": [20536620.42, 41527, 'Utah']},
            {"state": 'Florida', "value": [139845190.3, 498190, 'Florida']},
            {"state": 'Oregon', "value": [13056594.99, 26781, 'Oregon']},
            {"state": 'Virginia', "value": [64264537.12, 141959, 'Virginia']},
            {"state": 'Kentucky', "value": [18756899.93, 105591, 'Kentucky']},
            {"state": 'Massachusetts', "value": [163878572.9, 75909, 'Massachusetts']},
            {"state": 'New Hampshire', "value": [4263117.93, 10513, 'New Hampshire']},
            {"state": 'Wisconsin', "value": [18663577.29, 32527, 'Wisconsin']},
            {"state": 'Hawaii', "value": [4157746.24, 28269, 'Hawaii']},
            {"state": 'Iowa', "value": [10225940.27, 27446, 'Iowa']},
            {"state": 'Armed Forces', "value": [30491.36, 163, 'Armed Forces']},
            {"state": 'California', "value": [303123714.8, 613010, 'California']},
            {"state": 'Minnesota', "value": [35094943.25, 23600, 'Minnesota']},
            {"state": 'Oklahoma', "value": [9853951.33, 78954, 'Oklahoma']},
            {"state": 'South Carolina', "value": [16438643.05, 108229, 'South Carolina']},
            {"state": 'West Virginia', "value": [5354488.66, 35873, 'West Virginia']},
            {"state": 'Illinois', "value": [70998450.33, 204340, 'Illinois']},
            {"state": 'Kansas', "value": [20530453.41, 49613, 'Kansas']},
            {"state": 'North Dakota', "value": [2252747.2, 5250, 'North Dakota']},
            {"state": 'Virgin Islands', "value": [2229.65, 68, 'Virgin Islands']},
            {"state": 'Armed Forces Pacific', "value": [9756.75, 116, 'Armed Forces Pacific']},
            {"state": 'Maryland', "value": [43758671.97, 113207, 'Maryland']},
            {"state": 'Connecticut', "value": [17495869.82, 75299, 'Connecticut']},
            {"state": 'Louisiana', "value": [16630171.84, 118318, 'Louisiana']}
        ],
    },
    {
        "year": 2019,
        "data": [
            {"state": 'AS', "value": [12.08, 1, 'AS']},
            {"state": 'Georgia', "value": [44941521.82, 215938, 'Georgia']},
            {"state": 'Pennsylvania', "value": [88538917.68, 263361, 'Pennsylvania']},
            {"state": 'Rhode Island', "value": [6999366.63, 18157, 'Rhode Island']},
            {"state": 'Delaware', "value": [2478933.87, 19366, 'Delaware']},
            {"state": 'Michigan', "value": [67279396.4, 171118, 'Michigan']},
            {"state": 'District of Columbia', "value": [14488078.4, 18885, 'District of Columbia']},
            {"state": 'North Carolina', "value": [55425830.82, 170412, 'North Carolina']},
            {"state": 'Puerto Rico', "value": [3466918.22, 32179, 'Puerto Rico']},
            {"state": 'Texas', "value": [117108234.7, 552998, 'Texas']},
            {"state": 'Idaho', "value": [343123714.4, 16801, 'Idaho']},
            {"state": 'Indiana', "value": [24678049.67, 124483, 'Indiana']},
            {"state": 'Washington', "value": [36945415.28, 53760, 'Washington']},
            {"state": 'Wyoming', "value": [1132344.21, 3309, 'Wyoming']},
            {"state": 'Arkansas', "value": [5986890.04, 59586, 'Arkansas']},
            {"state": 'Mississippi', "value": [7915112.59, 68081, 'Mississippi']},
            {"state": 'Missouri', "value": [51683507.43, 124956, 'Missouri']},
            {"state": 'Nebraska', "value": [8956557.69, 30987, 'Nebraska']},
            {"state": 'Guam', "value": [1270.76, 30, 'Guam']},
            {"state": 'Montana', "value": [1026750.92, 5913, 'Montana']},
            {"state": 'New Mexico', "value": [2807839.57, 15544, 'New Mexico']},
            {"state": 'Ohio', "value": [67663948.34, 221292, 'Ohio']},
            {"state": 'South Dakota', "value": [3953307.09, 8438, 'South Dakota']},
            {"state": 'Colorado', "value": [55421960.08, 71112, 'Colorado']},
            {"state": 'Alaska', "value": [761856.66, 5205, 'Alaska']},
            {"state": 'Nevada', "value": [12744754.69, 50545, 'Nevada']},
            {"state": 'Maine', "value": [2110524.29, 7146, 'Maine']},
            {"state": 'New York', "value": [137772607.2, 415138, 'New York']},
            {"state": 'Alabama', "value": [18363934.9, 139474, 'Alabama']},
            {"state": 'Arizona', "value": [36995452.29, 127652, 'Arizona']},
            {"state": 'New Jersey', "value": [37909873.57, 233610, 'New Jersey']},
            {"state": 'Tennessee', "value": [47391018.11, 161694, 'Tennessee']},
            {"state": 'Vermont', "value": [880533.5, 981, 'Vermont']},
            {"state": 'Utah', "value": [20536620.42, 41527, 'Utah']},
            {"state": 'Florida', "value": [283123714.3, 498190, 'Florida']},
            {"state": 'Oregon', "value": [13056594.99, 26781, 'Oregon']},
            {"state": 'Virginia', "value": [64264537.12, 141959, 'Virginia']},
            {"state": 'Kentucky', "value": [18756899.93, 105591, 'Kentucky']},
            {"state": 'Massachusetts', "value": [163878572.9, 75909, 'Massachusetts']},
            {"state": 'New Hampshire', "value": [4263117.93, 10513, 'New Hampshire']},
            {"state": 'Wisconsin', "value": [18663577.29, 32527, 'Wisconsin']},
            {"state": 'Hawaii', "value": [4157746.24, 28269, 'Hawaii']},
            {"state": 'Iowa', "value": [10225940.27, 27446, 'Iowa']},
            {"state": 'Armed Forces', "value": [30491.36, 163, 'Armed Forces']},
            {"state": 'California', "value": [323123714.8, 613010, 'California']},
            {"state": 'Minnesota', "value": [35094943.25, 23600, 'Minnesota']},
            {"state": 'Oklahoma', "value": [9853951.33, 78954, 'Oklahoma']},
            {"state": 'South Carolina', "value": [16438643.05, 108229, 'South Carolina']},
            {"state": 'West Virginia', "value": [5354488.66, 35873, 'West Virginia']},
            {"state": 'Illinois', "value": [70998450.33, 204340, 'Illinois']},
            {"state": 'Kansas', "value": [20530453.41, 49613, 'Kansas']},
            {"state": 'North Dakota', "value": [2252747.2, 5250, 'North Dakota']},
            {"state": 'Virgin Islands', "value": [2229.65, 68, 'Virgin Islands']},
            {"state": 'Armed Forces Pacific', "value": [9756.75, 116, 'Armed Forces Pacific']},
            {"state": 'Maryland', "value": [43758671.97, 113207, 'Maryland']},
            {"state": 'Connecticut', "value": [17495869.82, 75299, 'Connecticut']},
            {"state": 'Louisiana', "value": [16630171.84, 118318, 'Louisiana']}
        ],
    },
    {
        "year": 2020,
        "data": [
            {"state": 'AS', "value": [12.08, 1, 'AS']},
            {"state": 'Georgia', "value": [44941521.82, 215938, 'Georgia']},
            {"state": 'Pennsylvania', "value": [88538917.68, 263361, 'Pennsylvania']},
            {"state": 'Rhode Island', "value": [6999366.63, 18157, 'Rhode Island']},
            {"state": 'Delaware', "value": [2478933.87, 19366, 'Delaware']},
            {"state": 'Michigan', "value": [67279396.4, 171118, 'Michigan']},
            {"state": 'District of Columbia', "value": [14488078.4, 18885, 'District of Columbia']},
            {"state": 'North Carolina', "value": [55425830.82, 170412, 'North Carolina']},
            {"state": 'Puerto Rico', "value": [3466918.22, 32179, 'Puerto Rico']},
            {"state": 'Texas', "value": [117108234.7, 552998, 'Texas']},
            {"state": 'Idaho', "value": [4118142.4, 16801, 'Idaho']},
            {"state": 'Indiana', "value": [24678049.67, 124483, 'Indiana']},
            {"state": 'Washington', "value": [36945415.28, 53760, 'Washington']},
            {"state": 'Wyoming', "value": [1132344.21, 3309, 'Wyoming']},
            {"state": 'Arkansas', "value": [5986890.04, 59586, 'Arkansas']},
            {"state": 'Mississippi', "value": [7915112.59, 68081, 'Mississippi']},
            {"state": 'Missouri', "value": [51683507.43, 124956, 'Missouri']},
            {"state": 'Nebraska', "value": [8956557.69, 30987, 'Nebraska']},
            {"state": 'Guam', "value": [1270.76, 30, 'Guam']},
            {"state": 'Montana', "value": [1026750.92, 5913, 'Montana']},
            {"state": 'New Mexico', "value": [2807839.57, 15544, 'New Mexico']},
            {"state": 'Ohio', "value": [67663948.34, 221292, 'Ohio']},
            {"state": 'South Dakota', "value": [3953307.09, 8438, 'South Dakota']},
            {"state": 'Colorado', "value": [55421960.08, 71112, 'Colorado']},
            {"state": 'Alaska', "value": [761856.66, 5205, 'Alaska']},
            {"state": 'Nevada', "value": [12744754.69, 50545, 'Nevada']},
            {"state": 'Maine', "value": [2110524.29, 7146, 'Maine']},
            {"state": 'New York', "value": [137772607.2, 415138, 'New York']},
            {"state": 'Alabama', "value": [18363934.9, 139474, 'Alabama']},
            {"state": 'Arizona', "value": [36995452.29, 127652, 'Arizona']},
            {"state": 'New Jersey', "value": [37909873.57, 233610, 'New Jersey']},
            {"state": 'Tennessee', "value": [47391018.11, 161694, 'Tennessee']},
            {"state": 'Vermont', "value": [880533.5, 981, 'Vermont']},
            {"state": 'Utah', "value": [20536620.42, 41527, 'Utah']},
            {"state": 'Florida', "value": [139845190.3, 498190, 'Florida']},
            {"state": 'Oregon', "value": [13056594.99, 26781, 'Oregon']},
            {"state": 'Virginia', "value": [64264537.12, 141959, 'Virginia']},
            {"state": 'Kentucky', "value": [18756899.93, 105591, 'Kentucky']},
            {"state": 'Massachusetts', "value": [163878572.9, 75909, 'Massachusetts']},
            {"state": 'New Hampshire', "value": [4263117.93, 10513, 'New Hampshire']},
            {"state": 'Wisconsin', "value": [18663577.29, 32527, 'Wisconsin']},
            {"state": 'Hawaii', "value": [4157746.24, 28269, 'Hawaii']},
            {"state": 'Iowa', "value": [10225940.27, 27446, 'Iowa']},
            {"state": 'Armed Forces', "value": [30491.36, 163, 'Armed Forces']},
            {"state": 'California', "value": [433123714.8, 613010, 'California']},
            {"state": 'Minnesota', "value": [35094943.25, 23600, 'Minnesota']},
            {"state": 'Oklahoma', "value": [9853951.33, 78954, 'Oklahoma']},
            {"state": 'South Carolina', "value": [16438643.05, 108229, 'South Carolina']},
            {"state": 'West Virginia', "value": [5354488.66, 35873, 'West Virginia']},
            {"state": 'Illinois', "value": [70998450.33, 204340, 'Illinois']},
            {"state": 'Kansas', "value": [20530453.41, 49613, 'Kansas']},
            {"state": 'North Dakota', "value": [2252747.2, 5250, 'North Dakota']},
            {"state": 'Virgin Islands', "value": [2229.65, 68, 'Virgin Islands']},
            {"state": 'Armed Forces Pacific', "value": [9756.75, 116, 'Armed Forces Pacific']},
            {"state": 'Maryland', "value": [43758671.97, 113207, 'Maryland']},
            {"state": 'Connecticut', "value": [17495869.82, 75299, 'Connecticut']},
            {"state": 'Louisiana', "value": [16630171.84, 118318, 'Louisiana']}
        ],
    },
    {
        "year": 2021,
        "data": [
            {"state": 'AS', "value": [12.08, 1, 'AS']},
            {"state": 'Georgia', "value": [44941521.82, 215938, 'Georgia']},
            {"state": 'Pennsylvania', "value": [88538917.68, 263361, 'Pennsylvania']},
            {"state": 'Rhode Island', "value": [6999366.63, 18157, 'Rhode Island']},
            {"state": 'Delaware', "value": [2478933.87, 19366, 'Delaware']},
            {"state": 'Michigan', "value": [617279396.4, 171118, 'Michigan']},
            {"state": 'District of Columbia', "value": [14488078.4, 18885, 'District of Columbia']},
            {"state": 'North Carolina', "value": [55425830.82, 170412, 'North Carolina']},
            {"state": 'Puerto Rico', "value": [3466918.22, 32179, 'Puerto Rico']},
            {"state": 'Texas', "value": [117108234.7, 552998, 'Texas']},
            {"state": 'Idaho', "value": [4118142.4, 16801, 'Idaho']},
            {"state": 'Indiana', "value": [24678049.67, 124483, 'Indiana']},
            {"state": 'Washington', "value": [36945415.28, 53760, 'Washington']},
            {"state": 'Wyoming', "value": [1132344.21, 3309, 'Wyoming']},
            {"state": 'Arkansas', "value": [5986890.04, 59586, 'Arkansas']},
            {"state": 'Mississippi', "value": [7915112.59, 68081, 'Mississippi']},
            {"state": 'Missouri', "value": [51683507.43, 124956, 'Missouri']},
            {"state": 'Nebraska', "value": [89536557.69, 30987, 'Nebraska']},
            {"state": 'Guam', "value": [1270.76, 30, 'Guam']},
            {"state": 'Montana', "value": [1026750.92, 5913, 'Montana']},
            {"state": 'New Mexico', "value": [2807839.57, 15544, 'New Mexico']},
            {"state": 'Ohio', "value": [67663948.34, 221292, 'Ohio']},
            {"state": 'South Dakota', "value": [3953307.09, 8438, 'South Dakota']},
            {"state": 'Colorado', "value": [55421960.08, 71112, 'Colorado']},
            {"state": 'Alaska', "value": [403123714.66, 5205, 'Alaska']},
            {"state": 'Nevada', "value": [12744754.69, 50545, 'Nevada']},
            {"state": 'Maine', "value": [2110524.29, 7146, 'Maine']},
            {"state": 'New York', "value": [137772607.2, 415138, 'New York']},
            {"state": 'Alabama', "value": [185363934.9, 139474, 'Alabama']},
            {"state": 'Arizona', "value": [36995452.29, 127652, 'Arizona']},
            {"state": 'New Jersey', "value": [433123714.57, 233610, 'New Jersey']},
            {"state": 'Tennessee', "value": [47391018.11, 161694, 'Tennessee']},
            {"state": 'Vermont', "value": [880533.5, 981, 'Vermont']},
            {"state": 'Utah', "value": [20536620.42, 41527, 'Utah']},
            {"state": 'Florida', "value": [139845190.3, 498190, 'Florida']},
            {"state": 'Oregon', "value": [13056594.99, 26781, 'Oregon']},
            {"state": 'Virginia', "value": [64264537.12, 141959, 'Virginia']},
            {"state": 'Kentucky', "value": [18756899.93, 105591, 'Kentucky']},
            {"state": 'Massachusetts', "value": [163878572.9, 75909, 'Massachusetts']},
            {"state": 'New Hampshire', "value": [4263117.93, 10513, 'New Hampshire']},
            {"state": 'Wisconsin', "value": [18663577.29, 32527, 'Wisconsin']},
            {"state": 'Hawaii', "value": [4157746.24, 28269, 'Hawaii']},
            {"state": 'Iowa', "value": [10225940.27, 27446, 'Iowa']},
            {"state": 'Armed Forces', "value": [30491.36, 163, 'Armed Forces']},
            {"state": 'California', "value": [2331523714.8, 613010, 'California']},
            {"state": 'Minnesota', "value": [35094943.25, 23600, 'Minnesota']},
            {"state": 'Oklahoma', "value": [9853951.33, 78954, 'Oklahoma']},
            {"state": 'South Carolina', "value": [16438643.05, 108229, 'South Carolina']},
            {"state": 'West Virginia', "value": [5354488.66, 35873, 'West Virginia']},
            {"state": 'Illinois', "value": [70998450.33, 204340, 'Illinois']},
            {"state": 'Kansas', "value": [20530453.41, 49613, 'Kansas']},
            {"state": 'North Dakota', "value": [483123714.2, 5250, 'North Dakota']},
            {"state": 'Virgin Islands', "value": [2229.65, 68, 'Virgin Islands']},
            {"state": 'Armed Forces Pacific', "value": [9756.75, 116, 'Armed Forces Pacific']},
            {"state": 'Maryland', "value": [43758671.97, 113207, 'Maryland']},
            {"state": 'Connecticut', "value": [17495869.82, 75299, 'Connecticut']},
            {"state": 'Louisiana', "value": [166360171.84, 118318, 'Louisiana']}
        ],
    },
    {
        "year": 2022,
        "data": [
            {"state": 'AS', "value": [12.08, 1, 'AS']},
            {"state": 'Georgia', "value": [44941521.82, 215938, 'Georgia']},
            {"state": 'Pennsylvania', "value": [88538917.68, 263361, 'Pennsylvania']},
            {"state": 'Rhode Island', "value": [6999366.63, 18157, 'Rhode Island']},
            {"state": 'Delaware', "value": [2478933.87, 19366, 'Delaware']},
            {"state": 'Michigan', "value": [67279396.4, 171118, 'Michigan']},
            {"state": 'District of Columbia', "value": [14488078.4, 18885, 'District of Columbia']},
            {"state": 'North Carolina', "value": [55425830.82, 170412, 'North Carolina']},
            {"state": 'Puerto Rico', "value": [3466918.22, 32179, 'Puerto Rico']},
            {"state": 'Texas', "value": [117108234.7, 552998, 'Texas']},
            {"state": 'Idaho', "value": [4118142.4, 16801, 'Idaho']},
            {"state": 'Indiana', "value": [24678049.67, 124483, 'Indiana']},
            {"state": 'Washington', "value": [36945415.28, 53760, 'Washington']},
            {"state": 'Wyoming', "value": [1132344.21, 3309, 'Wyoming']},
            {"state": 'Arkansas', "value": [5986890.04, 59586, 'Arkansas']},
            {"state": 'Mississippi', "value": [7915112.59, 68081, 'Mississippi']},
            {"state": 'Missouri', "value": [51683507.43, 124956, 'Missouri']},
            {"state": 'Nebraska', "value": [895446557.69, 30987, 'Nebraska']},
            {"state": 'Guam', "value": [1270.76, 30, 'Guam']},
            {"state": 'Montana', "value": [1026750.92, 5913, 'Montana']},
            {"state": 'New Mexico', "value": [2807839.57, 15544, 'New Mexico']},
            {"state": 'Ohio', "value": [67663948.34, 221292, 'Ohio']},
            {"state": 'South Dakota', "value": [395300307.09, 8438, 'South Dakota']},
            {"state": 'Colorado', "value": [55421960.08, 71112, 'Colorado']},
            {"state": 'Alaska', "value": [761856.66, 5205, 'Alaska']},
            {"state": 'Nevada', "value": [12744754.69, 50545, 'Nevada']},
            {"state": 'Maine', "value": [2110524.29, 7146, 'Maine']},
            {"state": 'New York', "value": [1377772607.2, 415138, 'New York']},
            {"state": 'Alabama', "value": [18363934.9, 139474, 'Alabama']},
            {"state": 'Arizona', "value": [36995452.29, 127652, 'Arizona']},
            {"state": 'New Jersey', "value": [387909873.57, 233610, 'New Jersey']},
            {"state": 'Tennessee', "value": [47391018.11, 161694, 'Tennessee']},
            {"state": 'Vermont', "value": [880533.5, 981, 'Vermont']},
            {"state": 'Utah', "value": [20536620.42, 41527, 'Utah']},
            {"state": 'Florida', "value": [13945190.3, 498190, 'Florida']},
            {"state": 'Oregon', "value": [13056594.99, 26781, 'Oregon']},
            {"state": 'Virginia', "value": [64264537.12, 141959, 'Virginia']},
            {"state": 'Kentucky', "value": [18756899.93, 105591, 'Kentucky']},
            {"state": 'Massachusetts', "value": [163878572.9, 75909, 'Massachusetts']},
            {"state": 'New Hampshire', "value": [4263117.93, 10513, 'New Hampshire']},
            {"state": 'Wisconsin', "value": [18663577.29, 32527, 'Wisconsin']},
            {"state": 'Hawaii', "value": [4157746.24, 28269, 'Hawaii']},
            {"state": 'Iowa', "value": [10225400.27, 27446, 'Iowa']},
            {"state": 'Armed Forces', "value": [30491.36, 163, 'Armed Forces']},
            {"state": 'California', "value": [833123714.8, 613010, 'California']},
            {"state": 'Minnesota', "value": [35094943.25, 23600, 'Minnesota']},
            {"state": 'Oklahoma', "value": [9853951.33, 78954, 'Oklahoma']},
            {"state": 'South Carolina', "value": [16438643.05, 108229, 'South Carolina']},
            {"state": 'West Virginia', "value": [5354488.66, 35873, 'West Virginia']},
            {"state": 'Illinois', "value": [70998450.33, 204340, 'Illinois']},
            {"state": 'Kansas', "value": [205304503.41, 49613, 'Kansas']},
            {"state": 'North Dakota', "value": [2252747.2, 5250, 'North Dakota']},
            {"state": 'Virgin Islands', "value": [2229.65, 68, 'Virgin Islands']},
            {"state": 'Armed Forces Pacific', "value": [9756.75, 116, 'Armed Forces Pacific']},
            {"state": 'Maryland', "value": [43758671.97, 113207, 'Maryland']},
            {"state": 'Connecticut', "value": [174795869.82, 75299, 'Connecticut']},
            {"state": 'Louisiana', "value": [16630171.84, 118318, 'Louisiana']}
        ],
    },
]


def get_year_chart(year: int):
    # ------------------ cost ------------------
    map_cost_data = [[[x["state"], [x["value"][0], x["value"][2]]] for x in d["data"]] for d in data
                if d["year"] == year][0]
    min_cost, max_cost = (
        min([d[1][0] for d in map_cost_data]),
        max([d[1][0] for d in map_cost_data]),
    )

    # ------------------ population ------------------
    map_pop_data = [[[x["state"], [x["value"][1], x["value"][2]]] for x in d["data"]] for d in data
                    if d["year"] == year][0]
    min_pop, max_pop = (
        min([d[1][0] for d in map_pop_data]),
        max([d[1][0] for d in map_pop_data]),
    )

    map_chart = (
        Map()
            .add(
            series_name="cost",
            maptype="美国",
            data_pair=map_cost_data,
            label_opts=opts.LabelOpts(is_show=True),
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
            .add(
            series_name="population",
            is_selected=False,
            maptype="美国",
            data_pair=map_pop_data,
            label_opts=opts.LabelOpts(is_show=True),
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Medical Cost In USA ",
                subtitle="From 2018~2022",
                pos_left="center",
                pos_top="3%",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[1] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=[
                opts.VisualMapOpts(
                    series_index=0,
                    is_calculable=True,
                    dimension=0,
                    pos_left="10",
                    pos_top="0",
                    range_text=["High", "Low"],
                    # range_color=["lightskyblue", "yellow", "orangered"],
                    textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                    min_=min_cost,
                    max_=max_cost,
                ),
                opts.VisualMapOpts(
                    is_show=False,
                    series_index=1,
                    is_calculable=True,
                    dimension=0,
                    pos_left="10",
                    pos_top="0",
                    range_text=["High", "Low"],
                    # range_color=["lightskyblue", "yellow", "orangered"],
                    textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                    min_=min_pop,
                    max_=max_pop,
                ),
            ]
        )
    )

    grid_chart = (
        Grid()
        #     .add(
        #     bar,
        #     grid_opts=opts.GridOpts(
        #         pos_left="10", pos_right="45%", pos_top="30%", pos_bottom="5"
        #     ))
            .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


# Draw timeline
year_list = [2018, 2019, 2020, 2021, 2022]
timeline = Timeline(
    init_opts=opts.InitOpts(width="1850px", height="930px", theme=ThemeType.DARK)
)
for y in year_list:
    g = get_year_chart(year=y)
    timeline.add(g, time_point=str(y))

timeline.add_schema(
    orient="vertical",
    is_inverse=True,
    play_interval=5000,
    pos_left="null",
    pos_right="5",
    pos_top="20",
    pos_bottom="20",
    width="50",
    label_opts=opts.LabelOpts(is_show=True, color="#fff"),
)

timeline.render("us_medical.html")
