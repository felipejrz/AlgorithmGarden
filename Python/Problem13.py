def solve(s):
    words = s.split()
    result = []

    for word in words:
        if word and word[0].isalpha():  # Comprobamos que sea letra
            result.append(word[0].upper() + word[1:])
        else:
            result.append(word)

    return " ".join(result)


if __name__ == '__main__':
    s = input()
    print(solve(s))