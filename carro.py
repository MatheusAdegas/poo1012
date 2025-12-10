class Carro:
  def __init__(self, velocidade_inicial):
    self.velocidade = velocidade_inicial
  
  def acelera(self):
    self.velocidade += 1
  
  def freia(self):
    self.velocidade -= 1
  
  def exibie_velocidade(self):
    print(f"Vel: {self.velocidade} km/h")