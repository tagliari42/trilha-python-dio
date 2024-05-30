salario = 2000


def salario_bonus(bonus):
    global salario

    lista_auxiliar = lista.copy()
    lista_auxiliar.append(2)
    print(f"lista auxiliar={lista_auxiliar}")

    salario += bonus
    return salario


lista = [1]
salario_com_bonus = salario_bonus(500)  # 2500
print(salario_com_bonus)
print(lista)