import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
import dados as dds

empresas = []

class usuario():
    def __init__ (self, escolha, saldo):
        self.escolha = escolha
        self.saldo = saldo
        self.acoes = 0

usuario1 = usuario(0, 5000)

class empresa():
    def __init__ (self, nome, nome_bolsa, data_inicio, data_fim, acoes):
        self.nome = nome
        self.nome_bolsa = nome_bolsa
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.datas = dds.puxar_dados(nome_bolsa,data_inicio,data_fim)[0]
        self.valores = dds.puxar_dados(nome_bolsa,data_inicio,data_fim)[1]
        self.acoes = acoes

empresas.append(empresa('google','googl','2020-11-11','2021-11-11',0))
print(empresas[0].data_fim)
empresas.append(empresa('apple','aapl','2021-11-11','2022-11-11',0))

x_values_ano = [0]*365
x_values_mes = [0]*30
y_values_ano = [0]*365
y_values_mes = [0]*30

# função para mostrar o histórico anual da empresa
def anual():
    if len(x_values_ano) > 366:
        print('vaca')
        for i in range (1,366):
            x_values_ano[-i] = (empresas[usuario1.escolha].valores[-i])
            y_values_ano[-i] = (empresas[usuario1.escolha].datas[-i])
    else:
        print('boi2')
        for i in range (1,(len(x_values_ano)+1)):
            x_values_ano[i] = (empresas[usuario1.escolha].valores[i])
            y_values_ano[i] = (empresas[usuario1.escolha].datas[i])

    plt.plot(x_values_ano)
    plt.show()
    return

# função para mostrar o histórico mensal da empresa
def mensal():
    for i in range (1,31):
        x_values_mes[-i] = (empresas[usuario1.escolha].valores[-i])
        y_values_mes[-i] = (empresas[usuario1.escolha].datas[-i])
    plt.plot(x_values_mes)
    plt.show()
    return

# função que cria a janela onde sera mostrada a empresa
def mostrar_empresa():
    def atualizar():
        empresas[usuario1.escolha].data_fim = str(dds.atualizar())
        empresas[usuario1.escolha].valores = dds.puxar_dados(empresas[usuario1.escolha].nome_bolsa, empresas[usuario1.escolha].data_inicio, empresas[usuario1.escolha].data_fim)[1]

    sec = tk.Toplevel(window, bg= 'grey13')
    sec.geometry('600x400')
    tk.Label(sec, text= 'nome: %s\nnome na bolsa: %s\nvalor mais recente da ação: %s\nvalor mais recente puxado em: %s\n você possui %s ações nessa empresa atualmente' % (empresas[usuario1.escolha].nome, empresas[usuario1.escolha].nome_bolsa, empresas[usuario1.escolha].valores[-1], empresas[usuario1.escolha].data_fim, empresas[usuario1.escolha].acoes), bg= 'grey13', fg = 'white').pack()
    tk.Button(sec, text= 'atualizar', command= atualizar, fg = 'white', bg = 'grey26').pack(pady=10)
    tk.Button(sec, text= 'voltar', command= sec.destroy, fg = 'white', bg = 'grey26').pack()

# função que mostra a tela onde sera escolhida uma empresa
def escolher_empresa():
    menu.pack_forget()
    tela_escolha.pack()

# função que mostra a tela onde será registrada uma empresa
def registrar_empresa():
    menu.pack_forget()
    tela_registrar.pack()

# função que cria uma janela onde são mostradas as empresas registradas
def lista_empresas():
    janela_empresas = tk.Toplevel(window, bg= 'grey13')
    janela_empresas.geometry('600x400')
    for i in range(len(empresas)):
        tk.Label(janela_empresas, text= 'Empresa: %s %s' % (i, empresas[i].nome), bg= 'grey13', fg = 'white').pack(pady = 10)
    tk.Button(janela_empresas, text= 'voltar', command= janela_empresas.destroy, fg = 'white', bg = 'grey26').pack()

# função que mostra a tela onde serão compradas as ações
def comprar_vender_acoes():
    menu.pack_forget()
    tela_compra.pack()

# função que mostra o perfil do usuário
def ver_perfil():
    janela_perfil = tk.Toplevel(window, bg= 'grey13')
    janela_perfil.geometry('600x400')
    tk.Label(janela_perfil, text= 'você tem um saldo de R$%s\nvocê possui %s ações atualmente' % (usuario1.saldo, usuario1.acoes), bg= 'grey13', fg = 'white').pack(pady=2)
    tk.Button(janela_perfil, text= 'voltar', command= janela_perfil.destroy, fg = 'white', bg = 'grey26').pack(pady= 10)

# função que registra a empresa
def pegar_valores():
    nome = entrada_nome.get()
    nome_bolsa = entrada_nome_bolsa.get()
    data_inicio = entrada_data_inicio.get()
    data_fim = entrada_data_fim.get()
    empresas.append(empresa(nome,nome_bolsa,data_inicio,data_fim,0))
    print(empresas[usuario1.escolha].nome)
    limpar()

# função que confirma a escolha de empresa do usuário
def confirmar_escolha():
    escolha = int(entrada_escolha.get())
    usuario1.escolha = escolha
    print(escolha)
    limpar()

