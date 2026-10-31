
# Courier Charge Optimization

print("===================================")
print("     COURIER CHARGE OPTIMIZATION")
print("===================================")

# Input parcel details
weight = float(input("Enter parcel weight (kg): "))

length = float(input("Enter length (cm): "))
width = float(input("Enter width (cm): "))
height = float(input("Enter height (cm): "))

# Calculate volumetric weight
volumetric_weight = (length * width * height) / 5000

# Calculate chargeable weight
chargeable_weight = max(weight, volumetric_weight)

print("\nActual Weight:", weight, "kg")
print("Volumetric Weight:", round(volumetric_weight, 2), "kg")
print("Chargeable Weight:", round(chargeable_weight, 2), "kg")

# Distance zone
print("\nDistance Zones:")
print("1. Local")
print("2. Regional")
print("3. National")

zone = int(input("Select distance zone (1-3): "))

zone_rates = {
    1: 40,
    2: 70,
    3: 100
}

if zone not in zone_rates:
    print("Invalid distance zone!")
    exit()

# Delivery urgency
print("\nDelivery Options:")
print("1. Normal")
print("2. Express")

urgency = int(input("Select urgency (1-2): "))

if urgency not in [1, 2]:
    print("Invalid urgency!")
    exit()

urgent_charge = 50 if urgency == 2 else 0

# Parcel restrictions
print("\nParcel Restrictions:")
print("1. Normal")
print("2. Fragile")
print("3. Liquid")
print("4. Prohibited")

restriction = int(input("Select restriction (1-4): "))

if restriction not in [1, 2, 3, 4]:
    print("Invalid restriction!")
    exit()

if restriction == 4:
    print("\nParcel cannot be delivered!")
    exit()

# Restriction charges
restriction_charge = 30 if restriction == 2 else 20 if restriction == 3 else 0

# Courier service rates per kg
couriers = {
    "Fast Express": 50,
    "Speed Courier": 40,
    "Budget Delivery": 30
}

print("\n========== COURIER COMPARISON ==========")

eligible_services = []

for name, rate in couriers.items():

    # Maximum parcel weight limits
    if name == "Budget Delivery" and restriction == 2:
        print(name, "- Not eligible for fragile parcels")
        continue

    if name == "Speed Courier" and restriction == 3:
        print(name, "- Not eligible for liquid parcels")
        continue

    if chargeable_weight > 20:
        print(name, "- Not eligible (Weight limit exceeded)")
        continue

    # Calculate delivery charge
    base_charge = zone_rates[zone]

    weight_charge = chargeable_weight * rate

    total_charge = (
        base_charge
        + weight_charge
        + urgent_charge
        + restriction_charge
    )

    eligible_services.append((name, total_charge))

    print(name, "- Rs.", round(total_charge, 2))

# Select the cheapest eligible courier
print("\n========== FINAL RESULT ==========")

if eligible_services:

    best = min(eligible_services, key=lambda x: x[1])

    print("Selected Courier:", best[0])
    print("Minimum Delivery Charge: Rs.", round(best[1], 2))

else:
    print("No eligible courier service available.")

print("\nThank you for using our system!")
