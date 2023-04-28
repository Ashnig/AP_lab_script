#this will be your second step

import pandas as pd

data = pd.read_csv("________") #fill the blank with the path of the csv file which you have created by running conversion.py file, Output_file.csv
cds = data["sorted amino acids"]
unique_code = data["Unique code"]

#For calculating length
length = []
for i in range(len(cds)):
    length.append(cds.str.len()[i])

#putting the length of each cds in another column
data["Length"] = length

#For calculating molecular weight for each coding sequence 
#and that will be the major factor by which we will differentiate the coding sequences

Mol_wt = []
for i in range(len(length)):
    Mol_wt.append(length[i]*110)


#putting the molecular weight of each cds in another column
data["Molecular weight"] = Mol_wt

#for getting a csv file with the additional details we can use this csv file for other purposes also 

data.to_csv("Output_file_1.csv", index = False) #saving the file into the same directory in which this python file is in, and the name of the file is Output_file_1.csv


