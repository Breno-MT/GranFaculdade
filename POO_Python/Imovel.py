class Categoria:
    def __init__(self, tipo = ''):
        self.tipo = tipo

    def taxaAgua(self, consumo):
        match self.tipo:
            case "Clínica": return consumo * 1
            case "Restaurante": return consumo * 2
            case "Hotel": return consumo * 2.5

class Imovel:
    imposto = 0.2

    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        self.categoria = Categoria()

    def __add__(self, other):
        soma_self = self.quartos + self.suites
        soma_other = other.quartos + other.suites

        return soma_self + soma_other

    def __gt__(self, other):
        soma_self = self.quartos + self.suites
        soma_other = other.quartos + other.suites

        return soma_self > soma_other
    
    def __lt__(self, other):
        soma_self = self.quartos + self.suites
        soma_other = other.quartos + other.suites

        return soma_self < soma_other
    
    def __str__(self):
        return str(self.__dict__)
    
    def detalhar(self):
        return self.__dict__
    
    def somarAposentos(self):
        return self.quartos + self.suites
    
    @staticmethod
    def metodoEstatico():
        print("Chamou um metodo estatico sem criar um Objeto")

    @classmethod
    def metodoClasse(cls):
        print("Chamou o metodo de classse que vê os atributos da classe: ", cls.imposto)

casarao = Imovel('Casarão', 4, 6)
mansao = Imovel('Mansão', 10, 12)

categoria = Categoria('Hotel')
hotel = Imovel('Hotel do Joãozinho', 0, 150)
hotel.categoria = categoria
print(hotel.categoria.taxaAgua(500))

# Imovel.metodoEstatico()
# Imovel.metodoClasse()
    
