
# Water Distribution Fairness Analysis

areas = ["Area A", "Area B", "Area C"]
days = 3

# Daily water demand (in litres)
demand = [
    [1000, 1200, 1100],
    [1500, 1400, 1600],
    [1000, 1000, 1200]
]

# Actual water supply (in litres)
supply = [
    [900, 1000, 950],
    [1000, 1100, 1200],
    [950, 900, 1100]
]

shortage_percentages = []

print("WATER DISTRIBUTION FAIRNESS ANALYSIS")
print("-" * 65)

for i in range(len(areas)):
    total_demand = sum(demand[i])
    total_supply = sum(supply[i])

    shortage = max(0, total_demand - total_supply)

    shortage_percentage = (
        shortage / total_demand
    ) * 100 if total_demand > 0 else 0

    shortage_percentages.append(shortage_percentage)

    print("\nArea:", areas[i])
    print("Total Demand:", total_demand, "litres")
    print("Total Supply:", total_supply, "litres")
    print("Shortage:", shortage, "litres")
    print("Shortage Percentage:",
          round(shortage_percentage, 2), "%")

# Identify the most underserved area
index = shortage_percentages.index(
    max(shortage_percentages)
)

print("\n" + "-" * 65)
print("MOST UNDERSERVED AREA:", areas[index])
print("Highest Shortage Percentage:",
      round(shortage_percentages[index], 2), "%")

print("\nAnalysis Completed.")

