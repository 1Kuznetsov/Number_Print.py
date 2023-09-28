'''
Задание 20.
Дано натуральное число не превосходящее 900 000 000. Напишите программу, которая
выводит на экран это число русскими словами.
'''


number = input()

digits = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
digits_form = ['одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
tens = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
        'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
tens_special = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
hundreds = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот',
            'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
thousands = ['тысяча', 'тысячи', 'тысяч']
millions = ['миллион', 'миллиона', 'миллионов']

number = number.rjust(9, '0')
res = ''


for i in range(2, 9, 3):
    left = i - 2
    right = i + 1
    ptr = number[left:right]

    if ptr.lstrip('0') != '':
        first = int(ptr[0])
        if first != 0:
            res += hundreds[first - 1] + ' '
        remain = int(ptr[1] + ptr[2])
        second = remain // 10
        third = remain % 10

        if remain != 0:
            if 0 < remain < 10:
                if i == 5:
                    res += digits_form[remain - 1] + ' '
                else:
                    res += digits[remain - 1] + ' '
            elif 9 < remain and third == 0:
                res += tens[second - 1] + ' '
            elif 10 < remain < 20:
                res += tens_special[third - 1] + ' '
            else:
                res += tens[second - 1] + ' '
                if i == 5:
                    res += digits_form[third - 1] + ' '
                else:
                    res += digits[third - 1] + ' '

        if i == 2:
            if third == 1:
                res += millions[0] + ' '
            elif 1 < third < 5:
                res += millions[1] + ' '
            else:
                res += millions[2] + ' '

        if i == 5:
            if third == 1:
                res += thousands[0] + ' '
            elif 1 < third < 5:
                res += thousands[1] + ' '
            else:
                res += thousands[2] + ' '

print(res)
