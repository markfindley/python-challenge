#!/usr/bin/env python
# coding: utf-8

# In[8]:


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
import sys

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
    
    csvfile = csv.reader(budgetfile, delimiter=",")
    firstrow = 1
    header = next(csvfile)
    
    for row in csvfile:

        number_of_months = number_of_months + 1
        profits_losses_this_month = int(row[1])
        total_profits_losses = total_profits_losses + profits_losses_this_month
        
        if firstrow != 1:
            profits_losses_month_difference = profits_losses_this_month - profits_losses_last_month
            total_profits_losses_over_all_months = total_profits_losses_over_all_months + profits_losses_month_difference
            
        if profits_losses_this_month > greatest_profit_month:
            greatest_profit_month = profits_losses_month_difference
            greatest_profit_month_name = str(row[0])
            
        if profits_losses_this_month < greatest_loss_month:
            greatest_loss_month = profits_losses_month_difference 
            greatest_loss_month_name = str(row[0])

        if firstrow == 1:
            firstrow = 0 
            
        profits_losses_last_month = profits_losses_this_month
        
    average_change = total_profits_losses_over_all_months / (number_of_months-1)
    
    print(f"Total Months: {number_of_months}")
    print(f"Total: ${total_profits_losses}")
    print("Average Change: $"+ "%.2f" % average_change)
    print(f"Greatest Increase in Profits: {greatest_profit_month_name} (${greatest_profit_month})")
    print(f"Greatest Decrease in Profits: {greatest_loss_month_name} (${greatest_loss_month})")
    
if os.path.exists("log.txt"):
    os.remove("log.txt")   

text_file = open("log.txt", "w")
text_file.write(f"Total Months: {number_of_months}" + '\n')
text_file.write(f"Total: ${total_profits_losses}" + '\n')
text_file.write("Average Change: $"+ "%.2f" % average_change + '\n')
text_file.write(f"Greatest Increase in Profits: {greatest_profit_month_name} (${greatest_profit_month})" + '\n')
text_file.write(f"Greatest Decrease in Profits: {greatest_loss_month_name} (${greatest_loss_month})" + '\n')
text_file.close()
   


# In[ ]:





# In[ ]:




