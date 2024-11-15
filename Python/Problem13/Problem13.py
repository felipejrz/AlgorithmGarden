def solve(s):
    result = []
    flag = True

    for char in s:
        if char == " ":
            result.append(char)
            flag = True
        elif flag:
            result.append(char.upper())  
            flag = False 
        else:
            result.append(char) 

    return "".join(result)


if __name__ == '__main__':
    s = input()
    print(solve(s))