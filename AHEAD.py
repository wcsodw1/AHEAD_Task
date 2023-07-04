
# python AHEAD.py

print("Hi AHEAD")

import FlowCal

# Load the FCS file

filename = "../raw_fcs/flowrepo_covid_EU_002_flow_001/export_COVID19 samples 23_04_20_ST3_COVID19_HC_005 ST3 230420_016_Live_cells.fcs"
fcs_file = FlowCal.io.FCSData(filename)
fcs_file_sub = fcs_file[:100]
# View the data
print(fcs_file)
print(fcs_file.shape)
print(fcs_file_sub.shape)
print(fcs_file.channels)

print("Done")