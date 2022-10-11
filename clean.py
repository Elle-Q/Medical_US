import os

import numpy as np
import pandas as pd
import dask.dataframe as dd

# ------------------- drop useless columns ----------------------
# file_path = "C:\\Users\\Administrator.000\\Desktop\\PP2020_drop_test.csv"
# drop_usecols=["Recipient_City","Recipient_State","Recipient_Zip_Code","Recipient_Country","Recipient_Province","Total_Amount_of_Payment_USDollars","Date_of_Payment","City_of_Travel","State_of_Travel","Country_of_Travel"]
# to_file = 'C:\\Users\\Administrator.000\\Desktop\\data_new.csv'
# for chunk in pd.read_csv(file_path, chunksize=1000, usecols=drop_usecols):
#     if not os.path.exists(to_file):
#         chunk.to_csv(to_file, mode='a', index=False)
#     else:
#         chunk.to_csv(to_file, mode='a', index=False, header=False)

def f_mi(x):
    d = {}
    d["cost_total"] = x['Total_Amount_of_Payment_USDollars'].sum()
    d["state"] = np.array(x['Recipient_State'])[0]
    d["count"] = x['Recipient_State'].count()
    return pd.Series(d, index=['state', "cost_total", "count"])

# ------------------- do groupby(state) & sum ----------------------
file_path = "C:\\Users\\Administrator.000\\Desktop\\data_new.csv"
to_file = 'C:\\Users\\Administrator.000\\Desktop\\cost_sum_by_state01.csv'
usecols = ["Recipient_State", "Total_Amount_of_Payment_USDollars"]
replace_state_name = {'AE': 'Armed Forces', 'AP': 'Armed Forces Pacific', 'AR': 'Arkansas', 'AZ': 'Arizona',
                      'AL': 'Alabama', 'AK': 'Alaska', 'AZ  ': 'Arizona', 'AR ': 'Arkansas', 'CA': 'California',
                      'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'DC': 'District of Columbia',
                      'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam',
                      'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
                      'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD ': 'Maryland', 'MA': 'Massachusetts',
                      'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
                      'MD': 'Maryland',
                      'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico',
                      'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'CM': 'Northern Mariana Islands',
                      'OH': 'Ohio', 'OK': 'Oklahoma',
                      'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island',
                      'SC': 'South Carolina',
                      'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
                      'VA': 'Virginia', 'VI': 'Virgin Islands', 'WA': 'Washington', 'WV': 'West Virginia',
                      'WI': 'Wisconsin', 'WY': 'Wyoming'}
ddf = dd.read_csv(file_path, blocksize="16MB", usecols=usecols, dtype={'Total_Amount_of_Payment_USDollars': 'float64'})
ddf["Total_Amount_of_Payment_USDollars"] = dd.to_numeric(ddf["Total_Amount_of_Payment_USDollars"], errors="coerce")
ddf = ddf.replace(replace_state_name)
compute = ddf.groupby('Recipient_State').apply(f_mi, meta={"state":"str", "cost_total":"float16", "count":"int"}).compute()
compute.to_csv(to_file, index=False, header={'Recipient_State','Total_Amount_of_Payment_USDollars'})
print(compute)
