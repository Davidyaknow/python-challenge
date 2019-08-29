import datetime

f = open("budget_data.txt", "r")
f.readline()

net_Total_Amount = 0
total_Months = 0
average_Change = 0
greatest_Increase = 0
greatest_Decrease = 0
greatest_Increase_Month = ""
greatest_Decrease_Month = ""
first_date = None
last_date = None

for row in f:
    # print(row, end="")
    x = row.split(",")
    date = x[0]
    date_obj = datetime.datetime.strptime(x[0], "%b-%Y")
    pl = int(x[1])
    print(date, pl)

    net_Total_Amount = net_Total_Amount + pl

    if pl > greatest_Increase:
        greatest_Increase = pl 
        greatest_Increase_Month = date

    if pl < greatest_Decrease:
        greatest_Decrease = pl 
        greatest_Decrease_Month = date
    
    if first_date == None or date_obj < first_date:
        first_date = date_obj
        
    if last_date == None or date_obj > last_date:
        last_date = date_obj
        

total_Months = last_date.month - first_date.month + 12 * (last_date.year - first_date.year) + 1 

average_Change = net_Total_Amount/total_Months

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_Months}")
print(f"Total: ${net_Total_Amount}")
print(f"Average  Change: ${round(average_Change, 2)}")
print(f"Greatest Increase in Profits: {greatest_Increase_Month} (${greatest_Increase})")
print(f"Greatest Decrease in Profits: {greatest_Decrease_Month} (${greatest_Decrease})")