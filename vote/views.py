from django.shortcuts import redirect, render
from .models import Topic,Choice
# Create your views here.
def index(request):
    t = Topic.objects.all()
    context={
        "tset":t
    }
    return render(request,'vote/index.html',context)

def detail(request,bpk):
    t=Topic.objects.get(id=bpk)
    c = t.choice_set.all()
    context={
        "cset":c,
        "t":t
    }
    return render(request,'vote/detail.html',context)

def vote(request,tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get("ch")
        c = Choice.objects.get(id=tpk)
        c.choicer.add(request.user)
    return redirect('vote:detail',tpk)