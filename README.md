# AHEAD_Task
The task from AHEAD tech


### Task1 (Watch detail from -> AHEAD.py & AHEAD.ipynb) :
- [AHEAD.py ](https://github.com/wcsodw1/AHEAD_Task/blob/main/AHEAD.py)
- [AHEAD.ipynb](https://github.com/wcsodw1/AHEAD_Task/blob/main/AHEAD.ipynb)

- TASK: There are a group of patients who were diagnosed either COVID-19 positive (sick) or negative (healthy). Each FCS file represents the specimen collected from one patient. Build an automatic predictor using a ML model of your selection, the labels provided in the “EU_label.xlsx” as ground truth, and marker-channels with “use” = 1 in “”EU_marker_channel_mapping.xlsx” as ” as data features

#### Step : 
- Concat FCSdata with FeatureName
- Data Analyze
- Concat dataframe with label 
- Label Encoding
- Training model by using all the patients data
- evaluate the performance of the model
![alt text](./data/result.png)

### Bonus Question :  (Watch detail from -> Bonus Question.ipynb)
- Below are plots of selected cell surface biomarkers of blood cell samples. Researchers are interested in picking out cells marked in yellow (accupying a high-density chunk at the bottom-right) for further analysis. How would you suggest a method to automatically identify these cells?
![Alt text](./data/bonus_result.png) 