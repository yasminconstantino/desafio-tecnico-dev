'''
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
'''

def contar_letras_a(texto):
    # iniciamos um contador em 0, para contar quantas vezes a letra a irá aparecer
    contador = 0
    
    # conversão da string para minusculo, para fazer a contagem das letras a
    texto = texto.lower()
    
    # percorrer a string
    for caractere in texto:
        if caractere == 'a':
            contador += 1
    
    # retornar valor atual do contador
    return contador

# lê a string do usuario
entrada = input("Digite uma string: ")

# chamada da função
ocorrencias = contar_letras_a(entrada)

# verificar se existe a ou não, para direcionar a saida correta
if ocorrencias > 0:
    print(f"A letra 'a' aparece {ocorrencias} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
