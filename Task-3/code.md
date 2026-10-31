# Courier Charge Optimization – Python Program

## 1. Problem Statement

Develop a Python program to calculate courier delivery charges based on parcel weight, dimensions, distance zones, delivery urgency, and declared restrictions.

The program should:

- Accept parcel weight, length, width, and height.
- Calculate actual weight and volumetric weight.
- Determine delivery charges based on distance zones.
- Apply additional charges for urgent delivery.
- Check restrictions such as fragile, liquid, and prohibited items.
- Compare different courier service options.
- Select the most economical eligible courier service.
- Display the final delivery charge and selected service.

## 2. Algorithm

1. Start the program.
2. Enter parcel weight, length, width, and height.
3. Calculate volumetric weight using:

\\[ \text{Volumetric Weight} = \frac{L \times W \times H}{5000} \\]

4. Calculate chargeable weight by selecting the maximum of actual weight and volumetric weight.
5. Enter the distance zone (Local, Regional, National).
6. Enter delivery urgency (Normal or Express).
7. Enter parcel restrictions (Fragile, Liquid, Prohibited).
8. Check whether the parcel is eligible for delivery.
9. Calculate charges for different courier services.
10. Compare the eligible courier charges.
11. Select the courier with the lowest delivery charge.
12. Display all courier options and the best option.
13. Stop.

## 3. Flowchart
```mermaid

flowchart TD
    A([Start]) --> B[/Enter parcel weight and dimensions/]
    B --> C[Calculate volumetric weight]
    C --> D[Calculate chargeable weight]
    D --> E[/Select distance zone/]
    E --> F[/Select delivery urgency/]
    F --> G[/Enter parcel restrictions/]
    G --> H{Is parcel prohibited?}

    H -->|Yes| I[Reject parcel]
    I --> Z([Stop])

    H -->|No| J[Calculate additional charges]
    J --> K[Compare courier services]
    K --> L{Service eligible?}

    L -->|No| M[Skip courier service]
    M --> K

    L -->|Yes| N[Calculate delivery charge]
    N --> O[Store courier and charge]
    O --> P{More services?}

    P -->|Yes| K
    P -->|No| Q{Any eligible service?}

    Q -->|No| R[Display no service available]
    Q -->|Yes| S[Select minimum charge]
    S --> T[Display best courier and charge]

    R --> Z
    T --> Z



```

## 4. Python Source Code

```
# Courier Charge Optimizationprint("===================================")print("     COURIER CHARGE OPTIMIZATION")print("===================================")# Input parcel detailsweight = float(input("Enter parcel weight (kg): "))length = float(input("Enter length (cm): "))width = float(input("Enter width (cm): "))height = float(input("Enter height (cm): "))# Calculate volumetric weightvolumetric_weight = (length * width * height) / 5000# Calculate chargeable weightchargeable_weight = max(weight, volumetric_weight)print("\nActual Weight:", weight, "kg")print("Volumetric Weight:", round(volumetric_weight, 2), "kg")print("Chargeable Weight:", round(chargeable_weight, 2), "kg")# Distance zoneprint("\nDistance Zones:")print("1. Local")print("2. Regional")print("3. National")zone = int(input("Select distance zone (1-3): "))zone_rates = {    1: 40,    2: 70,    3: 100
```

## 5. Sample Input

```
Enter parcel weight (kg): 2

Enter length (cm): 30
Enter width (cm): 20
Enter height (cm): 15

Select distance zone (1-3): 2

Select urgency (1-2): 2

Select restriction (1-4): 2
```

## 6. Sample Output

```
===================================
     COURIER CHARGE OPTIMIZATION
===================================

Actual Weight: 2.0 kg
Volumetric Weight: 1.8 kg
Chargeable Weight: 2.0 kg

========== COURIER COMPARISON ==========

Fast Express - Rs. 250.0
Speed Courier - Rs. 230.0
Budget Delivery - Not eligible for fragile parcels

========== FINAL RESULT ==========

Selected Courier: Speed Courier
Minimum Delivery Charge: Rs. 230.0

Thank you for using our system!
```

## 7. Mermaid Flowchart Code
<img src="<img width="1858" height="2794" alt="mermaid-diagram (2)" src="https://github.com/user-attachments/assets/04c0b608-68ac-42b0-8c88-2b1baa2a5d92" />



