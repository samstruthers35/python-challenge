import os
import csv

date = []
profits = []
change = []


bank_csv = os.path.join('Resources', 'budget_data.csv')

with open(bank_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
            date.append(row[0])
            profits.append(int(row[1]))

    for i in range(1,len(profits)):
        change.append(profits[i]-profits[i-1])


total_months = len(date)
total_profits = sum(profits)
average_change = round((sum(change) / len(change)),2)
max_change = max(change) 
min_change = min(change)         

print("Financial Analysis")

print("--------------")

print(f"Total Months : {total_months}")
print(f"Total Profits : ${total_profits}")
print(f"Average Change: ${average_change}")


change_index = change.index
max_date = date[change_index(max_change) + 1]
min_date = date[change_index(min_change) + 1]

print(f"Greatest Increase in Profits : {max_date} : (${max_change})")
print(f"Greatest Decrease in Profits : {min_date} : (${min_change})")

output_file = os.path.join("Resources", "budget_analysis.txt")

with open(output_file, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Months : {total_months}")
    txt_file.write("\n")
    txt_file.write(f"Total Profits : ${total_profits}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: ${average_change}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits : {max_date} : (${max_change})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits : {min_date} : (${min_change})")
    txt_file.write("\n")

