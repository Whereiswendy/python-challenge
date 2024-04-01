### PYPOLL CODE
###-----------------------------------------
## Read the CSV File
##------------------------------------------
# 1. Import relevant modules

# Import os module - allows for creation of file paths across operating systems
import os

# Import csv module - allows for reading of CSV files
import csv

# Define the path to the contacts.csv file. This uses `os.path.join` to ensure the path is constructed correctly across different operating systems.
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# 2. Reading *.csv

# Open the CSV file using a context manager to ensure proper handling of the file resource.

pypoll_data=[]

with open(csvpath) as csvfile:
    
    # Initialise the CSV reader specifying the delimiter as ',', which creates an object to iterate over lines in the given CSV file.
    csvreader=csv.reader(csvfile, delimiter=",")

    # Skip the header row when analysing data (but only if there is a header row)
    csv_header=next(csvreader)

    # Read each row of data after the header - check output in terminal
    for row in csvreader:
        pypoll_data.append(row)

##------------------------------------------
## Calculate the Analysis Metrics
##------------------------------------------

# Function to analyse the data
def voting_analysis(pypoll_data):

# Calculate the total number of votes cast
    total_votes=len(pypoll_data)

# Provide a complete list of candidates who received votes
    # Use a set to store unique candidate names. 
    # Note: set used ensure uniqueness; sets cannot hold duplicate elements
    candidates_set=set()

    # Use a dictionary to store the vote count for each candidate
    candidate_votes={}

    # Iterate through the data in column [2]/'Column C' to populate the set with unique candidate names
    # and to count the votes for each candidate
    for row in pypoll_data:
        # Create variable for candidate name
        candidate_name=row[2]
        # Add candidate name to set of candidates (looks for unique values because it is adding to a set)
        candidates_set.add(candidate_name)
         # If the candidate is already in the candidate_votes dictionary, increment their count
        # Otherwise, add them to the dictionary with a count of 1
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

    # Convert the set (unordered) to a list (ordered) if you need an ordered collection, such as for alphabetical listing
    candidates=list(candidates_set)

    # Sort the list alphabetically
    candidates.sort()

    # Initialise a variable to keep track of the winner's vote count and name
    candidate_details=""
    max_votes = 0
    winner=""

    # Iterate over the candidate votes to calculate the percentage and print their results
    for candidate in candidates:
        
        # Provide the total number of votes each candidate won
        votes = candidate_votes[candidate]
        
        # Provide the percentage of votes each candidate won and print them
        percentage = (votes / total_votes) * 100
        candidate_details += f'{candidate}: {percentage:.3f}% ({votes})\n'
        
        # Check votes of current candidate against the current max_votes
        if votes>max_votes:
            max_votes=votes
            winner=candidate
        
    # Prepare the summary of the analysis
    summary=(
        f'Election Results\n'
        f'-----------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'-----------------------------\n'
        f'{candidate_details}'
        f'-----------------------------\n'
        f'Winner: {winner}\n'
        f'-----------------------------'
    )

    # Print the summary to the terminal
    print(summary)

    # Specify the file name to write the *.txt file to
    output_path=os.path.join("..","Analysis","voting_analysis.txt")

    # Open the file name to write the *.txt file to
    with open(output_path,"w") as textfile:
        textfile.write(summary)
      
##------------------------------------------
## Call the Function (voting_analysis())
##------------------------------------------

# Call the Function (voting_analysis())
voting_analysis(pypoll_data)

##------------------------------------------
## Print to Terminal - in the function (voting_analysis())
##------------------------------------------
# Run in terminal using python pypoll.py prompt - screen capture take and stored in ~\python-challenge\PyPoll\Analysis

##------------------------------------------
## Write to a Text File  - in the function (voting_analysis())
##------------------------------------------