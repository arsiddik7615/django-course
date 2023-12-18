from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={'author':'John','age':9, 'lst':['python','is','best'],'birthday' : datetime.datetime.now(),'courses':[
        {
            'id':1,
            'name': 'python',
            'fee' : 5000
        },
        {
            'id':2,
            'name': 'django',
            'fee' : 50008
        },
        {
            'id':3,
            'name': 'c course',
            'fee' : 1000
        },
        
        
    ]}
    return render(request,'home.html',d)