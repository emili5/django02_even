from django.shortcuts import render
import pdfplumber

# Create your views here.
def index(request):
    context={}
    if request.method=="POST":
        fi = request.FILES.get("file")
        if fi:
            pdf = pdfplumber.open(fi)
            num = len(pdf.pages)
            st=""
            for i in range(num):
                st+=pdf.pages[i].extract_text()
                context["st"]=st
    return render(request,'pdfread/index.html',context)





 # pdf page 객체들의 리스트
             # page 수만큼 객체들이 존재

# 1페이지 텍스트 추출