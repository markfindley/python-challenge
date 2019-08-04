#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Pseudo-code:
    # Open the budget data file.
    # Get the first record to get to the second row.
    # Iterate through all the rows collecting:
        # Count of the number of months in the dataset.
        # Aggregate of the total profits and losses.
        # Aggregate of the difference between each month.
        # Save the largest month difference in profits.
        # Save the largest month difference in losses.  
    # When done iterating:
        # Determine the average of the aggregation of the differences between each month.
        # Print to Jupyter, python/gitbash and a new text file:
            # Total months.
            # Total profits and losses.
            # Average change from month to month.
            # Largest month difference in profits.
            # Largest month difference in losses.
            
import os
import csv

number_of_months = int(0)
total_profits_losses = int(0)
greatest_profit_month = int(0)
greatest_loss_month = int(0)
profits_losses_this_month = int(0)
profits_losses_last_month = int(0)
profits_losses_month_difference = int(0)
total_profits_losses_over_all_months = int(0)

csvpath = os.path.join("..","Resources", "budget_data.csv")

with open(csvpath, newline="") as budgetfile:
    
    # establish the file object
    csvfile = csv.reader(budgetfile, delimiter=",")
    firstrow = 1
    
    # get the first row
    header = next(csvfile)
    
    # iterate through the file
    for row in csvfile:

        number_of_months = number_of_months + 1
        profits_losses_this_month = int(row[1])
        
        # track total profits and losses
        total_profits_losses = total_profits_losses + profits_losses_this_month
        
        # after processing the first row, start tracking differences in profits and losses for each month
        if firstrow != 1:
            profits_losses_month_difference = profits_losses_this_month - profits_losses_last_month
            total_profits_losses_over_all_months = total_profits_losses_over_all_months + profits_losses_month_difference
            
        # track the greatest monthly increase in profits    
        if profits_losses_this_month > greatest_profit_month:
            greatest_profit_month = profits_losses_month_difference
            greatest_profit_month_name = str(row[0])
            
        # track the greatest monthly decrease in profits
        if profits_losses_this_month < greatest_loss_month:
            greatest_loss_month = profits_losses_month_difference 
            greatest_loss_month_name = str(row[0])

        # after processing the first row, set to zero to start processing differences in profits between months
        if firstrow == 1:
            firstrow = 0 
            
        # save for processing against the next month
        profits_losses_last_month = profits_losses_this_month
        
    # get average change in profits and losses over each month for all months
    average_change = total_profits_losses_over_all_months / (number_of_months-1)
    
    # print to Jupyter Notebook
    print(f"Total Months: {number_of_months}")
    print(f"Total: ${total_profits_losses}")
    print("Average Change: $"+ "%.2f" % average_change)
    print(f"Greatest Increase in Profits: {greatest_profit_month_name} (${greatest_profit_month})")
    print(f"Greatest Decrease in Profits: {greatest_loss_month_name} (${greatest_loss_month})")
    
# if the log file exists, delete it    
if os.path.exists("log.txt"):
    os.remove("log.txt")   

# write results to a text file and close the file
text_file = open("log.txt", "w")
text_file.write(f"Total Months: {number_of_months}" + '\n')
text_file.write(f"Total: ${total_profits_losses}" + '\n')
text_file.write("Average Change: $"+ "%.2f" % average_change + '\n')
text_file.write(f"Greatest Increase in Profits: {greatest_profit_month_name} (${greatest_profit_month})" + '\n')
text_file.write(f"Greatest Decrease in Profits: {greatest_loss_month_name} (${greatest_loss_month})" + '\n')
text_file.close()
   


# In[ ]:





# In[ ]:




