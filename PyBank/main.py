import csv, os
from operator import itemgetter

# Open csv file in ..\PyBank\Resources.
bank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Function for calculating sum of profit/losses
def calculate_sum(dict):
    net_total = 0
    for item in dict:
        for key, value in item.items():       
            if key == "Profit/Losses":
                net_total = net_total + int(value)
    
    return(net_total)

# Create list for calculating average change between two periods
def calculate_average(dict):
    list = []
    for item in dict:
        for key, value in item.items():      
            if key == "Profit/Losses":
                list.append(int(value))
    
    new_list = []
    for l in range(1, len(list)):
        new_list.append(list[l] - list[l-1])
    
    return(new_list)

# Create list of tuples for calculating difference and maintaining the correct date
def calculate_difference(dict):
    list = []
    diff_list = []

    # This creates a list of Tuples from the dictionary that I can manipulate and return
    for l in range(len(dict)):
        list.append(tuple([dict[l]['Date'],int(dict[l]['Profit/Losses'])]))

    # This will iterate through each tuple in the list and grab the date (starting with the second element), 
    # then grab the profit/loss and subtract the previous profit/loss from it. It will add the date and the difference to a new tuple that we can then min/max with.
    for l in range(1, len(list)):
        diff_list.append(tuple([list[l][0], (list[l][1]-list[l-1][1])]))
    return(diff_list)

# Open the csv file in the Resources folder
with open(bank_csv, 'r', newline='') as bank_data:
    csv_reader = csv.DictReader(bank_data, delimiter=",")

    # Put data into dict
    bank_dict = [row for row in csv_reader]       
    
    # Count Months
    month_count = len(bank_dict)

    # Calculate Sum of Transactions
    total = calculate_sum(bank_dict)

    # Calculate the average change in profit/loss between two periods
    average = sum(calculate_average(bank_dict)) / len(calculate_average(bank_dict))

    # Calculate Greatest Increase - Had to use item getter to min/max on the appropriate values.
    # https://docs.python.org/3/library/operator.html#operator.itemgetter
    max_date = max(calculate_difference(bank_dict), key=itemgetter(1))[0]
    max_diff = max(calculate_difference(bank_dict), key=itemgetter(1))[1]

    # Calculate Greatest Decrease
    min_date = min(calculate_difference(bank_dict), key=itemgetter(1))[0]
    min_diff = min(calculate_difference(bank_dict), key=itemgetter(1))[1]

with open("PyBank\\Analysis\\results.txt", "w", newline='') as output:

    # Write to TXT file
    output.write(f"""
    Financial Analysis \n ---------------------------- \n 
    Total Months: {month_count}
    Profit/Losses = ${total:,}
    Average Change = ${average:,.2f}
    Greatest Increase in Profits: {max_date} ${max_diff:,}
    Greatest Decrease in Profits: {min_date} ${min_diff:,}""")
    
    # Print output to console
    print(f"""\nFinancial Analysis \n---------------------------- \n 
    Total Months: {month_count}
    Profit/Losses = ${total:,}
    Average Change = ${average:,.2f}
    Greatest Increase in Profits: {max_date} (${max_diff:,})
    Greatest Decrease in Profits: {min_date} (${min_diff:,}""")