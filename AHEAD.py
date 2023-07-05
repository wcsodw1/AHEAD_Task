
# python AHEAD.py

print("Hi AHEAD")

import FlowCal
import pandas as pd

# Load the FCS file

# filename = "../raw_fcs/flowrepo_covid_EU_002_flow_001/export_COVID19 samples 23_04_20_ST3_COVID19_HC_005 ST3 230420_016_Live_cells.fcs"
# fcs_file = FlowCal.io.FCSData(filename)
# fcs_file_sub = fcs_file[:100]
# # View the data
# print(fcs_file)
# print(fcs_file.shape)
# print(fcs_file_sub.shape)
# print(fcs_file.channels)
# print(type(fcs_file))
#
# # Convert the FCS data to a pandas DataFrame
# data_frame = pd.DataFrame(fcs_file)
#
# # View the first few rows of the DataFrame
# print(data_frame.head())

filename = "../raw_fcs/flowrepo_covid_EU_002_flow_001/export_COVID19 samples 23_04_20_ST3_COVID19_HC_005 ST3 230420_016_Live_cells.fcs"

def concat_FCSdata_FeatureMame(filename):
    # Load the FCS file
    fcs_file = FlowCal.io.FCSData(filename)

    # View and store feature
    tuple_feature = fcs_file.channels
    list_feature = list(tuple_feature)

    # Convert the FCS data to DataFrame
    data_frame = pd.DataFrame(fcs_file)

    # concatenate feature name with FCS data
    data_frame.columns = list_feature
    print(data_frame)

# run program
concat_FCSdata_FeatureMame(filename)
