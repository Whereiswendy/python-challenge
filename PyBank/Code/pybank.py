### PYBANK CODE
###-----------------------------------------
## Read the CSV File
##------------------------------------------
# 1. Import relevant modules

# Import os module - allows for creation of file paths across operating systems
import os

# Import csv module - allows for reading of CSV files
import csv

# Define the path to the contacts.csv file. This uses `os.path.join` to ensure the path is constructed correctly across different operating systems.
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# 2. Reading *.csv

# Open the CSV file using a context manager to ensure proper handling of the file resource.

pybank_data =[]

with open(csvpath) as csvfile:

    # Initialise the CSV reader specifying the delimiter as ',', which creates an object to iterate over lines in the given CSV file.
    csvreader=csv.reader(csvfile, delimiter=",")

    # Print the csvreader object for debugging purposes
    #print(csvreader)

    # Skip the header row when analysing data (but only if there is a header row)
    csv_header=next(csvreader)
    #print(f'CSV Header: {csv_header}')

    # Read each row of data after the header - check output in terminal
    for row in csvreader:
        pybank_data.append(row)

##------------------------------------------
## Calculate the Analysis Metrics
##------------------------------------------

# Function to sort the data by date

from datetime import datetime

def parse_date(date_string):
    # Parse the date_string from the format "Month-Year" to a datetime object
    # Assumption: year is '20XX'
    return datetime.strptime(date_string, '%b-%y')

# Function to analyse the data
def profit_loss_analysis(pybank_data):
    
    # # First, sort the data by date
    pybank_data.sort(key=lambda row: parse_date(row[0]))

    # Calculate the total number of months included in the dataset (note: this assumes that no months are duplicated)
    total_months=len(pybank_data)

    # Calculate the net total amount of "Profit/Losses" over the entire period
    # Initiate profit_loss total
    total_profit_losses=0
    
    # Iterate through the data to sum the Profit/Losses column [1]
    for row in pybank_data:
        total_profit_losses += int(row[1])
    
    # Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
    # To track the profit/loss of the previous month
    previous_month_profit_loss = None

    # Iterate through the dataset to calculate total profit/losses and changes
    changes=[]
    # Format: [Date, Amount]
    greatest_increase = ["",0]
    greatest_decrease = ["",0]

    for row in pybank_data:
        # Extract the current month's profit/loss
        current_month_profit_loss=int(row[1])

        # Calculate change from previous month if pevious_month_profit_loss is not None
        if previous_month_profit_loss is not None:
            change=current_month_profit_loss-previous_month_profit_loss
            changes.append(change)
            # Determine the greatest increase in profits (date and amount) over the entire period
            # Check if the current change is greater than the greatest increase recorded
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            
            # Determine the greatest decrease in profits (date and amount) over the entire period
            # Check if the current change is less than the greatest decrease recorded
            if change < greatest_decrease[1]:
                greatest_decrease=[row[0],change]

        #Update previous_month_profit_loss for the next iteration
        previous_month_profit_loss=current_month_profit_loss

    # Calculate the average change. Note: Use len(changes) to avoid division by zero.
    average_change = sum(changes) / len(changes) if changes else 0
    
    # Prepare the summary of the analysis
    summary=(
        f'Financial Analysis\n'
        f'-------------------------------\n'
        f'Total Months: {total_months}\n'
        f'Total Profit/Losses: ${total_profit_losses}\n'
        f'Average Change in Profit/Losses: ${average_change:.2f}\n'
        f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n'
        f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n'
    )
    # Print the summary to the terminal
    print(summary)

    # Specify the file name to write the *.txt file to
    output_path=os.path.join("..","Analysis","financial_analysis.txt")

    # Open the file in write mode and write the summary to it
    with open(output_path,'w') as textfile:
        textfile.write(summary)

##------------------------------------------
## Call the Function (profit_loss_analysis())
##------------------------------------------

# Call the function profit_loss_analysis()
profit_loss_analysis(pybank_data)

##------------------------------------------
## Print to Terminal - in the function (profit_loss_analysis())
##------------------------------------------
# Run in terminal using python pybank.py prompt - screen capture take and stored in ~\python-challenge\PyBank\Analysis

##------------------------------------------
## Write to a Text File - in the function (profit_loss_analysis())
##------------------------------------------







