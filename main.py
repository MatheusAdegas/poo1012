from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_corrida import CarroCorrida

def test_drive(carro):
    print(f"\nTestando {carro.__class__.__name__}:")
    carro.acelera()
    carro.exibie_velocidade()

if __name__ == "__main__":
    # testando carroInteligente
    carro_inteligente = CarroInteligente(10)
    print("Carro inteligente: ")
    carro_inteligente.acelera()
    carro_inteligente.exibie_velocidade()
    carro_inteligente.estaciona()
    test_drive(carro_inteligente)
    print()

    # testando carroEsportivo
    carro_inteligente = CarroInteligente(10)
    print("Carro esportivo: ")
    carro_esportivo.turbo()
    carro_esportivo.exibie_velocidade()
    carro_esportivo.freia()
    carro_esportivo.exibie_velocidade()
    test_drive(carro_inteligente)
    print()

    # testando carro de corrida
    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)
    