# função que confirma a compra de ações de uma empresa
def confirmar_compra():
    compra = int(entrada_compra.get())
    valor_compra = empresas[usuario1.escolha].valores[-1] * compra
    if compra >= 0:
        empresas[usuario1.escolha].acoes += compra
        usuario1.acoes += compra
        usuario1.saldo -= valor_compra
        limpar()
    print(compra)

# função que confirma a venda de ações de uma empresa
def confirmar_venda():
    venda = int(entrada_compra.get())
    valor_venda = empresas[usuario1.escolha].valores[-1] * venda
    if venda >= 0 and venda <= empresas[usuario1.escolha].acoes:
        empresas[usuario1.escolha].acoes -= venda
        usuario1.acoes -= venda
        usuario1.saldo += valor_venda
        limpar()
    print(venda)

# função que limpa os valores entrados pelo usuário
def limpar():
    entrada_nome.delete(0, tk.END)
    entrada_nome_bolsa.delete(0, tk.END)
    entrada_data_inicio.delete(0, tk.END)
    entrada_data_fim.delete(0, tk.END)
    entrada_escolha.delete(0, tk.END)
    entrada_compra.delete(0, tk.END)

# função para voltar ao menu principal
def voltar():
    tela_registrar.pack_forget()
    tela_escolha.pack_forget()
    tela_compra.pack_forget()
    menu.pack()

# janela do programa
window = tk.Tk()
window.title('Simulador de mercado de ações')
window.geometry('600x400')
window.configure(bg= 'grey13')

# tela do menu principal
menu = tk.Frame(window)
menu.configure(bg= 'grey13')
menu.pack()
tk.Button(menu, text= 'histórico anual', command= anual, fg = 'white', bg = 'grey26').pack(pady=20)
tk.Button(menu, text= 'histórico mensal', command= mensal, fg = 'white', bg = 'grey26').pack()
tk.Button(menu, text= 'mostrar empresa', command= mostrar_empresa, fg = 'white', bg = 'grey26').pack(pady=20)
tk.Button(menu, text= 'registrar empresa', command= registrar_empresa, fg = 'white', bg = 'grey26').pack()
tk.Button(menu, text= 'escolher empresa', command= escolher_empresa, fg = 'white', bg = 'grey26').pack(pady= 20)
tk.Button(menu, text= 'lista de empresas', command= lista_empresas, fg = 'white', bg = 'grey26').pack()
tk.Button(menu, text= 'comprar/vender ações', command= comprar_vender_acoes, fg = 'white', bg = 'grey26').pack(pady= 20)
tk.Button(menu, text= 'perfil', command= ver_perfil, fg = 'white', bg = 'grey26').pack()

# tela para registrar a empresa
tela_registrar = tk.Frame(window, bg = 'grey13')
tk.Label(tela_registrar, text= 'Digite o nome da empresa:', fg = 'white', bg = 'grey13').pack()
entrada_nome = tk.Entry(tela_registrar)
entrada_nome.pack()
tk.Label(tela_registrar, text= 'Digite o nome da empresa na bolsa de valores:', fg = 'white', bg = 'grey13').pack()
entrada_nome_bolsa = tk.Entry(tela_registrar)
entrada_nome_bolsa.pack()
tk.Label(tela_registrar, text= 'Digite a data inicial (AAAA-MM-DD):', fg = 'white', bg = 'grey13').pack()
entrada_data_inicio = tk.Entry(tela_registrar)
entrada_data_inicio.pack()
tk.Label(tela_registrar, text= 'Digite a data final (AAAA-MM-DD):', fg = 'white', bg = 'grey13').pack()
entrada_data_fim = tk.Entry(tela_registrar)
entrada_data_fim.pack()
tk.Button(tela_registrar, text= 'confirmar', command= pegar_valores, fg = 'white', bg = 'grey26').pack(pady= 10)
tk.Button(tela_registrar, text= 'voltar', command= voltar, fg = 'white', bg = 'grey26').pack()

# tela para escolher a empresa
tela_escolha = tk.Frame(window, bg = 'grey13')
tk.Label(tela_escolha, text= 'entre com sua escolha (número):', fg = 'white', bg = 'grey13').pack()
entrada_escolha = tk.Entry(tela_escolha)
entrada_escolha.pack()
tk.Button(tela_escolha, text= 'confirmar', command= confirmar_escolha, fg = 'white', bg = 'grey26').pack(pady= 10)
tk.Button(tela_escolha, text= 'voltar', command= voltar, fg = 'white', bg = 'grey26').pack()

# tela para comprar ações
tela_compra = tk.Frame(window, bg = 'grey13')
tk.Label(tela_compra, text= 'entre com a quantidade de ações que deseja comprar ou vender:', fg = 'white', bg = 'grey13').pack()
entrada_compra = tk.Entry(tela_compra)
entrada_compra.pack()
tk.Button(tela_compra, text= 'comprar', command= confirmar_compra, fg = 'white', bg = 'grey26').pack(pady= 10)
tk.Button(tela_compra, text= 'vender', command= confirmar_venda, fg = 'white', bg = 'grey26').pack()
tk.Button(tela_compra, text= 'voltar', command= voltar, fg = 'white', bg = 'grey26').pack(pady= 10)

window.mainloop()