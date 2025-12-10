from carro import Carro

class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial):
    
    # Override the acelera method
    def acelera(self):
        self.velocidade += 5
        print("Aceleração de corrida; velocidade aumentou em 5")
        