#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv

number_of_total_votes = int(0)

# establish the lists to zip into a dictionary
candidate_list = []
votes = []

csvpath = os.path.join("..","Resources", "election_data.csv")

with open(csvpath, newline="") as electionfile:
    
    # establish the file object
    csvfile = csv.reader(electionfile, delimiter=",")
   
    # get the first row
    header = next(csvfile)

    # create a list of the candidates and give them zero votes
    for row in csvfile:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            votes.append(0)

    # now create a dictionary of the candidates and their vote counts
    candidate_dictionary = dict(zip(candidate_list,votes))

with open(csvpath, newline="") as electionfile2:    

    # establish the file object
    csvfile2 = csv.reader(electionfile2, delimiter=",")
   
    # get the first row
    header = next(csvfile2)
    
    # update the candidates by iterating back through the file
    for row in csvfile2:

        key = row[2]
        if key in candidate_dictionary:
            number_of_total_votes = number_of_total_votes + 1 
            previous_votes = candidate_dictionary.get(key)
            votes = previous_votes + 1
            candidate_dictionary[key] = votes

    # this will get the candidate data
    top_vote_getter_votes = int(0)
    
    print("Election Results")
    print(f"Total Votes:  {number_of_total_votes}")
    for the_key, the_value in candidate_dictionary.items():
        percentage_of_votes = round((the_value/number_of_total_votes)*100)
        print(f"{the_key}: {percentage_of_votes}% ({the_value})")
        if the_value > top_vote_getter_votes:
            top_vote_getter_votes = the_value
            top_vote_getter = the_key
            
    print(f"Winner: {top_vote_getter}")        
    
    # if the log file exists, delete it    
    if os.path.exists("log.txt"):
        os.remove("log.txt")   

    # write results to a text file and close the file
    text_file = open("log.txt", "w")
    text_file.write("Election Results" + '\n')
    text_file.write(f"Total Votes: {number_of_total_votes}" + '\n')
    for the_key, the_value in candidate_dictionary.items():
        percentage_of_votes = round((the_value/number_of_total_votes)*100)
        text_file.write(f"{the_key}: {percentage_of_votes}% ({the_value})" + '\n')
    text_file.write(f"Winner: {top_vote_getter}" + '\n')
    text_file.close()


# In[ ]:




