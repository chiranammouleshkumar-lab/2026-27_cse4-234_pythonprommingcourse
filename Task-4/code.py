
# Student Feedback Sentiment Scoring

positive_keywords = [
    "good", "excellent", "great",
    "helpful", "interesting", "amazing",
    "best", "clear", "easy", "friendly"
]

negative_keywords = [
    "bad", "poor", "worst",
    "difficult", "boring", "slow",
    "confusing", "hard", "waste", "weak"
]

# Get number of feedback sentences
n = int(input("Enter number of feedback sentences: "))

for i in range(n):

    print("\nFeedback", i + 1)
    feedback = input("Enter feedback: ").lower()

    # Initialize counters
    positive_count = 0
    negative_count = 0

    # Split feedback into words
    words = feedback.split()

    # Count positive and negative keywords
    for word in words:
        word = word.strip(".,!?;:")

        if word in positive_keywords:
            positive_count += 1

        if word in negative_keywords:
            negative_count += 1

    # Calculate sentiment score
    score = positive_count - negative_count

    # Classify feedback
    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Display results
    print("\n----- Feedback Analysis -----")
    print("Positive Indicators:", positive_count)
    print("Negative Indicators:", negative_count)
    print("Sentiment Score:", score)
    print("Feedback Classification:", sentiment)

print("\nFeedback Analysis Completed!")

