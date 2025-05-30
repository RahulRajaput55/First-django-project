from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render (request,'index.html')

def home(request):
    return HttpResponse("Welcome to Home Page")

def analyze(request):
    dj=request.POST.get('text', 'default')
    jd=request.POST.get('removepunc','off')
    cap=request.POST.get('capitalize','off')
    charcnt=request.POST.get('charcount','off')
    print(dj)
    print(jd)
    print(cap)
    analyze= ""
    punctuations = '''.,?!:;-–—'"‘’“”()[]{}..@#$%&*/\\|^~_=+<>`'''
    if jd=='on' and cap=='on'and charcnt=='on':
        count=0
        for char in dj:
            if char not in punctuations:
                analyze=analyze+char.upper()
                count=count+1
        param={ 'Analyzed_text' : analyze, 'Count_Characters' : count }
        return render (request,'analyze.html',param)
    
    elif jd=='on' and cap=='off' and charcnt=='on':
        count=0
        for char in dj:
            if char not in punctuations:
                analyze=analyze+char
                count=count+1
        param={ 'Analyzed_text' : analyze,'Count_Characters' : count}
        return render (request,'analyze.html',param)
    
    elif jd=='on' and cap=='on' and charcnt=='off':
        for char in dj:
            if char not in punctuations:
                analyze=analyze+char.upper()
                
        param={ 'Analyzed_text' : analyze }
        return render (request,'analyze.html',param)
    
    elif jd=='on' and cap=='off' and charcnt=='off':
        for char in dj:
            if char not in punctuations:
                analyze=analyze+char
            
        param={ 'Analyzed_text' : analyze }
        return render (request,'analyze.html',param)
    
    elif jd=='off' and cap=='on' and charcnt=='on':
        count=0
        for char in dj:
            analyze=analyze+char.upper()
            count=count+1
    
        param={ 'Analyzed_text' : analyze, 'Count_Characters' : count }
        return render (request,'analyze.html',param)
    
    elif jd=='off' and cap=='off' and charcnt=='on':
        count=0
        for char in dj:
            analyze=analyze+char
            count=count+1
        param={ 'Analyzed_text' : analyze, 'Count_Characters' : count }
        return render (request,'analyze.html',param)
    
    elif jd=='off' and cap=='on' and charcnt=='off':
        for char in dj:
            analyze=analyze+char.upper()
            
        param={ 'Analyzed_text' : analyze,}
        return render (request,'analyze.html',param)
        
    else:
        return HttpResponse("""<html>
                                    <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
                                         <div style="color: red; font-weight: bold; font-size: 1.2em;">
                                            ERROR
                                        </div>
                                        <div style="color: red; font-weight: bold; font-size: 1.2em;">
                                            You have to switch at least one of them.
                                        </div>
                                     </body>
                                </html>
                            """)
    

def contactus(request):
    return HttpResponse("Contact Us Page")

def navigator(request):
    return render(request,'navigator.html')