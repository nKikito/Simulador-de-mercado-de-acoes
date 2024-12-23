import yfinance as yf
from datetime import datetime

def verificar_numero(numero):
    n = 0
    p = 0
    for i in numero:
        if i.isdigit():
            n += 1
        elif i == '.':
            p += 1
        else:
            return False
    # print(n, p, len(numero))
    if n  == len(numero) - 1 and p == 1 or n == len(numero):
        return True
    

def puxar_dados(empresa, data_inicio, data_fim):
    lista_datas = []
    lista_valores = []

    data_inicio = data_inicio.split("-")
    ano = data_inicio[0]
    mes = data_inicio[1]
    dia = data_inicio[2]
    dia2 = '28'
    ano2 = ano

    data_fim = data_fim.split("-")
    ano_fim = data_fim[0]
    mes_fim = data_fim[1]
    dia_fim = data_fim[2]

    while ano != ano_fim or mes != mes_fim:
        if mes not in ['09', '10', '11', '12']:
            mes2 = f"0{int(mes)+1}"
        elif mes == '12':
            mes2 = '01'
            ano2 = f"{int(ano)+1}"
        else:
            mes2 = f"{int(mes)+1}"

        if mes2 == mes_fim:
            dia2 = dia_fim 

        data = yf.download(empresa, start=f'{ano}-{mes}-{dia}', end=f'{ano2}-{mes2}-{dia2}')
        test1 = (str(data["Close"]).split())
        dia = '28'
       
    
        x = 5

        a = 3
 
        for i  in range(len(test1)):
            
            if x + 3 < len(test1):
                if verificar_numero(test1[x]):    
                    lista_valores.append(test1[x])
                    x += 3
            elif i == len(test1)-1:
                lista_valores.append(test1[-1])

            if a + 3 <= len(test1):
                lista_datas.append(test1[a])    
                a += 3


        for i in range(len(lista_valores)):
            lista_valores[i] = float(lista_valores[i])

        if mes not in ['09', '10', '11', '12']:
            mes = f"0{int(mes)+1}"
        elif mes == '12':
            mes = '01'
            ano = f"{int(ano)+1}"
        else:
            mes = f"{int(mes)+1}"

    return [lista_datas, lista_valores]

def atualizar():
    date = ((datetime.now()).strftime("%D")).split("/")
    ano_atual = f'20{date[2]}'
    mes_atual = date[0]
    dia_atual = date[1]
    return f"{ano_atual}-{mes_atual}-{dia_atual}"   

