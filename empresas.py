empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]
empresa5 = [1400, 1750, 2000, 4500, 5900]

def calcular_estatisticas(salarios):
    media = statistics.mean(salarios)
    moda = statistics.mode(salarios)
    mediana = statistics.median(salarios)
    desvio_padrao = statistics.stdev(salarios)
    
    return media, moda, mediana, desvio_padrao
import statistics

def calcular_estatisticas(salarios):
    media = statistics.mean(salarios)
    moda = statistics.mode(salarios)
    mediana = statistics.median(salarios)
    desvio_padrao = statistics.stdev(salarios)
    
    return media, moda, mediana, desvio_padrao

# Dados das empresas
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]
empresa5 = [1400, 1750, 2000, 4500, 5900]

# Calculando estatísticas para cada empresa
media1, moda1, mediana1, desvio_padrao1 = calcular_estatisticas(empresa1)
media2, moda2, mediana2, desvio_padrao2 = calcular_estatisticas(empresa2)
media3, moda3, mediana3, desvio_padrao3 = calcular_estatisticas(empresa3)
media4, moda4, mediana4, desvio_padrao4 = calcular_estatisticas(empresa4)
media5, moda5, mediana5, desvio_padrao5 = calcular_estatisticas(empresa5)

print('Empresa1')
print(f'Média: {media1}, Moda: {moda1}, Mediana: {mediana1}, Desvio Padrão: {desvio_padrao1}')
print()
print("Empresa2")
print(f'Média: {media2},  Moda: {moda2}, Mediana: {mediana2}, Desvio Padrão: {desvio_padrao2}')
print()
print("Empresa3")
print(f'Média: {media3},  Moda: {moda3}, Mediana: {mediana3}, Desvio Padrão: {desvio_padrao3}')
print() 
print("Empresa4")
print(f"Média: {media4},  Moda: {moda4},  Mediana: {mediana4},Desvio Padrão:  {desvio_padrao4} ")
print()
print("Empresa5")
print(f'Média: {media5},  Moda: {moda5},  Mediana: {mediana5},Desvio Padrão:  {desvio_padrao5} ')
print()









# #Adicionar comentários:  justifique sua escolha;

# # Qual empresa escolheria? Eu escolheria a Empresa número 2
# Porquê? A Empresa 2 parece uma boa escolha por conta da base na média mais alta
# O que você entendeu do desvio padrão, média, moda, mediana, amplitude,  variância dessa empresa?
#  A média é de 4200, o que representa o valor médio das observações.
#  Desvio Padrão: O desvio padrão é aproximadamente 1723.8, indicando que os valores têm uma dispersão moderada em torno da média.
#  Mediana: A mediana é 4000, o que indica que metade dos valores estão abaixo de 4000 e metade acima.
#  Moda: Não há moda clara, pois nenhum valor se repete.
#  Amplitude: A amplitude é 5000, mostrando a diferença entre o maior e o menor valor.