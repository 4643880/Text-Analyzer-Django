# I have created this file - Aizaz
from django.http import HttpResponse
from django.shortcuts import render

def indexFunc(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello")


def analyze(request):
    inputText = request.GET.get('textareaNameHTML', 'default')
    print(inputText)
    remText = request.GET.get('removePuncHTML', 'off')
    print(remText)
    if remText == 'on':
        totalpunctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_var = ''
        for i in inputText:
            if i not in totalpunctuations:
                analyzed_var = analyzed_var + i

        params = {'analyzed_text': analyzed_var, 'purpose': 'Remove Punctuations', }
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Something Went Wrong (Aizaz)')










#
# def removePuncFunc(request):
#     gettingText = print(request.GET.get('textareaName', 'default'))
#     print(gettingText)
#     return HttpResponse("Hello")
#
# def capfirstFunc(request):
#     return HttpResponse("Hello")
#
# def spaceremoveFunc(request):
#     return HttpResponse("Hello")
#
# def charcountFunc(request):
#     return HttpResponse("Hello asdfd")

