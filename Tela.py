import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('LightBlue6')
        # layout
        layout = [ 
            [sg.Text('Cadastro cliente ISERVICE',font='Courier 24',justification= 'center',size=(50,0))],
            [sg.Text('Nome',size=(10,0)),sg.Input(size=(40,0),key='nome')],
            [sg.Text('Idade',size=(10,0)),sg.Input(size=(40,0),key='idade')],
            [sg.Text('endereço',size=(10,0)),sg.Input(size=(40,0),key='endereço'),sg.Text('numero',size=(5,0)),sg.Input(size=(10,0),key='numero'),sg.Text('referencia',size=(10,0)),sg.Input(size=(40,0),key='referencia')],
            [sg.Text('cpf',size=(10,0)),sg.Input(size=(30,0),key='cpf'),sg.Text('rg',size=(14,0)),sg.Input(size=(30,0),key='rg')],
            [sg.Text('Quais provedores de email são os seus?')],
            [sg.Checkbox('Gmeil',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Possui cartao')],
            [sg.Radio('Sim','cartoes',key='aceitacartão'),sg.Radio('Nao','cartoes',key='nãoaceitacartão')],
            [sg.Button('Enviar e visualize seus dados')],
            [sg.Output(size=(30,20))], #cria a box de saida dos dados na tela
        ]
        # janela
        self.janela = sg.Window('Dados do usuario').layout(layout)

        # Extrair os dados da tela  
        #self.button, self.values = janela.Read()   linha antiga da que se localiza abaixo do laço. laço esse que serve
        #para, ao invés de executar uma vez apenas o programa e logo fechar, entrar em um looping e permanecer aberto.

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            endereço = self.values['endereço']
            numero = self.values['numero']
            cpf = self.values['cpf']
            rg = self.values['rg']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_gmail = self.values['gmail']
            aceita_cartao = self.values['aceitacartão']
            nao_aceita_cartao = self.values['nãoaceitacartão']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'endereço: {endereço}')
            print(f'numero: {numero}')
            print(f'cpf: {cpf}')
            print(f'rg: {rg}')
            print(f'outlook: {aceita_outlook}')
            print(f'yahoo: {aceita_yahoo}')
            print(f'gmail: {aceita_gmail}')
            print(f'aceitacartão {aceita_cartao}')
            print(f'nãoaceitacartão {nao_aceita_cartao}')
            


tela = TelaPython()
tela.Iniciar()

#key funcionando para fixar na hora de rodar, o que voce escreveu na string
#