from carro import Carro
from carro import FuncoesCarro


car = Carro("verde", "ka", "Ford", "2019", "qnh-0987")
#car = Carro()
car1 = FuncoesCarro("verde", "ka", "Ford", "2019", "qnh-0987")

print(FuncoesCarro)

#car1.liga()
#car1.sair()
"""car1.meteMarcha()
car1.meteMarcha()"""
#car1.marcha = 4
car1.mostraEstado()
#car1.ligado = True
car1.sair()
car1.meteMarcha()
#car1.marcha = car1.neutro()
car1.mostraEstado()
car1.sair()
car1.mostraEstado()
"""car1.cor = "azul"

print("A cor do carro é", car.cor)
car1.mudaCor("amarelo")
print("A nova cor é", car1.cor)"""