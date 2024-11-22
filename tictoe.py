# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

# Função para verificar se alguém ganhou
def verificar_vitoria(tabuleiro):
    # Linhas, colunas e diagonais para vitória
    combinacoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    
    for combinacao in combinacoes_vitoria:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] and tabuleiro[combinacao[0]] != ' ':
            return True
    return False

# Função para verificar se o jogo terminou em empate
def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

# Função principal para jogar
def jogar():
    tabuleiro = [' '] * 9  # Tabuleiro inicial
    jogador_atual = 'X'  # Jogador inicial
    while True:
        imprimir_tabuleiro(tabuleiro)
        try:
            # Solicitar ao jogador a posição onde quer jogar
            posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição de 1 a 9: ")) - 1
            if tabuleiro[posicao] != ' ':
                print("Essa posição já está ocupada. Tente outra.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Digite um número entre 1 e 9.")
            continue
        
        # Colocar o símbolo do jogador na posição escolhida
        tabuleiro[posicao] = jogador_atual
        
        # Verificar se alguém venceu
        if verificar_vitoria(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        
        # Verificar se houve empate
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break
        
        # Trocar o jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Iniciar o jogo
if __name__ == "__main__":
    jogar()