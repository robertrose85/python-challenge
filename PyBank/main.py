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

    # Calculate the average change
    average = sum(calculate_difference(bank_dict)) / len(calculate_difference(bank_dict))

with open("results.txt", "w", newline='') as output:
    output.write(f"""\n\nFinancial Analysis \n ---------------------------- \n 
    Total Months: {month_count}
    Profit/Losses = ${calculate_sum(bank_dict):,}
    Average Change = ${average:,.2f}
    Greatest Increase in Profits = ${max(calculate_difference(bank_dict)):,}
    Greatest Decrease in Profits = ${min(calculate_difference(bank_dict)):,}""")
    
    print(f"""\n\nFinancial Analysis \n ---------------------------- \n 
    Total Months: {month_count}
    Profit/Losses = ${calculate_sum(bank_dict):,}
    Average Change = ${average:,.2f}
    Greatest Increase in Profits = ${max(calculate_difference(bank_dict)):,}
    Greatest Decrease in Profits = ${min(calculate_difference(bank_dict)):,}""")
    
    
    
    
    # print(f"""\n\nFinancial Analysis \n ---------------------------- \n
    #     Total Months: {month_count}\n
    #     Profit/Losses = ${calculate_sum(bank_dict):,}\n""")

    # output.write(f'Total Months: {month_count}')
    # print(f'Total Months: {month_count}')

    # output.write(f'Profit/Losses = ${calculate_sum(bank_dict):,}')
    # print(f'Profit/Losses = ${calculate_sum(bank_dict):,}')

    # output.write(f'Average Change = ${average:,.2f}')
    # print(f'Average Change = ${average:,.2f}')

    # # Calculate and display the greatest increase in profit over two periods
    # print(f'Greatest Increase in Profits = ${max(calculate_difference(bank_dict)):,}')

    # # Calculate and display the greatest decrease in profit over two periods
    # print(f'Greatest Decrease in Profits = ${min(calculate_difference(bank_dict)):,}')


    



