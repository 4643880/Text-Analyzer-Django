# I have created this file - Aizaz
from django.http import HttpResponse
from django.shortcuts import render

def indexFunc(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello")

def analyze(request):
    # Getting Text
    inputText = request.POST.get('textareaNameHTML', 'default')
    # Getting On / Off Values
    remText = request.POST.get('removePuncHTML', 'off')
    upperText = request.POST.get('upperHTML', 'off')
    lowerText = request.POST.get('lowerHTML', 'off')
    capitalizeText = request.POST.get('capitalizeHTML', 'off')
    newLineText = request.POST.get('newLineHTML', 'off')
    extraSpaceText = request.POST.get('extraSpaceHTML', 'off')

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
        analyzedNewLine = ""
        for i in inputText:
            if i != "\n" and i != "\r":
                analyzedNewLine = analyzedNewLine + i
        params = {'yourNewLine_text': analyzedNewLine}
        return render(request, 'analyze.html', params)
    elif extraSpaceText == 'on':
        analyzedExtraSpace = ""
        # Short Code
        for i, j in enumerate(inputText):
            if not(inputText[i] == " " and inputText[i + 1] == " "):
                analyzedExtraSpace = analyzedExtraSpace + j

        # Lengthy Code for understanding
        # inputText[i + 1] means next index number
        # for i, j in enumerate(inputText):
        #     if inputText[i] == " " and inputText[i + 1] == " ":
        #         pass
        #     else:
        #         analyzedExtraSpace = analyzedExtraSpace + j

        params = {'yourExtraSpace_text': analyzedExtraSpace}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Something Went Wrong (Aizaz)')

