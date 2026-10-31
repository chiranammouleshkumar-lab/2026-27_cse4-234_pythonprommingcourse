
# Smart Hostel Resource Monitoring System

# Resource rates
ELECTRICITY_RATE = 8
WATER_RATE = 0.05

# Consumption thresholds
ELECTRICITY_LIMIT = 100
WATER_LIMIT = 1000

hostel = {}

# Input number of floors
floors = int(input("Enter number of floors: "))

# Collect room-wise information
for floor in range(1, floors + 1):

    print(f"\n--- Floor {floor} ---")

    rooms = int(input("Enter number of rooms: "))

    hostel[floor] = []

    for room in range(1, rooms + 1):

        print(f"\nRoom {room}")

        electricity = float(
            input("Enter electricity consumption (kWh): ")
        )

        water = float(
            input("Enter water consumption (litres): ")
        )

        # Calculate charges
        electricity_charge = electricity * ELECTRICITY_RATE
        water_charge = water * WATER_RATE

        total_charge = electricity_charge + water_charge

        # Check threshold violations
        alerts = []

        if electricity > ELECTRICITY_LIMIT:
            alerts.append("High Electricity")

        if water > WATER_LIMIT:
            alerts.append("High Water")

        if not alerts:
            alerts.append("Normal")

        # Store room details
        hostel[floor].append({
            "room": room,
            "electricity": electricity,
            "water": water,
            "electricity_charge": electricity_charge,
            "water_charge": water_charge,
            "total_charge": total_charge,
            "status": ", ".join(alerts)
        })

# Display room-wise report
print("\n========== ROOM-WISE REPORT ==========")

for floor, room_list in hostel.items():

    print(f"\nFloor {floor}")

    for data in room_list:

        print(
            f"Room {data['room']} | "
            f"Electricity: {data['electricity']} kWh | "
            f"Water: {data['water']} L | "
            f"Total Charge: Rs.{data['total_charge']:.2f} | "
            f"Status: {data['status']}"
        )

# Floor-wise analysis
print("\n========== FLOOR-WISE ANALYSIS ==========")

floor_summary = {}

for floor, room_list in hostel.items():

    total_electricity = sum(
        r["electricity"] for r in room_list
    )

    total_water = sum(
        r["water"] for r in room_list
    )

    total_charge = sum(
        r["total_charge"] for r in room_list
    )

    floor_summary[floor] = {
        "electricity": total_electricity,
        "water": total_water,
        "charge": total_charge
    }

    print(f"\nFloor {floor}")
    print(f"Electricity: {total_electricity} kWh")
    print(f"Water: {total_water} Litres")
    print(f"Total Charges: Rs.{total_charge:.2f}")

# Compare floors
highest_electricity_floor = max(
    floor_summary,
    key=lambda f: floor_summary[f]["electricity"]
)

highest_water_floor = max(
    floor_summary,
    key=lambda f: floor_summary[f]["water"]
)

# Find highest consuming rooms
all_rooms = [
    (floor, room)
    for floor, room_list in hostel.items()
    for room in room_list
]

highest_electricity_room = max(
    all_rooms,
    key=lambda x: x[1]["electricity"]
)

highest_water_room = max(
    all_rooms,
    key=lambda x: x[1]["water"]
)

print("\n========== FINAL SUMMARY ==========")

print(
    f"Highest Electricity Floor: "
    f"Floor {highest_electricity_floor}"
)

print(
    f"Highest Water Consumption Floor: "
    f"Floor {highest_water_floor}"
)

print(
    f"Highest Electricity Room: "
    f"Floor {highest_electricity_room[0]}, "
    f"Room {highest_electricity_room[1]['room']}"
)

print(
    f"Highest Water Consumption Room: "
    f"Floor {highest_water_room[0]}, "
    f"Room {highest_water_room[1]['room']}"
)

print("\nHostel Resource Monitoring Completed!")

