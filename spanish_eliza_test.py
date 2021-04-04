# =====================================================================================
# LING48/CS72 Homework 1 Grading Help
# Rolando Coto (rolando.a.coto.solano@dartmouth.edu)
# Last modification: 2021/03/28
#
# The program reads the function eliza from a student's file and then
# prints examples of phrases that should be handled by each of the
# eight regular expressions 
#
# YOU NEED TO MODIFY TWO VARIABLES TO DO THE GRADING:
# userFilename: The name of the student's .py file (without the extension)
# usesAccents:  Whether the student uses Spanish characters or not (e.g. á,ñ,¿)
# =====================================================================================

import sys
import importlib
userFilename = "hw1_eliza_complete"  # Don't include the .py extension
m = importlib.import_module(userFilename)

usesAccents = 1 # The person used accents in words like "mamá" ("mom")

# =====================================================================================================
# Function:     replaceAccents
# Input:        strWithAccents (a string with Spanish text)
# Output:       withoutAccents (a string with Spanish text, where all characters are basic ASCII)
# Description:  Takes text and replaces Spanish special characters when their non-accent equivalents
# =====================================================================================================

def replaceAccents(strWithAccents):
    withoutAccents = strWithAccents.replace("á", "a")
    withoutAccents = withoutAccents.replace("é", "e")
    withoutAccents = withoutAccents.replace("í", "i")
    withoutAccents = withoutAccents.replace("ó", "o")
    withoutAccents = withoutAccents.replace("ú", "u")
    withoutAccents = withoutAccents.replace("ñ", "n")
    withoutAccents = withoutAccents.replace("Á", "A")
    withoutAccents = withoutAccents.replace("É", "E")
    withoutAccents = withoutAccents.replace("Í", "I")
    withoutAccents = withoutAccents.replace("Ó", "O")
    withoutAccents = withoutAccents.replace("Ú", "U")
    withoutAccents = withoutAccents.replace("Ñ", "N")
    withoutAccents = withoutAccents.replace("¡", "")
    withoutAccents = withoutAccents.replace("¿", "")
    return withoutAccents

# =====================================================================================================
# Function:     printAnswers
# Input:        (1) userInput (string with text in Spanish; what the user tells the computer)
#               (2) expectedAnswer (string with text in Spanish; what the computer should reply)
#               (3) translationUserInput (string with text in English)
#               (4) translationExpectedAns (string with text in English)
# Output:       No returned variable
# Description:  Takes userInput and sends it to the eliza function. Then, it prints the answer
#               along with the expected answer (and the translations, to make reading them easier)
# =====================================================================================================

def printAnswers(userInput, expectedAnswer, translationUserInput, translationExpectedAns):
    
    print("USER:             " + translationUserInput)
    print("COMPUTER:         " + translationExpectedAns)
    
    if (usesAccents == 0):
        userInput = replaceAccents(userInput)
        expectedAnswer = replaceAccents(expectedAnswer)
      
    studentOutput = m.eliza(userInput)
    if (usesAccents == 0): studentOutput = replaceAccents(studentOutput)
        
    print("INPUT:            " + userInput)
    print("EXPECTED OUTPUT : " + expectedAnswer)
    print("STUDENT OUTPUT:   " + studentOutput)
    print("\n")

# =====================================================================================
# Main body of the program
# The system sends a number of inputs to printAnswers, so that it can get
# the answer from the eliza function and format it to make it easier to grade.
# =====================================================================================

print("\n---------- File being read ----------\n")

print(userFilename + ".py")

print("\n---------- 1. Name ----------\n")

printAnswers("Mi nombre es Rolando", "Hola, Rolando. ¿Cómo estás?", "My name is Rolando", "Hi, Rolando. How are you?")
printAnswers("Me llamo Rolando.", "Hola, Rolando. ¿Cómo estás?", "I'm called Rolando", "Hi, Rolando. How are you?")

print("---------- 2. State of mind ----------\n")

printAnswers("estoy muy feliz... :)", "¿Porqué estás feliz?", "i'm very happy ... :)", "Why are you happy?")
printAnswers("No estoy feliz.", "¿Porqué no estás feliz?", "I'm not happy.", "Why aren't you happy?")
printAnswers("Yo estoy un poco triste.", "¿Porqué estás triste?", "I'm a bit sad", "Why are you sad?")
printAnswers("Estoy un poco triste.", "¿Porqué estás triste?", "I'm a bit sad", "Why are you sad?")

