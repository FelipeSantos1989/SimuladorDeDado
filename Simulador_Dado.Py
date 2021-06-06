#Simulador de dado
#Simular o uso de um dado, gerando um valor de 1 ate 6
import random 

class SimuladorDeDado:
    def _init_ (self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'você gostaria de gerar um novo valor para o dado'

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos a sua participação')
            else:
                print('Favort digitar sim ou nao')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    def GerarValorDoDado(self):
        print(random.rendint(self.valor_minimo,self.valor_maximo))
simulador = SimuladorDeDado()
simulador.Iniciar()