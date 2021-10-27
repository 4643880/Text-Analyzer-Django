# I have created this file - Aizaz
from django.http import HttpResponse
from django.shortcuts import render

def indexFunc(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello")


def analyze(request):
    # Getting Text
    inputText = request.GET.get('textareaNameHTML', 'default')
    # Getting On / Off Values
    remText = request.GET.get('removePuncHTML', 'off')
    upperText = request.GET.get('upperHTML', 'off')
    lowerText = request.GET.get('lowerHTML', 'off')
    capitalizeText = request.GET.get('capitalizeHTML', 'off')
    newLineText = request.GET.get('newLineHTML', 'off')
    extraSpaceText = request.GET.get('extraSpaceHTML', 'off')

    # Selections Statement Starts Here
    if remText == 'on':
        totalpunctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_var = ''
        for i in inputText:
            if i not in totalpunctuations:
                analyzed_var = analyzed_var + i
        params = {'analyzed_text': analyzed_var}
        return render(request, 'analyze.html', params)
    elif upperText == 'on':
        analyzedcaps = ""
        for i in inputText:
            analyzedcaps = analyzedcaps + i.upper()
        params = {'yourUpperCase_text': analyzedcaps}
        return render(request, 'analyze.html', params)
    elif lowerText == 'on':
        analyzedlower = ""
        for i in inputText:
            analyzedlower = analyzedlower + i.lower()
        params = {'yourLowerCase_text': analyzedlower}
        return render(request, 'analyze.html', params)
    elif capitalizeText == 'on':
        analyzedcapitalize = str(inputText).capitalize()
        # for i in inputText:
        #     analyzedcapitalize = analyzedcapitalize + i.capitalize()
        params = {'yourCapitalize_text': analyzedcapitalize}
        return render(request, 'analyze.html', params)
    elif newLineText == 'on':
        analyzedNewLine= ""
        for i in inputText:
            if i != "\n":
                analyzedNewLine = analyzedNewLine + i
        params = {'yourNewLine_text': analyzedNewLine}
        return render(request, 'analyze.html', params)
    elif extraSpaceText == 'on':
        analyzedExtraSpace= ""
        for i in inputText:
            if i != "  ":
                analyzedExtraSpace = analyzedExtraSpace + i
        params = {'yourExtraSpace_text': analyzedExtraSpace}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Something Went Wrong (Aizaz)')





    # elif upperText == 'on' and remText == 'on':
    #     totalpunctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analyzed_var = ''
    #     for i in inputText:
    #         if i not in totalpunctuations:
    #             analyzed_var = analyzed_var + i
    #     doingUpperCaseVar = str(inputText).upper()
    #     params = {'analyzed_text': analyzed_var, 'yourUpperCase_text': doingUpperCaseVar}
    #     return render(request, 'analyze.html', params)








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

