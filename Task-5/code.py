
# Multi-Branch Expense Matrix Analysis

# Monthly expenses of different branches
# Categories: Rent, Salaries, Electricity, Transport

branches = {
    "Vijayawada": [15000, 40000, 5000, 3000],
    "Hyderabad": [20000, 50000, 7000, 5000],
    "Chennai": [18000, 45000, 6000, 4000]
}

categories = ["Rent", "Salaries", "Electricity", "Transport"]

branch_totals = {}
category_totals = [0] * len(categories)

overall_total = 0

# Calculate branch and category totals
for branch, expenses in branches.items():

    total = sum(expenses)
    average = total / len(expenses)

    branch_totals[branch] = total
    overall_total += total

    for i in range(len(expenses)):
        category_totals[i] += expenses[i]

    print("\nBranch:", branch)
    print("Total Expense:", total)
    print("Average Expense:", average)

# Find highest spending branch
highest_branch = max(branch_totals, key=branch_totals.get)

# Find highest spending category
highest_category_index = category_totals.index(max(category_totals))

# Calculate overall average
overall_average = overall_total / (
    len(branches) * len(categories)
)

# Display final results
print("\n----- OVERALL ANALYSIS -----")

print("Overall Expense:", overall_total)
print("Overall Average:", overall_average)

print("\nCategory-wise Expenses:")

for i in range(len(categories)):
    print(categories[i], ":", category_totals[i])

print("\nHighest Spending Branch:", highest_branch)
print("Highest Branch Expense:", branch_totals[highest_branch])

print("Highest Spending Category:",
      categories[highest_category_index])

print("Highest Category Expense:",
      category_totals[highest_category_index])

