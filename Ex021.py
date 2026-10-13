import pygame
pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((400, 300))
pygame.mixer.music.load('teste1.mp3')
pygame.mixer.music.play(0)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


