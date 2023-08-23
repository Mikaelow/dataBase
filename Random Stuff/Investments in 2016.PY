# Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:
# have the same tiv_2015 value as one or more other policyholders, and
# are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
# Round tiv_2016 to two decimal places.
# The result format is in the following example.

import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['policzone_lat'] = insurance.groupby('lat')['lat'].transform('count')
    insurance['policzone_tiv'] = insurance.groupby('tiv_2015')['tiv_2015'].transform('count')
    unique_location = insurance[(insurance['policzone_lat'] == 1) & (insurance['policzone_tiv']>1)]
    # unique_location = unique_location.groupby('tiv_2015')['tiv_2016'].sum().reset_index()
    sum_2016 = unique_location['tiv_2016'].sum().round(2)
    # return pd.DataFrame([sum_2016],columns=['tiv_2016'])
    return unique_location



data = [[1,224.17,952.73,32.4,20.2],
[2,224.17,900.66,52.4,32.7],
[3,824.61,645.13,72.4,45.2],
[4,424.32,323.66,12.4,7.7],
[5,424.32,282.9,12.4,7.7],
[6,625.05,243.53,52.5,32.8],
[7,424.32,968.94,72.5,45.3],
[8,624.46,714.13,12.5,7.8],
[9,425.49,463.85,32.5,20.3],
[10,624.46,776.85,12.4,7.7],
[11,624.46,692.71,72.5,45.3],
[12,225.93,933,12.5,7.8],
[13,824.61,786.86,32.6,20.3],
[14,824.61,935.34,52.6,32.8],
[15,826.37,516.1,12.4,7.7],
[16,824.61,374.5,12.6,7.9],
[17,824.61,924.19,32.6,20.4],
[18,626.81,897.47,52.6,32.9],
[19,224.76,714.79,72.6,45.4],
[20,224.76,681.53,12.4,7.7],
[21,427.25,263.27,32.7,20.4],
[22,224.76,671.8,52.7,32.9],
[23,424.9,769.18,72.7,45.4]]
Insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype(
    {'pid':'Int64', 'tiv_2015':'Float64', 'tiv_2016':'Float64', 'lat':'Float64', 'lon':'Float64'})

print(find_investments(Insurance))