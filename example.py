def line_processing(line):
    operator = '-+*/=%'
    n = 0
    a = ['']
    for i in line:
        if i in operator:
            a.append('')
            n = n + 1
            a[n] = a[n] + i
            a.append('')
            n = n + 1
        else:
            a[n] = a[n] + i
    return a


def math_operation(x):
    if x[1] == '+':
        x[0] = float(x[0]) + float(x[2])
    if x[1] == '-':
        x[0] = float(x[0]) - float(x[2])
    if x[1] == '*':
        x[0] = float(x[0]) * float(x[2])
    if x[1] == '/':
        x[0] = float(x[0]) / float(x[2])
    if x[1] == '%':
        x[0] = float(x[2])/float(x[0])*100
    if x[0] - int(x[0]) == 0:
        return int(x[0])
    else:
        return x[0]


