# Step 1: Read input
n, k = map(int, input().split())  # Number of participants and the position threshold
scores = list(map(int, input().split()))  # Scores of participants

# Step 2: Determine the score threshold
threshold_score = scores[k - 1]

# Step 3: Count the number of participants who advance
advancers_count = sum(1 for score in scores if score >= threshold_score and score > 0)

# Step 4: Output the result
print(advancers_count)
