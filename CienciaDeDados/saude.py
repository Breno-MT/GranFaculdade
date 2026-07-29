import numpy as np
import pandas as pd

class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

pacientes = {
    "paciente_1": Paciente('Maria', 20, 'F', 60, 1.66),
    "paciente_2": Paciente('Glória', 32, 'F', 49, 1.52),
    "paciente_3": Paciente('João', 55, 'M', 80, 1.88),
    "paciente_4": Paciente('Mateus', 70, 'M', 71, 1.74),
    "paciente_5": Paciente('Pedro', 43, 'M', 90, 1.55),
}

l_pacientes = [p.__dict__ for p in pacientes.values()]

df_pacientes = pd.DataFrame.from_records(l_pacientes, index=pacientes.keys())

df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis=1)

media = np.min(df_pacientes['IMC'])

sobrepeso = df_pacientes[df_pacientes['IMC'] > 25]

percentual = len(sobrepeso) / len(df_pacientes) * 100

