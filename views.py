from django.http import HttpResponse

def calculate(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    op = request.GET.get('op')  

    if not num1 or not num2:
        return HttpResponse("Please provide both num1 and num2 in the query.")

    num1 = int(num1)
    num2 = int(num2)

    if op == 'add':
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    else:
        return HttpResponse("Please provide a valid operation: ?op=add or ?op=sub")

    return HttpResponse(f"Result: {result}")
