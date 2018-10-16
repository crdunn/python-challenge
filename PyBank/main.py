import os
import csv

budgetData = os.path.join("Resources", "budget_data.csv")

with open(budgetData) as csvData:
    reader = csv.reader(csvData)
    # Skips the header
    header = next(reader)
    # Counts the total number of months
    monthCounter = 0
    # Tracks the total Profit
    totalProfitLoss = 0

    countProfitLoss = []

    # Will store the current row at the end of each iteration of the loop
    prevProfitLoss = int(next(reader)[1])

    # Initial values of largest and smallest
    greatestProfitLoss = 0
    leastProfitLoss = 1000000

    # Loops over the rows in the csv
    for row in reader:
        # Iterates the month counter
        monthCounter += 1

        # Sums the profits and losses
        totalProfitLoss += int(row[1])

        # Gets the difference between the current profit/Loss and the previous month's one
        profitLossDiff = int(row[1]) - prevProfitLoss

        countProfitLoss.append(profitLossDiff)

        # COnditional to set the greatest and least difference in profits
        if (profitLossDiff > greatestProfitLoss):
            greatestProfitLoss = profitLossDiff
            greatestMonth = row[0]
        elif(profitLossDiff < leastProfitLoss):
            leastProfitLoss = profitLossDiff
            leastMonth = row[0]

        # Stores the previous month's profit/loss for use in the next iteration of the loop
        prevProfitLoss = int(row[1])

avgProfitLoss = round(sum(countProfitLoss)/len(countProfitLoss))

print(header)
print(f"Number of months: \n~~~~ {monthCounter}")
print(f"Total Profit: \n~~~~ ${totalProfitLoss}")
print(f"Average Profit: \n~~~~ ${avgProfitLoss}")
print(f"Greatest Profit increase: \n~~~~ ${greatestProfitLoss} in {greatestMonth}")
print(f"Least Profit increase: \n~~~~ ${leastProfitLoss} in {leastMonth}")