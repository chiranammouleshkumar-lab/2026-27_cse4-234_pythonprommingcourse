
# Multi-Criteria Internship Candidate Ranking

candidates = []
qualified = []
rejected = []

n = int(input("Enter number of candidates: "))

# Accept candidate details
for i in range(n):
    print(f"\nEnter details of Candidate {i + 1}")

    name = input("Candidate Name: ")
    marks = float(input("Academic Marks (%): "))
    assessment = float(input("Assessment Score (%): "))
    attendance = float(input("Attendance (%): "))

    # Validate input
    if not all(0 <= x <= 100 for x in
               [marks, assessment, attendance]):
        print("Invalid input! Values must be 0-100.")
        continue

    # Check eligibility
    reasons = []

    if marks < 60:
        reasons.append("Academic marks below 60%")

    if assessment < 50:
        reasons.append("Assessment score below 50%")

    if attendance < 75:
        reasons.append("Attendance below 75%")

    candidate = {
        "name": name,
        "marks": marks,
        "assessment": assessment,
        "attendance": attendance
    }

    if not reasons:
        # Calculate weighted score
        score = (
            marks * 0.40 +
            assessment * 0.40 +
            attendance * 0.20
        )

        candidate["total"] = score
        qualified.append(candidate)

    else:
        candidate["reason"] = ", ".join(reasons)
        rejected.append(candidate)

# Sort candidates using tie-breaking rules
qualified.sort(
    key=lambda x: (
        -x["total"],
        -x["assessment"],
        -x["marks"],
        -x["attendance"],
        x["name"].casefold()
    )
)

# Display qualified candidates
print("\n========== FINAL INTERNSHIP RANKING ==========")

if qualified:
    print("Rank  Name       Marks  Assessment  Attendance  Score")

    for rank, c in enumerate(qualified, start=1):
        print(
            f"{rank:<5} "
            f"{c['name']:<10} "
            f"{c['marks']:<7.1f} "
            f"{c['assessment']:<12.1f} "
            f"{c['attendance']:<12.1f} "
            f"{c['total']:.2f}"
        )
else:
    print("No qualified candidates found.")

# Display rejected candidates
print("\n========== REJECTED CANDIDATES ==========")

if rejected:
    for c in rejected:
        print(f"\nName: {c['name']}")
        print(f"Reason: {c['reason']}")
else:
    print("No rejected candidates.")

