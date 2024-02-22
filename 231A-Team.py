# Step 1: Read input
n = int(input())  # Number of problems
problems_count = 0  # Counter to store the number of problems they will implement

# Step 2: Iterate through each problem
for _ in range(n):
    opinions = list(map(int, input().split()))  # Read opinions of the three friends for the current problem
    # Check if at least two friends are sure about the solution
    if sum(opinions) >= 2:
        problems_count += 1  # Increment the count of problems they will implement

# Step 3: Output the result
print(problems_count)