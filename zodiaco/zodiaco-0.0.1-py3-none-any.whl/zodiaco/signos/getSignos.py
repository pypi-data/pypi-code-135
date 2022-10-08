from datetime import datetime as dt

def getSigno(data_nascimento):
    data_nascimento =  dt.strptime(data_nascimento, "%Y-%m-%d")
    dia_nascimento = data_nascimento.day
    mes_nascimento = data_nascimento.month
    signo = ""

    if (mes_nascimento == 1):
        if (dia_nascimento <= 20):
            signo = "Capricórnio"
        else:        
            signo = "Aquário"
    elif (mes_nascimento == 2):
        if (dia_nascimento <= 19):
            signo = "Aquário"
        else:
            signo = "Peixes"
    elif (mes_nascimento == 3):
        if (dia_nascimento <= 20):
            signo = "Peixes"
        else:
            signo = "Áries"
    elif (mes_nascimento == 4):
        if (dia_nascimento <= 20):
            signo = "Áries"
        else:        
            signo = "Touro"
    elif (mes_nascimento == 5):
        if (dia_nascimento <= 20):
            signo = "Touro"
        else:       
            signo = "Gêmeos"
    elif (mes_nascimento == 6):
        if (dia_nascimento <= 20):
            signo = "Gêmeos"
        else:       
            signo = "Câncer"
    elif (mes_nascimento == 7):
        if (dia_nascimento <= 22):
            signo = "Câncer"
        else:       
            signo = "Leão"
    elif (mes_nascimento == 8):
        if (dia_nascimento <= 22):
            signo = "Leão"
        else:       
            signo = "Virgem"
    elif (mes_nascimento == 9):
        if (dia_nascimento <= 22):
            signo = "Virgem"
        else:       
            signo = "Libra"
    elif (mes_nascimento == 10):
        if (dia_nascimento <= 22):
            signo = "Libra"
        else:       
            signo = "Escorpião"
    elif (mes_nascimento == 11):
        if (dia_nascimento <= 21):
            signo = "Escorpião"
        else:       
            signo = "Sagitário"
    elif (mes_nascimento == 11):
        if (dia_nascimento <= 21):
            signo = "Sagitário"
        else:       
            signo = "Capricórnio" 

    return signo

def getCor(signo):
    switcher = {
        "Áries": "Vermelho",
        "Touro": "Lilás",
        "Gêmeos": "Amarelo",
        "Câncer": "Branco",
        "Leão": "Laranja", 
        "Virgem": "Verde", 
        "Libra": "Rosa",
        "Escorpião": "Vinho",
        "Sagitário": "Violeta",
        "Capricórnio": "Preto",
        "Aquário": "Azul", 
        "Peixes":  "Roxo",   
    }
    return switcher.get(signo, "nothing")

def getNumeroSorte(signo):
    switcher = {
        "Áries": 10,
        "Touro": 3,
        "Gêmeos": 8,
        "Câncer": 1,
        "Leão": 6, 
        "Virgem": 4, 
        "Libra": 9,
        "Escorpião": 7,
        "Sagitário": 2,
        "Capricórnio": 5,
        "Aquário": 8, 
        "Peixes":  6,   
    }
    return switcher.get(signo, 0)