print("---------- 3. Characteristics of a person ----------\n")

printAnswers("Soy desordenado.", "¿Porqué eres desordenado?", "I'm messy", "Why are you messy?")
printAnswers("Yo no soy una persona ordenada.", "¿Porqué no eres una persona ordenada?", "I'm not a tidy person", "Why aren't you a tidy person?")
printAnswers("Soy una estudiante de Dartmouth.", "¿Porqué eres una estudiante de Dartmouth?", "I'm a student at Dartmouth", "Why are you a student at Dartmouth?")
printAnswers("Es que yo soy bastante desordenado.", "¿Porqué eres bastante desordenado?", "It's just that I'm fairly messy", "Why are you fairly messy?")

print("---------- 4: Family ----------\n")

printAnswers("A mi mamá le gustan las orquídeas.", "Cuéntame más de tu mamá.", "Mom likes orquids.", "Tell me more about your mom")
printAnswers("Porque mi papá prefiere los árboles.", "Cuéntame más de tu papá.", "Because my dad likes trees.", "Tell me more about your dad")
printAnswers("Porque mi mamá quiere que yo me vaya de la casa.", "Cuéntame más de tu mamá.", "Because my mom wants me to leave the house", "Tell me more about your mom")

print("---------- 5: Handling modal verbs and clitics ----------\n")

printAnswers("no quiero aprender a programar", "¿Porqué no quieres aprender a programar?", "i don't want to learn how to program", "Why don't you want to learn how to program?")
printAnswers("puedo comerme diez galletas.", "¿Porqué puedes comerte diez galletas?", "i can eat ten cookies", "Why can you eat ten cookies?")
printAnswers("No quiero irme de viaje!", "¿Porqué no quieres irte de viaje?", "I don't want to go on a trip!", "Why don't you want to go on a trip?")
printAnswers("Yo puedo caminar en la nieve.", "¿Porqué puedes caminar en la nieve?", "I can walk on the snow.", "Why can you walk on the snow?")
printAnswers("Ella dice que debo ordenar el cuarto.", "¿Porqué debes ordenar el cuarto?", "She says I need to tidy up the room.", "Why must you tidy up the room?")
printAnswers("Bueno. No sé. Me cuesta mucho. No puedo ser ordenado.", "¿Porqué no puedes ser ordenado?", "I mean, I dunno.... It's difficult. I can't be tidy", "Why can't you be tidy?")

print("---------- 6: Thoughts and hopes ----------\n")

printAnswers("Pienso que mis amigos también hacían eso.", "¿Porqué piensas eso?", "I think my friends did that too.", "Why do you think that?")
printAnswers("Yo espero graduarme el año próximo.", "¿Porqué esperas eso?", "I'm hoping to graduate next year.", "Why do you hope that?")
printAnswers("Pienso que todo empezó cuando fui a la playa por primera vez.", "¿Porqué piensas eso?", "I think it all started when I went to the beach for the first time", "Why do you think that?")

print("---------- 7: Asking for specific examples ----------\n")

printAnswers("Él siempre dice lo mismo.", "¿Puedes darme un ejemplo específico?", "He always says the same thing", "Can you give me a specific example?")
printAnswers("Mi hermano siempre se come las galletas.", "¿Puedes darme un ejemplo específico?", "My brother always eats the cookies", "Can you give me a specific example?")
printAnswers("Porque cuando era niño siempre me gustaba jugar en la naturaleza, donde todo es libre.", "¿Puedes darme un ejemplo específico?", "Because when I was a kid I always liked to play in nature, where everything is free", "Can you give me a specific example?")

print("---------- 8: Handling insults ----------\n")

printAnswers("No, ¡estúpida!", "¡Hey, sin insultos! Cálmate y cuéntame más.", "No, stupid!", "Hey, no insults! Calm down and tell me more.")
printAnswers("Eres una idiota.", "¡Hey, sin insultos! Cálmate y cuéntame más.", "You're an idiot.", "Hey, no insults! Calm down and tell me more.")

print("---------- 9: Generic reply ----------\n")

printAnswers("¡Porque me da la gana!", "Cuéntame más", "Because I don't wanna!", "Tell me more")