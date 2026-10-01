def calcular_troca_oleo(odometro, ultima_troca, limite):
    percorrido = odometro - ultima_troca
    if percorrido >= limite:
        return "Troca de óleo atrasada em " + str(percorrido - limite) + " km"
    else:
        restante = limite - percorrido
        return "Faltam " + str(restante) + " km para a troca de óleo"

odometro_atual = float(input("Informe a quilometragem atual: "))
ultima_troca_km = float(input("Informe a quilometragem da última troca: "))
limite_oleo = float(input("Informe o limite do óleo (km): "))

resultado = calcular_troca_oleo(odometro_atual, ultima_troca_km, limite_oleo)
print(resultado)