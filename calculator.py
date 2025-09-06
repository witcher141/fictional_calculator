# a= []
# a.append(10)   СТЭК
# x = a.pop()
# def top(a):
#     return a[len(a)-1] 
input = input("")    #СЮДА ВВОДИМ ВЫРАЖЕНИЕ
def na_tokeni(num1):  
    tokens = []     #список всех частичек(токенов)
    number = ""   #сюда собираем все циферки     
    for c in num1:
        if c.isdigit():       # попалась цифра,положили в number
            number += c
        else:
            if number != "":   # когда оператор ,убираем получившееся число из number в список tokens
                tokens.append(number)
                number = ""
            tokens.append(c)  # оператор,скобку сразу в список
    if number != "":
        tokens.append(number)
    return tokens
print(na_tokeni(input))  # смотрим на все токены,потом создаем стэк и аутпут
stack = []
output = []
def push(stack, value):  #чтобы добавить в стэк элемент
    stack.append(value)
def pop(stack):           #чтобы достать крайний элемент
    return stack.pop()
def top(stack):          #смотрим верхушку
    return stack[-1]
def is_empty(stack):      #кол-во элементов в стэке равно 0 (если не 0 , то будем добавлять)
    return len(stack) == 0 
priority = {'+': 1,'-': 1,'*': 2,'/': 2}    #приоритет в виде словарика
tokens = na_tokeni(input)       
for token in tokens:
    if token.isdigit():           #определяем число,если да, то все в аутпут
        output.append(token)
    elif token in '+-*/':         # оператор если подходит по приоритету пока стэк не пустой,то ложим в аутпут
        while not is_empty(stack) and top(stack) in '+-*/' and priority[top(stack)] >= priority[token]:
            output.append(pop(stack))    
        push(stack, token)     #ложим в стэк если норм с приоритетом все
    elif token == '(':
        push(stack, token)    #ложим в стэк скобочку,когда нашли вторую вытаскиваем через .pop все что внутри скобки в аутпут(скобки уходят)
    elif token == ')':
        while top(stack) != '(':
            output.append(pop(stack))
        pop(stack)  #убираем открывающую скобку из стека и в конце достаём всё оставшееся в стеке
while not is_empty(stack):              #все что сталось в аутпут
    output.append(pop(stack))
print(output)
batman = []    #финалочка
for token in output:
    if token.isdigit():                     # если токен число,то в стэк
        batman.append(int(token))      
    else:                                   # если не число,значит оператор
        b = batman.pop()                # достаём второй операнд плюс первый и выполняем с ними операцию
        a = batman.pop()               
        if token == '+':
            batman.append(a + b)
        elif token == '-':
            batman.append(a - b)
        elif token == '*':
            batman.append(a * b)
        elif token == '/':
            batman.append(a / b)
joker = batman.pop()     # :) (*^*)
print(joker)