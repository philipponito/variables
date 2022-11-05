"""
Питт 63
Ургант 78
Нагиев 67
Фокс 86
Бибер 94
"""

right_answers = 0
mistakes = 0
i = 'да'
while i == "да":
    print('Угадайте, в каком году родились следующие знаменитости?')

    pitt = (int(input("Бред Питт: ")))
    if pitt == 1963:
        right_answers += 1
    else:
        mistakes +=1

    urgant = (int(input("Иван Ургант: ")))
    if urgant == 1978:
        right_answers +=1
    else: mistakes +=1

    nagiev = (int(input('Дмитрий Нагиев:')))
    if nagiev == 1967:
        right_answers +=1
    else: mistakes +=1
    fox = (int(input("Меган Фокс: ")))
    if fox == 1986:
        right_answers += 1
    else: mistakes +=1

    bieber = (int(input('Джастин Биебер:')))
    if bieber== 1994:
        right_answers +=1
    else: mistakes +=1
    print ('Правильных ответов: ',right_answers)
    print('Ошибок: ',mistakes)
    proc_positive = right_answers*100/5
    print('Процент правильных ответов: ',proc_positive,'%')
    print("Процент неправильных ответов: ",100 - proc_positive,"%" )
    i = input('Хотите сыграть снова?')
print("Всего хорошего!")