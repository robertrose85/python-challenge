import csv, os

bank_csv = os.path.join("..", "PyBank\Resources", "budget_data.csv")

# Function for calculating sum of transactions
def calculate_sum(dict):
    net_total = 0
    for item in dict:
        for key, value in item.items():       
            if key == "Profit/Losses":
                net_total = net_total + int(value)
    
    return(net_total)

# Create list of differences between consecutive periods
def calculate_difference(dict):
    list = []
    for item in bank_dict:
        for key, value in item.items():      
            if key == "Profit/Losses":
                list.append(int(value))
    
    new_list = []
    for l in range(1, len(list)):
        new_list.append(list[l] - list[l-1])
    
    return(new_list)

with open(bank_csv, 'r', newline='') as bank_data:
    csv_reader = csv.DictReader(bank_data, delimiter=",")

    # Put data into dict
    bank_dict = [row for row in csv_reader]       
    
    # Count Months
    month_count = len(bank_dict)

    # Calculate Sum of Transactions
    total = calculate_sum(bank_dict)

    # Calculate the average change
    average = sum(calculate_difference(bank_dict)) / len(calculate_difference(bank_dict))

    # Calculate Greatest Increase
    greatest_increase = max(calculate_difference(bank_dict))

    # Calculate Greatest Decrease
    greatest_decrease = min(calculate_difference(bank_dict))

with open("results.txt", "w", newline='') as output:

    # Write to TXT file
    output.write(f"""\n\nFinancial Analysis \n ---------------------------- \n 
    Total Months: {month_count}
    Profit/Losses = ${total:,}
    Average Change = ${average:,.2f}
    Greatest Increase in Profits = ${greatest_increase:,}
    Greatest Decrease in Profits = ${greatest_decrease:,}""")
    
    # Print output to console
    print(f"""\n\nFinancial Analysis \n ---------------------------- \n 
    Total Months: {month_count}
    Profit/Losses = ${total:,}
    Average Change = ${average:,.2f}
    Greatest Increase in Profits = ${greatest_increase:,}
    Greatest Decrease in Profits = ${greatest_decrease:,}""")