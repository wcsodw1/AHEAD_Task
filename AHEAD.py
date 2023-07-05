
# python AHEAD.py

print("Hi AHEAD")

import os
import FlowCal
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def concat_FCSdata_FeatureName(filename):
    # Load the FCS file
    fcs_file = FlowCal.io.FCSData(filename)

    # View and store feature
    tuple_feature = fcs_file.channels
    list_feature = list(tuple_feature)

    # Convert the FCS data to DataFrame
    df = pd.DataFrame(fcs_file)

    # concatenate feature name with FCS data
    df.columns = list_feature
    # display(df)

    return df


def df_descripbe(df):
    df_summary = df.describe()
    series_max = df_summary.loc['max']
    series_min = df_summary.loc['min']
    series_mean = df_summary.loc['mean']
    series_std = df_summary.loc['std']

    # convert the Series to a DataFrame
    df_max_column = series_max.to_frame()
    df_min_column = series_min.to_frame()
    df_mean_column = series_mean.to_frame()
    df_std_column = series_std.to_frame()

    # data type from row to column
    df_max = df_max_column.transpose()
    df_min = df_min_column.transpose()
    df_mean = df_mean_column.transpose()
    df_std = df_std_column.transpose()

    return df_max, df_min, df_mean, df_std


count = 0
fcs_list = []
folder_path = '../raw_fcs/'

# read the Excel file into a DataFrame
EU_label = pd.read_excel('EU_label.xlsx')

# create an empty DataFrame to store the results
concatAll_df = pd.DataFrame()

# define the mapping from string labels to integer labels
label_map = {
    'Sick': 1,
    'Healthy': 0,
}

for patientID in EU_label['file_flow_id']:
    path = folder_path + patientID

    # 1.get a list of all the FCS files in the folder
    list_fcs_files = [f for f in os.listdir(path) if f.endswith('.fcs')]
    fcs_files_tail = ', '.join(list_fcs_files)
    fcs_files_Path = path + "/" + fcs_files_tail

    # 2.Data Analyze Each fcs
    df = concat_FCSdata_FeatureName(fcs_files_Path)
    df_max, df_min, df_mean, df_std = df_descripbe(df)

    # 3.Concat with label, filename extract patient ID:
    Patient = path.split('/')[-1]
    label = EU_label['label']

    for ID in (EU_label['file_flow_id']):
        if Patient == ID:
            df_max.insert(0, 'COVID19', label[count])
            df_max.insert(1, "Patient_ID", ID)
            count += 1
            df_max['Label'] = df_max['COVID19'].replace(label_map)

            # concat all the patientID information as a new data
            concatAll_df = concatAll_df.append(df_max)

x = concatAll_df.drop(['Label', 'COVID19', 'Patient_ID'], axis=1)
y = concatAll_df['Label'].to_frame()
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# print the shapes of the training and testing sets
print(f'Training set shape: {X_train.shape}, {y_train.shape}')
print(f'Testing set shape: {X_test.shape}, {y_test.shape}')

# train a decision tree classifier on the training data
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# make predictions on the testing data
y_pred = clf.predict(X_test)

# evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Mean squared error:", mse)
print("R-squared:", r2)
print("The process is Complete")