from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'jinjaoperations.html',context=d)

def loop(request):
    fd={'name':'pikun','mobile':[9078343412,99329822928]}
    return render(request,'loop.html',context=fd)