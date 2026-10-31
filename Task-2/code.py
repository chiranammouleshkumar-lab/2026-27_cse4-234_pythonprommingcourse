
import math

print("===== ATTENDANCE RECOVERY COMPUTATION =====")

# Input
total_classes = int(input("Enter total conducted classes: "))
attended_classes = int(input("Enter attended classes: "))
required_percentage = float(input("Enter required attendance percentage: "))

# Input validation
if total_classes <= 0:
    print("Total classes must be greater than zero.")

elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid attended classes.")

elif required_percentage <= 0 or required_percentage > 100:
    print("Invalid required percentage.")

else:
    # Calculate current attendance
    current_percentage = (attended_classes / total_classes) * 100

    print("\n----- CURRENT ATTENDANCE -----")
    print("Total Classes:", total_classes)
    print("Attended Classes:", attended_classes)
    print("Current Attendance: {:.2f}%".format(current_percentage))
    print("Required Attendance:", required_percentage, "%")

    # Eligibility check
    if current_percentage >= required_percentage:
        print("\nStatus: ELIGIBLE")
        print("You have already reached the required attendance.")
        minimum_classes = 0

    else:
        # Calculate minimum consecutive classes
        minimum_classes = math.ceil(
            (required_percentage * total_classes / 100 - attended_classes)
            / (1 - required_percentage / 100)
        )

        print("\nStatus: NOT ELIGIBLE")
        print("Minimum consecutive classes required:",
              minimum_classes)

    # Future attendance scenarios
    print("\n----- FUTURE ATTENDANCE SCENARIOS -----")

    scenarios = [5, 10, 15, 20, 30]

    for future_classes in scenarios:
        future_attendance = (
            (attended_classes + future_classes) /
            (total_classes + future_classes)
        ) * 100

        print("\nIf you attend", future_classes, "more classes:")
        print("Future Attendance: {:.2f}%".format(future_attendance))

        if future_attendance >= required_percentage:
            print("Status: ELIGIBLE")
        else:
            print("Status: NOT ELIGIBLE")

    print("\n===== END OF PROGRAM =====")

