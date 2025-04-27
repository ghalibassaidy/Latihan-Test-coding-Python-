def char(s: str) -> dict:
    s = s.lower()
    counter = {}
    for char in s:
        if char != '':
            counter[char] = counter.get(char, 0) + 1
    return counter

print(char("Hello World"))