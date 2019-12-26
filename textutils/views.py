# Author of file : Kshitij Nath
from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def analyzer(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # get the checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremover', 'off')
    charcounter = request.POST.get('charcounter','off')

    punctuation = string.punctuation
    analyzed = ""
    if removepunc == 'on':
        purpose = 'Punctuation Removed'
        for char in djtext:
            if char not in punctuation:
                analyzed += char

    elif uppercase == 'on':
        purpose = 'Upper Case'
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

    elif newlineremove == 'on':
        purpose = 'New Line Removed'
        for char in djtext:
            if char != '\n':
                analyzed += char
    
    elif charcounter=='on':
        counter=0
        for char in djtext:
            counter+=1
        purpose=str(counter)+'characters'
    
    elif newlineremove=='on' and charcounter=='on':
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed+=char
        
        count=str(len(djtext))
        analyzed=analyzed+'\n'+f'This contains {count} charecters'
    else:
        analyzed = 'You have not checked the box'
    params = {'purpose': f'{purpose}', 'analyzed_text': analyzed}
    # analyze the text
    return render(request, 'analyze.html', params)

def about(request):
    return render(request,'about.html')
