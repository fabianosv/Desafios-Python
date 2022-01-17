class Carro:
    def __init__(self, cor, modelo, marca, ano, placa):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.placa = placa

    def mudaCor(self, NovaCor):
        self.cor = NovaCor


class FuncoesCarro(Carro):
    #  def check_carro(self):
    def __init__(self, cor, modelo, marca, ano, placa):
        super().__init__(cor, modelo, marca, ano, placa)
        self.ligado = False
        self.v = 0
        self.velocidadeMax = 220.00
        self.marcha = 0

    def liga(self):
        if self.ligado is False:
            self.ligado = True
            print("Ligando Carro")
        else:
            return

    def desliga(self):
        if self.ligado is True:
            self.ligado = False
            print("Desligando Carro")
        else:
            return

    def acelera(self):
        if self.ligado is True:
            self.v += 10  # aumenta 10 km a cada chamada da funcão
            print("A velocidade é", self.v)
            if self.v > self.velocidadeMax:
                self.v = self.velocidadeMax
        else:
            return

    def freia(self):
        if self.ligado is True:  # verifica se o carro esta ligado
            if self.v > 0:  # verifica se o carro está em movimento
                self.v -= 10
                print("Freando:", "a velicidade é", self.v)
            else:
                return  # carro em ponto morto


    def meteMarcha(self):
        if self.ligado is True:
            if self.marcha == 0 or self.marcha < 6:
                self.marcha += 1
                print("Metendo a", self.marcha,  "marcha")
                self.acelera()
        else:
            return


    def tiraMarcha(self):
        if self.ligado is True:
            if self.marcha > 0:
                print("Tirando a", self.marcha, "marcha")
                self.marcha -= 1
                self.freia()
        else:
            return

    def neutro(self):
        if self.marcha > 0 and self.marcha <= 6:
            return self.marcha - self.marcha
        else:
            return 0

    def sair(self):
        if self.ligado is False:
            if self.marcha == 0: #verifica se esta em ponto morto
                self.liga()
                self.meteMarcha()
                #self.acelera()

            else:
                print("Coloque em ponto morto para ligar ligar o carro!")
                #self.tiraMarcha()
                self.marcha = self.neutro()
                self.sair()
        else:
            if self.marcha == 0 or self.marcha == 1:
                self.v = 0
                self.marcha = self.neutro()
                self.meteMarcha()
            #self.acelera()

    def mostraEstado(self):
        print("O carro está na", self.marcha, "marcha")

