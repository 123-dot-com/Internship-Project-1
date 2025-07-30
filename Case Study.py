import pandas as pd

named_list = []
def extract (version, row):
    if (version == 1):
        named_list.append()


#Merging the files:
csv_files = ['Bangalore.csv', 'Chennai.csv', 'Mumbai.csv', 'Delhi.csv', 'Hyderabad.csv']
merged_files = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index = True)

#Printing row and column count:
rows = len(merged_files)
columns = len(merged_files.T)
print ("Row count = ",rows)
print ("Column count = ",columns)

#Printing duplicate row and column counts:
duplicated_rows = merged_files.duplicated().sum()
duplicated_columns = merged_files.T.duplicated().sum()
print ("Duplicate row count = ",duplicated_rows)
print ("Duplicate column count = ",duplicated_columns)

#Dropping duplicate rows and columns:
merged_files = merged_files.drop_duplicates()
merged_files = merged_files.T.drop_duplicates().T

#Printing updated row and column counts
rows = len(merged_files)
columns = len(merged_files.T)
print ("Row count after duplicate removal = ",rows)
print ("Column count after duplicate removal = ",columns)

#Updating column headings:
merged_files = merged_files.set_axis(['S. No.','Car Title','Car Model','Gear_type','Driven_km','Car Owner','Fuel_type','Reg_place','Car price per month','Price','Car Location','Location'], axis = 1)

#Adding new variables:
merged_files['Car_brand'] = merged_files['Car Title'].str.split(' ').str[1]
merged_files['Model_year'] = merged_files['Car Title'].str.split(' ').str[0]
merged_files['Ownership_count'] = merged_files['Car Owner'].str[0:1]
merged_files['EMI_Rs'] = merged_files['Car price per month'].str.replace(",", "")
merged_files['EMI_Rs'] = merged_files['EMI_Rs'].str.replace("/month", "")

#Dropping old variables:
merged_files.drop(['Car Title', 'Car Owner', 'Car price per month'], axis = 1, inplace = True)

#Storing output in new csv file:
merged_files.to_csv('output.csv')