from django.shortcuts import render
import random

# Create your views here.
def index_view(request):

    return render(request, 'index.html')

def get_result(request):
    print("TEST_01")
    print(request.POST.get('operation'))
    x = request.POST.get('fnum')
    y = request.POST.get('snum')
    x = int(x)
    y = int(y)
    result = ''
    operation = request.POST.get('operation')
    if operation == 'add':
        result = x + y
        print(f'result: {result}')
    elif operation == 'subtract':
        result = x - y
        print(f'result: {result}')
    elif operation == 'multiply':
        result = x * y
        print(f'result: {result}')
    elif operation == 'divide':
        result = x / y
        r = round(result)
        if result % r == 0:
            result = r
        print(f'result: {result}')

    return render(request, 'index.html', context={'res': result})
