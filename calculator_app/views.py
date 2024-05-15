from django.shortcuts import render
from django.http import HttpResponse
import json

def calculate(request):
    if request.method == 'GET':
        return render(request, 'calculator.html')

    elif request.method == 'POST':
        data = json.loads(request.body)
        a = int(data.get('a', 0))
        b = int(data.get('b', 0))
        operation = data.get('operation')
        result = None

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            result = a / b if b != 0 else 'Cannot divide by zero'

        return HttpResponse(json.dumps({'result': result}), content_type="application/json")
