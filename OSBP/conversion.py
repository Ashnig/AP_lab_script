#This will be your first step

#this code is specially for converting the fasta file into a csv file 
#so that we can prepare a csv file for our further investigation 
from Bio.SeqIO.FastaIO import SimpleFastaParser
import pandas as pd

#You need to save the download the FASTA file and it should be in the same folder as this python file is

with open('______') as fasta_file: #fill in the blank with the name of the FASTA file with extension, for ex- dibothriocephalus_latus.protein.fa
    u_c = [] 
    seq = []
    for title, sequence in SimpleFastaParser(fasta_file):

        #The First word is ID and 
        u_c.append(title.split(None, 1)[0])  # u_c is the list containing the unique codes
        seq.append(sequence) # seq is the list containing the respective coding sequences

    # In order to create dataframe we made a dictionary which will be then converted into a 
    # dataframe with the help of pandas library   
    dict = {'Unique_code':u_c, 'coding_sequence':seq}
    df = pd.DataFrame(dict)
    #print(df)
    #Now we have dataframe so now we can save this dataframe into a csv file 
    df.to_csv('Output.csv', index=False)#saving the file into the same directory in which this python file is in, and the name of the file is Output_file.csv








    


