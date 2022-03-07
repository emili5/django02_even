from django.shortcuts import render,redirect
import googletrans
from googletrans import Translator
 
# Create your views here.
def index(request):
    #딕셔너리로 전달받음
    context={}
    if request.method=="POST":
        bf = request.POST.get("bf")
        fr = request.POST.get("from")
        to = request.POST.get("to")
        translator = Translator()
        if bf:
            trans = translator.translate(bf, src=fr, dest=to)
            # print(trans.text)
            context.update({
                "af":trans.text,
                "bf":bf,
                "fr":fr,
                "to":to
            })
    return render(request,'trans/index.html',context)
    



 
# text1 = "Hello welcome to my website!"
 

 





