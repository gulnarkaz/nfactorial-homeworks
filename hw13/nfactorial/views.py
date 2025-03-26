from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, nfactorial school!")

def add(request, first, second):
    result = first + second
    return HttpResponse(f"Сумма {first} и {second} равна {result}")

def upper(request, text):
    return HttpResponse(text.upper())

def palindrome(request, word):
    if word == word[::-1]:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def calculator(request, first, operation, second):
    if operation == 'add':
        result = first + second
    elif operation == 'sub':
        result = first - second
    elif operation == 'mult':
        result = first * second
    elif operation == 'div':
        if second == 0:
            return HttpResponse("Ошибка: Деление на ноль!")
        result = first / second

    return HttpResponse(f"Результат: {result}")