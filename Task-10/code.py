
# Multi-Event Sports Scheduling and Scoring

# Event schedule using tuples
events = [
    ("Cricket", "2026-11-01", "09:00", "Ground A"),
    ("Football", "2026-11-01", "10:00", "Ground B"),
    ("Basketball", "2026-11-01", "09:00", "Ground A"),
    ("Volleyball", "2026-11-02", "11:00", "Ground C")
]

print("===== SPORTS EVENT SCHEDULE =====")

for event in events:
    print(event)

# Check scheduling conflicts
print("\n===== SCHEDULING CONFLICTS =====")

conflict_found = False

for i in range(len(events)):
    for j in range(i + 1, len(events)):
        if (events[i][1] == events[j][1] and
            events[i][2] == events[j][2] and
            events[i][3] == events[j][3]):

            print(events[i][0], "and", events[j][0],
                  "have a scheduling conflict.")
            conflict_found = True

if not conflict_found:
    print("No scheduling conflicts found.")

# Team scores using tuples
scores = [
    ("Team A", "Cricket", 30),
    ("Team B", "Cricket", 20),
    ("Team C", "Cricket", 25),
    ("Team A", "Football", 20),
    ("Team B", "Football", 30),
    ("Team C", "Football", 15),
    ("Team A", "Basketball", 25),
    ("Team B", "Basketball", 15),
    ("Team C", "Basketball", 25),
    ("Team A", "Volleyball", 10),
    ("Team B", "Volleyball", 20),
    ("Team C", "Volleyball", 15)
]

# Calculate total points
total_points = {}

for team, event, points in scores:
    if team not in total_points:
        total_points[team] = 0

    total_points[team] += points

# Sort teams by points and alphabetical order
rankings = sorted(
    total_points.items(),
    key=lambda x: (-x[1], x[0])
)

# Display final rankings
print("\n===== TEAM TOTAL POINTS =====")

for team, points in total_points.items():
    print(team, ":", points)

print("\n===== FINAL RANKINGS =====")

for rank, (team, points) in enumerate(rankings, start=1):
    print(rank, ".", team, "-", points, "points")

print("\nProgram completed successfully.")

