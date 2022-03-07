import varModule

#FORMATTING


#BREAKLINE


def breakline():
    print("\n====================================================================================\n")


#INNER BREAKLINE


def inbreakline():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


#UI BREAKLINE


def uibreakline():
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")


#ERROR SIGNAL


def error():
    inbreakline()
    print("That does not seem to be a viable command. Please check your spelling.")
    varModule.lastError = False

def uiError():
    uibreakline()
    print("That does not seem to be a viable command. Please check your spelling.")
