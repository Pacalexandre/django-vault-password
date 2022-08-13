from django.shortcuts import render

def index(request):
    coins = [{'name':'batman','price':1.23 , 'symbol':'aa' , 'rank':1},
    {'name':'robin','price':1.23 , 'symbol':'aa' , 'rank':2},
    {'name':'gata','price':1.23 , 'symbol':'aa' , 'rank':3},
    ]
    return render(request, 'index.html',context={'coins': coins})