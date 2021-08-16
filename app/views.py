from django.shortcuts import render

# Create your views here.
def renderfun(args):
    return render(args,'one.html',context={'name':'Dhoni','team':'CSK'})
    