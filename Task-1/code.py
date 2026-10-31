
# Progressive Electricity Billing System

bills = []

# Electricity slab rates
slabs = [
    (50, 1.45),
    (100, 2.80),
    (100, 3.70),
    (100, 4.80),
    (float('inf'), 6.60)
]

# Function to calculate electricity charges
def calculate_energy_charge(units):

    energy_charge = 0
    remaining = units

    for limit, rate in slabs:
        consumed = min(remaining, limit)
        energy_charge += consumed * rate
        remaining -= consumed

        if remaining <= 0:
            break

    return energy_charge


# Get number of months
n = int(input("Enter number of months: "))

for i in range(n):

    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units: "))

    if units < 0:
        print("Invalid units! Enter positive units.")
        continue

    # Calculate bill components
    energy = calculate_energy_charge(units)

    fixed_charge = 50
    surcharge = energy * 0.05

    if units <= 100:
        rebate = 20
    else:
        rebate = 0

    total = energy + fixed_charge + surcharge - rebate

    # Compare with previous month
    status = "Normal"
    increase = 0

    if len(bills) > 0:
        previous_bill = bills[-1]["total"]

        if previous_bill > 0:
            increase = ((total - previous_bill)
                        / previous_bill) * 100

            if increase > 25:
                status = "Unusual Increase"

    # Store monthly details
    bill = {
        "month": month,
        "units": units,
        "energy": energy,
        "fixed": fixed_charge,
        "surcharge": surcharge,
        "rebate": rebate,
        "total": total,
        "status": status,
        "increase": increase
    }

    bills.append(bill)

    # Display individual bill
    print("\n----- ELECTRICITY BILL -----")
    print("Month:", month)
    print("Units Consumed:", units)
    print("Energy Charges: Rs.", round(energy, 2))
    print("Fixed Charges: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", rebate)
    print("Total Bill: Rs.", round(total, 2))
    print("Status:", status)


# Monthly bill comparison
print("\n========== MONTHLY BILL COMPARISON ==========")

print("{:<12} {:<12} {:<15} {}".format(
    "Month", "Units", "Bill (Rs.)", "Status"
))

for bill in bills:
    print("{:<12} {:<12} {:<15.2f} {}".format(
        bill["month"],
        bill["units"],
        bill["total"],
        bill["status"]
    ))

print("\n========== ANALYSIS ==========")

for bill in bills:
    if bill["status"] == "Unusual Increase":
        print("Warning:", bill["month"],
              "has an unusual increase of",
              round(bill["increase"], 2), "%")

print("\nBilling calculation completed!")

