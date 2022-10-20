""" Skriv en funktion som returner olika texter beroende på
 vad för typ argumentet var och vilket värde

Om argumentet var ett heltal och hade värdet 42:
"Answer to the Ultimate Question of Life, the Universe, and Everything"

I övrigt om det var ett heltal:
"Det var ett heltal"

Om argumentet var ett flyttal och är under 0:
"Var inte så negativ"

I övrigt om det är ett flyttal:
"Det var ett flyttal"

Om argumentet var en boolean och hade värdet False:
"Lögnare!"

Om argumentet var en boolean och hade värdet True:
"Det var en boolean"

Om argumentet var en sträng och hade värdet "Hej!"
"Hej på dig!"

I övrigt om det är en sträng:
"Det var en sträng"
 """

from xmlrpc.client import boolean


def type_checking(tal):
    if type(tal) == int and tal == 42:
        return "Answer to the Ultimate Question of Life, the Universe, and Everything"
    
    elif type(tal) == int:
        return "Det var ett heltal"

    elif type(tal) == float and tal < 0:
        return "Var inte så negativ"

    elif type(tal) == float:
        return "Var inte så negativ"

    elif type(tal) == bool and tal == False:
        return "Lögnare!"

    elif type(tal) == bool and tal == True:
        return "Det var en boolean"

    elif type(tal) == str and tal == "Hej!":
        return "Hej på dig!"

    elif type(tal) == str:
        return "Det var en sträng"