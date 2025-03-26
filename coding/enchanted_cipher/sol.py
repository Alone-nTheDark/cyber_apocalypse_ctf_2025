input_text = input().strip()

N = int(input())
shifts = eval(input())

len_shifts = len(shifts)
result = []

group_size = 5
alpha_index = 0

for ch in input_text:
    if ch.isalpha():
        group_index = alpha_index // group_size
        shift = shifts[group_index]

        original_code = (ord(ch.lower()) - ord('a') - shift) % 26
        result.append(chr(original_code + ord('a')))
        alpha_index += 1
    else:
        result.append(ch)

print("".join(result))