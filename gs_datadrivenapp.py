
#  GS 2026.1 - Building Data Driven Applications
#  Eduardo Bambulim 1TSCPV FIAP
# Flavio Junior Carvalho 1TSCPV FIAP



tipos_eventos  = []
paises         = []
regioes        = []
cidades        = []
areas_afetadas = []
intensidades   = []
ocorrencias    = []


quantidade = 0
while quantidade <= 0:
    try:
        quantidade = int(input("Insira a quantidade de eventos: "))
        if quantidade <= 0:
            print("    A quantidade deve ser maior que zero. Tente novamente.")
    except ValueError:
        print("    Valor inválido. Digite um número inteiro.")


for i in range(1, quantidade + 1):
    print(f"\n--- Evento {i} ---")

   
    tipo = input("Tipo: ").strip()
    while not tipo:
        print("    O tipo não pode estar vazio.")
        tipo = input("Tipo: ").strip()
    tipos_eventos.append(tipo)

   
    pais = input("País: ").strip()
    while not pais:
        print("    O país não pode estar vazio.")
        pais = input("País: ").strip()
    paises.append(pais)

    
    regiao = input("Região: ").strip()
    while not regiao:
        print("    A região não pode estar vazia.")
        regiao = input("Região: ").strip()
    regioes.append(regiao)

    
    cidade = input("Cidade: ").strip()
    while not cidade:
        print("    A cidade não pode estar vazia.")
        cidade = input("Cidade: ").strip()
    cidades.append(cidade)

    
    area = 0.0
    while area <= 0:
        try:
            area = float(input("Área (km²): "))
            if area <= 0:
                print("    A área deve ser maior que zero.")
        except ValueError:
            print("    Valor inválido. Digite um número.")
    areas_afetadas.append(area)

   
    intensidade = 0
    while intensidade < 1 or intensidade > 10:
        try:
            intensidade = int(input("Intensidade (1 a 10): "))
            if intensidade < 1 or intensidade > 10:
                print("    A intensidade deve estar entre 1 e 10.")
        except ValueError:
            print("    Valor inválido. Digite um número inteiro entre 1 e 10.")
    intensidades.append(intensidade)

   
    num_ocorrencias = 0
    while num_ocorrencias < 1:
        try:
            num_ocorrencias = int(input("Ocorrências: "))
            if num_ocorrencias < 1:
                print("    O número de ocorrências deve ser pelo menos 1.")
        except ValueError:
            print("    Valor inválido. Digite um número inteiro.")
    ocorrencias.append(num_ocorrencias)


total_eventos = len(tipos_eventos)


soma_areas = 0.0
for area in areas_afetadas:
    soma_areas += area


soma_intensidades = 0
for intens in intensidades:
    soma_intensidades += intens
media_intensidade = soma_intensidades / total_eventos


indice_maior_area = areas_afetadas.index(max(areas_afetadas))


indice_mais_ocorrencias = ocorrencias.index(max(ocorrencias))
regiao_mais_ocorrencias = regioes[indice_mais_ocorrencias]


soma_densidades = 0.0
for j in range(total_eventos):
    soma_densidades += ocorrencias[j] / areas_afetadas[j]
densidade_media = soma_densidades / total_eventos


eventos_acima_media = 0
for intens in intensidades:
    if intens > media_intensidade:
        eventos_acima_media += 1


indice_critico = 0
for j in range(1, total_eventos):
    if intensidades[j] > intensidades[indice_critico]:
        indice_critico = j
    elif intensidades[j] == intensidades[indice_critico]:
        if areas_afetadas[j] > areas_afetadas[indice_critico]:
            indice_critico = j



print("\n========================================")
print("        RELATÓRIO DE ANÁLISE")
print("========================================")
print(f"Total de eventos registrados: {total_eventos}")
print("----------------------------------------")
print("Resumo Geral")
print("----------------------------------------")
print(f"Área total afetada: {soma_areas:.0f} km²")
print(f"Média de intensidade: {media_intensidade:.1f}")
print("----------------------------------------")
print("Análises")
print("----------------------------------------")
print(f"Região com maior número de ocorrências: {regiao_mais_ocorrencias}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")
print("----------------------------------------")
print("Evento Mais Crítico")
print("----------------------------------------")
print(f"Tipo: {tipos_eventos[indice_critico]}")
print(f"Local: {cidades[indice_critico]}, {regioes[indice_critico]}, {paises[indice_critico]}")
print(f"Intensidade: {intensidades[indice_critico]}")
print(f"Área afetada: {areas_afetadas[indice_critico]:.0f} km²")
print("========================================")
print(f"Total de desastres registrados: {total_eventos}")
