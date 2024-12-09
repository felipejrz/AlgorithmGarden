def timeConversion(s):
    hora, periodo = s[:-2], s[-2:]
    horas, min, seg = map(int, hora.split(':'))
    if periodo == 'PM' and horas != 12:
        horas += 12
    elif periodo == 'AM' and horas == 12:
        horas = 0
    print(f'{horas:02}:{min:02}:{seg:02}')

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
