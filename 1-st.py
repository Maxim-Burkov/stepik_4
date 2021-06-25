В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа, которым они соответствуют в десятичной системе счисления):

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.

Формат ввода:
Строка, содержащая натуральное число nn, 0 < n < 40000<n<4000.

Формат вывода:
Строка, содержащая число, закодированное в римской системе счисления.

Sample Input 1:

1984
Sample Output 1:

MCMLXXXIV
Sample Input 2:

9
Sample Output 2:

IX
Sample Input 3:

3
Sample Output 3:

III




inp = str(input())
result = ''
romans = (
    ('C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', ''),
    ('X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ''),
    ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', '')
)

for i in range(len(inp)):
    if i == 0 and len(inp) == 4:
        result += 'M' * int(inp[i])
    else:
        result += romans[(i - len(inp)) % 3][int(inp[i]) - 1]

print(result)
