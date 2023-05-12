#Classe ônibus
class Onibus:

        def __init__(self, marca, modelo, poutronas):
            self.marca = marca
            self.modelo = modelo
            self.poutronas= poutronas

        def Mostrar_Marca:
            return (f'A marca do altomóvel é:{self.marca}')

        def Mostrar_Modelo:
            return (f'O modelo do veículo é:{self.modelo}')

        def Mostrar_poutronas:
            return (f'Quantidade de poutronas do ônibus é: {self.poutronas}')



