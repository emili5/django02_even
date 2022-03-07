from django.shortcuts import redirect, render
from .models import Board,Reply
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def index(request):
    b= Board.objects.all()
    context={
        "bset":b
    }
    return render(request,"board/index.html",context)

def detail(request,bpk):
    b = Board.objects.get(id=bpk)
    r= b.reply_set.all() #board에 단 댓글 다 나옴
    context={
        "b":b,
        "rset":r
    }
    return render(request,"board/detail.html",context)
def delete(request,bpk):
    b = request.objects.get(id=bpk)
    if request.user == b.writer: # 일치할 때만 삭제!
        b.delete()
    else:
        messages.error(request,"잘못된 접근입니다")
    return redirect("board:detail")

def create(request):
    if request.method == "POST":  
        bs = request.POST.get("sub")
        bc = request.POST.get("con")
        if bs and bc:
            Board(subject=bs,content=bc,writer=request.user,pubdate=timezone.now())
        return redirect("board:index")
    return render(request,"board/create.html")

def update(request,bpk):
    b=Board.objects.get(id=bpk)
    #자신의 글이 아니면 지정 페이지로 이동!->보안 생각했다고 포트폴리오에 어필하기!!
    if request.user != b.writer:
        messages.error(request,"자신이 작성한 글만 접근할 수 있습니다")
        return redirect("board:index")
    if request.method=="POST":
        bs  = request.POST.get("sub")
        bc = request.POST.get("con")
        b.subject= bs,b.comment=bc
        b.save()
        return redirect("board:detail")
    context={
        "b":b
    }
    return render(request,"board/update.html",context)

def creply(request,bpk):
        c = request.POST.get("com")
        b = Board.objects.get(id=bpk)
        Reply(b=b,replyer=request.user,comment=c,pubdate=timezone.now()).save()
        return redirect("board:detail",bpk)
   

def dreply(request,bpk,rpk):
    r = Reply.objects.get(id=rpk)
    if r.replyer == request.user:
        r.delete()
    else:
        pass
    return redirect("board:detail",bpk)

def likey(request,bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect('board:detail',bpk)

def cancel(request,bpk):
    b = Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect('board:detail',bpk)