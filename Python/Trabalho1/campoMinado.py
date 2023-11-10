import pygame
import sys
import random

# Configurações do jogo
largura = 10
altura = 10
tamanho_celula = 40
largura_janela = largura * tamanho_celula
altura_janela = altura * tamanho_celula
bombas = largura * altura // 10  # 10% das células com bombas

# Cores
BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)
VERMELHO = (255, 0, 0)
VERDE_CLARO = (0, 255, 0)

# Inicialização do Pygame
pygame.init()

# Criação da janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Campo Minado")

# Função para criar o campo minado com bombas
def criaCampo():
    campo = [[' ' for _ in range(largura)] for _ in range(altura)]

    for _ in range(bombas):
        x, y = random.randint(0, largura - 1), random.randint(0, altura - 1)
        while campo[y][x] == 'B':
            x, y = random.randint(0, largura - 1), random.randint(0, altura - 1)
        campo[y][x] = 'B'

    return campo

campo = criaCampo()
celulas_reveladas = [[False for _ in range(largura)] for _ in range(altura)]

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            coluna = x // tamanho_celula
            linha = y // tamanho_celula
            if not celulas_reveladas[linha][coluna]:
                celulas_reveladas[linha][coluna] = True
                if campo[linha][coluna] == 'B':
                    # O jogo acaba, o jogador perdeu
                    print("Você perdeu!")
                else:
                    # Atualize a interface gráfica
                    pygame.draw.rect(janela, VERDE_CLARO, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
                    if campo[linha][coluna] != ' ':
                        fonte = pygame.font.Font(None, 36)
                        texto = fonte.render(campo[linha][coluna], True, VERMELHO)
                        janela.blit(texto, (coluna * tamanho_celula + 10, linha * tamanho_celula + 10))
                    else:
                        # Mostrar números nas células adjacentes
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                nova_linha = linha + i
                                nova_coluna = coluna + j
                                if 0 <= nova_linha < altura and 0 <= nova_coluna < largura:
                                    if campo[nova_linha][nova_coluna] == 'B':
                                        continue
                                    numero_bombas = sum(1 for dx in range(-1, 2) for dy in range(-1, 2) if 0 <= nova_linha + dy < altura and 0 <= nova_coluna + dx < largura and campo[nova_linha + dy][nova_coluna + dx] == 'B')
                                    if numero_bombas > 0:
                                        pygame.draw.rect(janela, VERDE_CLARO, (nova_coluna * tamanho_celula, nova_linha * tamanho_celula, tamanho_celula, tamanho_celula))
                                        fonte = pygame.font.Font(None, 36)
                                        texto = fonte.render(str(numero_bombas), True, VERMELHO)
                                        janela.blit(texto, (nova_coluna * tamanho_celula + 10, nova_linha * tamanho_celula + 10))
    
    pygame.display.flip()
