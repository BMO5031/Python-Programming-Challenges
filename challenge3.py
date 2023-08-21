def solve(s):
    def get_value(c):
        return ord(c) - ord('a') + 1
    
    max_value = 0
    current_value = 0
    
    for char in s:
        if char not in "aeiou":
            current_value += get_value(char)
            if current_value > max_value:
                max_value = current_value
        else:
            current_value = 0
            
    return max_value
print(solve("hello"))