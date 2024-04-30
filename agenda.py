agenda_telefonica = {
    'Hannah': '12-99771-9890',
    'Fernando': '12-99661-9810',
    'Lisandra': '12-91911-1221',
    'Luisa': '12-92331-1221',
    'Gustavo': '12-91111-1721',
    'Noah': '12-91911-1331',
}

def encontrar_numero(nome):
    return agenda_telefonica.get(nome, "Nome não localizado")

nome = 'Fernando'
print(encontrar_numero(nome))


def encontrar_dono(numero):
    for nome, num in agenda_telefonica.items():
        if num == numero:
            return nome

numero = '12-91911-1331'
print(encontrar_dono(numero))


def ler_numero_agenda():
    for nome, num in agenda_telefonica.items():
        print(f"{nome}: {num}")

ler_numero_agenda()



def ler_numero_nomes_L():
    for nome, num in agenda_telefonica.items():
        if nome.startswith('L'):
            print(f"{nome}: {num}")

ler_numero_nomes_L()
