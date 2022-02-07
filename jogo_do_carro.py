import pygame
pygame.init()

centro = 515
lateral = 300
velocidade = 10
y2 = -50
v2 = -20

fundo = pygame.image.load('pista_de_carro_01.png')
pista02 = pygame.image.load('pista_02.png')
pista03 = pygame.image.load('pista_02.png')
carro = pygame.image.load('foto_do_carro.png')
janela = pygame.display.set_mode((1075, 650))
pygame.display.set_caption("Smith's Car Game")

janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta  = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        lateral -= velocidade
    if comandos[pygame.K_DOWN]:
        lateral += velocidade
    if comandos[pygame.K_RIGHT]:
        centro += velocidade
    if comandos[pygame.K_LEFT]:
        centro -= velocidade
    y2 -= v2
    if (y2 >= 700):
        y2 = -70

    janela.blit(fundo,(0,0))
    janela.blit(pista02,(306,y2))
    janela.blit(pista03,(650, y2))
    janela.blit(carro,(centro,lateral))
    pygame.display.update()


pygame.quit()
