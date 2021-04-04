# LING48/CS72 Homework 1: Eliza-style Chatbot
# Ari Chadda, Rolando Coto
# Last modification: 2021/03/28
#
# The program uses regular expressions to parse a user's input and generate a
# response in English. Be sure to test your regular expressions.

import sys
import re

def compileRegEx(regExInput):
  return re.compile(regExInput, re.IGNORECASE)

def eliza(userInput):
    reply = ""

    initalGreeting = compileRegEx(r'(Mi nombre es|Me llamo)(.* )?(.+)\b')
    stateOfMind = compileRegEx(r'([N|n]o )?([E|e]stoy) (.*?)(feliz|triste)')
    personCharacteristics = compileRegEx(r'([N|n]o )?([S|s]oy) (.*)?.')
    aboutFamily = compileRegEx(r'([P|p]apá|[M|m]amá)')
    modalVerbs = compileRegEx(r'([N|n]o )?([Q|q]uiero|[D|d]ebo|[P|p]uedo) (irme|mudarme|comerme)?(.*[\w])')
    thoughtsHopes = compileRegEx(r'([P|p]ienso|[E|e]spero)')
    specificExamples = compileRegEx(r'([S|s]iempre)')
    handlingInsults = compileRegEx(r'(¡estúpida!|idiota)')

    if (initalGreeting.match(userInput)):
        inputName = initalGreeting.search(userInput)
        if (inputName.group(3)):
            reply = "Hola, " + inputName.group(3) + ". ¿Cómo estás?"
    elif (stateOfMind.search(userInput)):
        stateWords = stateOfMind.search(userInput)
        if (stateWords.group(1)):
            reply = "¿Porqué " + stateWords.group(1).lower() + "estás " + stateWords.group(4) + "?"
        else:
            reply = "¿Porqué estás " + stateWords.group(4) + "?"
    elif (personCharacteristics.search(userInput)):
        characteristicWords = personCharacteristics.search(userInput)
        if (characteristicWords.group(1)):
            reply = "¿Porqué " + characteristicWords.group(1).lower() + "eres " + characteristicWords.group(3) + "?"
        else:
            reply = "¿Porqué eres " + characteristicWords.group(3) + "?"
    elif (aboutFamily.search(userInput)):
        fatherMother = aboutFamily.search(userInput)
        if (fatherMother.group(1)):
            reply = "Cuéntame más de tu " + fatherMother.group(1).lower() + "."
    elif (modalVerbs.search(userInput)):
        wantMust = modalVerbs.search(userInput)
        if (wantMust.group(1)):
            if (wantMust.group(3)):
                reply = "¿Porqué " + wantMust.group(1).lower() + wantMust.group(2)[:-1] + "es " + wantMust.group(3)[:-2] + "te" + wantMust.group(4) + "?"
            else:
                reply = "¿Porqué " + wantMust.group(1).lower() + wantMust.group(2)[:-1] + "es " + wantMust.group(4) + "?"
        else:
            if (wantMust.group(3)):
                reply = "¿Porqué " + wantMust.group(2)[:-1] + "es " + wantMust.group(3)[:-2] + "te" + wantMust.group(4) + "?"
            else:
                reply = "¿Porqué " + wantMust.group(2)[:-1] + "es " + wantMust.group(4) + "?"
    elif (thoughtsHopes.search(userInput)):
        thinkSuppose = thoughtsHopes.search(userInput)
        if (thinkSuppose.group(1)):
            reply = "¿Porqué " +  thinkSuppose.group(1).lower()[:-1] + "as " + "eso?"
    elif (specificExamples.search(userInput)):
        alwaysMore = specificExamples.search(userInput)
        if (alwaysMore.group(1)):
            reply = "¿Puedes darme un ejemplo específico?"
    elif (handlingInsults.search(userInput)):
        stupidIdiot = handlingInsults.search(userInput)
        if (stupidIdiot.group(1)):
            reply = "¡Hey, sin insultos! Cálmate y cuéntame más."
    else:
        reply = "Cuéntame más"

    return reply

if (len(sys.argv) < 2):
   print("Please provide an input phrase")

else:
    print(eliza(str(sys.argv[1])))
