# Input the text as a single string
input_text = input()  # Example: "shock;979;23"

# Write your solution below and make sure to encode the word correctly

def max_energy(tokens):
    if not tokens:
        return 0
    
    elif len(tokens) == 1:
        return tokens[0]

    dp = [0] * len(tokens)
    dp[0] = tokens[0]
    dp[1] = max(tokens[0], tokens[1])
    
    for i in range(2, len(tokens)):
        dp[i] = max(dp[i-1], dp[i-2] + tokens[i])
    
    return dp[-1]

input_text = input_text.strip()

tokens = eval(input_text)

print(max_energy(tokens))