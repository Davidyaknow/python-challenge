import datetime

f = open("budget_data.csv", "r")
f.readline()

net_Total_Amount = 0
first_pl = None
last_pl = None
total_Months = 0
average_Change = 0
previous_val = 0
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

    net_Total_Amount = net_Total_Amount + pl
    difference = pl - previous_val
    # print(date, pl, difference)

    if difference > greatest_Increase:
        greatest_Increase = difference 
        greatest_Increase_Month = date

    if difference < greatest_Decrease:
        greatest_Decrease = difference 
        greatest_Decrease_Month = date
    
    if first_date == None or date_obj < first_date:
        first_date = date_obj
        first_pl = pl
        
    if last_date == None or date_obj > last_date:
        last_date = date_obj
        last_pl = pl


    previous_val = pl
        

total_Months = last_date.month - first_date.month + 12 * (last_date.year - first_date.year) + 1 

average_Change = (last_pl - first_pl) / (total_Months - 1)

def print_result(f_out=None):
    print("Financial Analysis", file=f_out)
    print("----------------------------", file=f_out)
    print(f"Total Months: {total_Months}", file=f_out)
    print(f"Total: ${net_Total_Amount}", file=f_out)
    print(f"Average  Change: ${round(average_Change, 2)}", file=f_out)
    print(f"Greatest Increase in Profits: {greatest_Increase_Month} (${greatest_Increase})", file=f_out)
    print(f"Greatest Decrease in Profits: {greatest_Decrease_Month} (${greatest_Decrease})", file=f_out)

print_result()

f_out = open("budget_data_output.txt", "w")
print_result(f_out) 
