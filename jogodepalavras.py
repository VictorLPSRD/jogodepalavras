palavra=input('Digite uma palavra secreta :') # Você vai digitar a palavra.

import os # importei o módulo os .

os.system('cls') # usei(cls) para não fica exibindo a palavra que você colocou ele vai limpa o terminal. 

palavra_secreta = palavra # a palavra fica salva nessa variavel.
letras_acertadas = '' # Para salva as letras acertadas e exibir.
numero_tentativas = 0 # numero de acertos começa com zero.

while True: # Crie um laço de repetição.
    letra_digitada = input('Digite uma letra: ') # pega a letra que o usuario digitou.
    numero_tentativas += 1 # A cada letra digitada vai adicionar um a numero_tentativas.

    if len(letra_digitada) > 1: # Se o usuario digita mais de uma letra .
        print('Digite apenas uma letra.') # Sera exibido isso.
        continue # ele volta ao começo do laço .

    if letra_digitada in palavra_secreta: # Se a letra_digitada estiver em palavra_digitada.
        letras_acertadas += letra_digitada # A cada letra_acertada ele adiciona a letra em letras_acertadas.

    palavra_formada = ''# Essa variavel serve para a palra_formada fica na horizontal e exibir ela de uma vez. 
    for letra_secreta in palavra_secreta: # Crie um for para pecore letra por letra.
        if letra_secreta in letras_acertadas: # Se a letr_secreta estiver em letras_acertadas.
            palavra_formada += letra_secreta  # Ele vai adicionar a letra em letras_secreta e exibir ela no lugar do asterisco(*).
        else: # Se não 
            palavra_formada += '*' # ele vai exibir o asterisco(*).

    print('Palavra formada:', palavra_formada) # fora do for ele vai exibir ou a letra ou asterisco(*).

    if palavra_formada == palavra_secreta: # Se palavra_formada for igual a palavra_secreta 
        os.system('clear')# Ele vai limpa o terminal.
        print('VOCÊ GANHOU!! PARABÉNS!') # Vai exibir isso.
        print('A palavra era', palavra_secreta) # Mostra a palrava_secreta .
        print('Tentativas:', numero_tentativas) # Vai mostra o numero de tentivas. 
        letras_acertadas = '' # vai zera as letras_acertadas.
        numero_tentativas = 0 # e zera numero de tentativas.
