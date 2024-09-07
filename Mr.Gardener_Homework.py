solution = 1275120

def count_valid_strings():
    count = 0
    for a in range(1, 6):  # 1 to 5 represent the 5 vowels
        for b in range(1, 27):
            if a == b:
                continue
            for c in range(1, 27):
                if b == c or a == c:
                    continue
                for d in range(1, 27):
                    if a == d or b == d or c == d:
                        continue
                    for e in range(6, 27):  # 6 to 26 represent the 21 consonants
                        if a == e or b == e or c == e or d == e:
                            continue
                        count += 1
    return count

result = count_valid_strings()
print(f"The number of valid strings is: {result}")

