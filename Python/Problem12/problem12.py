def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    r = []
    for i in range(size):
        s = '-'.join(alphabet[i:n])
        s = s[::-1] + s[1:]
        r.append(s.center(4 * n - 3, '-'))
    print('\n'.join(r[:0:-1] + r))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)