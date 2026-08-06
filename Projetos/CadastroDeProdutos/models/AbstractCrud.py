import json
from abc import ABC

class AbstractCrud(ABC):
    def detalhar(self):
        return self.__dict__
    
    def inserir(self):
        lista = self.ler_arquivo()
        lista.append(self.detalhar())
        self.__salvar_arquivo(lista)

    def atualizar(self, item):
        lista = self.ler_arquivo()
        lista[item] = self.detalhar()
        self.__salvar_arquivo(lista)

    @classmethod
    def deletar(cls, item):
        lista = cls.ler_arquivo()
        del lista[item]
        with open(cls.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)
        
            print('Operação realizada com sucesso.')

    def __salvar_arquivo(self, lista):
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)

        print('Operação realizada com sucesso.')

    @classmethod
    def listar_todos(cls):
        lista = cls.ler_arquivo()

        for i, v in enumerate(lista):
            print(f"{i} - {v}")

    @classmethod
    def ler_arquivo(self, item = None):
        try:
            with open(self.arquivo) as file:
                lista = json.load(file)

            return lista[item] if isinstance(item, int) else lista
        except Exception:
            return []
