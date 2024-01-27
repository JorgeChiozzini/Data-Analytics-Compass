import hashlib

while True:
    # Recebe uma string via input
    input_string = input("Digite uma string para mascarar (ou 'exit' para sair): ")

    # Verifica se o usuário deseja sair
    if input_string.lower() == 'exit':
        break

    # Gera o hash SHA-1 da string
    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()

    # Imprime o hash em tela
    print(f"Hash SHA-1 da string '{input_string}': {sha1_hash}")
