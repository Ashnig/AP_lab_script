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

#now we will read the new file which we have generated with the additional details
data = pd.read_csv("_______") #Fill in the blank with the path of the output_file-1, which you have created in this file only


Mol_wt = data["Molecular weight"]

# two empty lists where we will store the sorted values and then finally
# from these lists we will make a dictionary and then from a dictionary,
# we will make a csv file which then will be used in the next file.
u_c = []
filter_seq = []

#filtering the data in a specified molecular weight because 
#FATTY ACID BINDING PROTEINS are generally occur in this region

for i in range(len(unique_code)):
    if Mol_wt[i] >= 12000 and Mol_wt[i] <= 16000:
        filter_seq.append(cds[i])
        u_c.append(unique_code[i])


#print(filter_data)
#print(len(filter_data))
#print(len(u_c))

dictionary = {"Unique code": u_c, "sorted amino acids": filter_seq}

df = pd.DataFrame(dictionary)

#this is the final file which we will use for our 
#further investigation of FATTY ACID BINDING PROTEINS
df.to_csv("Output_file-2.csv", index = False) #saving the final output with the desired name you want 
