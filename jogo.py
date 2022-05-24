import pygame , sys , os
from pygame.constants import K_ESCAPE, KEYDOWN

import sys
from pygame.locals import *
import random
from words import word_list

# Largura em pixeis
SCREEN_WIDTH = 900
# Altura em pixeis
SCREEN_HEIGHT = 1000

# Inicia a PYGAME
pygame.init()

# Tamanho define o tamanho do display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Titulo da pagina
pygame.display.set_caption('Simple Games')

# Carrega as imagens do menu (botões)
start_img = pygame.image.load(os.path.join('Img','Play.png')).convert_alpha()
exit_img = pygame.image.load(os.path.join('Img','Exit.png')).convert_alpha()
logo = pygame.image.load(os.path.join('Img','Logo.png')).convert_alpha()



class Button():  
    def __init__(self, x , y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action =True 

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image,(self.rect.x, self.rect.y))

        return action

def open_menu():
    
    run = True

    start_button = Button(315, 531.25, start_img, 0.25)
    exit_button = Button(315, 687.5, exit_img, 0.25)
    logo_button = Button(112.5, -61.25, logo, 0.625)

    while run:

        screen.fill((202, 228, 241))

        if start_button.draw() == True:
            games_menu()
        if exit_button.draw() ==  True:
            pygame.quit()
        if logo_button.draw() == True:
            eegg()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        
        pygame.display.update()

def games_menu():
    
    def jogo1txt():
        font = pygame.font.Font('Img\Berlin-sans-fb-demi-bold.ttf', 50)
        msg_screen = font.render('Jogos:', True, (255,145,76))
        screen.blit(msg_screen, [380, 15])

    menugames = True
    forcabtt = pygame.image.load(os.path.join('Img','Forcabtt.png')).convert_alpha()
    forca_button = Button(315, 131.25, forcabtt, 0.25)

    while menugames:

        screen.fill((202, 228, 241))

        jogo1txt()

        if forca_button.draw() == True:
            forca()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menugames = False
        
        pygame.display.update()

def eegg():
    
    eegg = True

    def eeggtext():
        font = pygame.font.Font('Img\Berlin-sans-fb-demi-bold.ttf', 40)
        credito = font.render('Creditos:', True, (0,0,0))
        Visual = font.render('• Artes visuais: @viniiid', True, (0,0,0))
        Desenvolvimento = font.render('• Criacao e dev.: @felpsds', True, (0,0,0))
        screen.blit(credito, [100, 100])
        screen.blit(Visual, [150, 150])
        screen.blit(Desenvolvimento, [150, 200])


    
    
    while eegg:

        screen.fill((202, 228, 241))

        eeggtext()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    eegg = False
        
        pygame.display.update()
        
# Começa o menu do jogo da forca
def forca():
    # Função que pega a palavra
    def get_word():
        # Palavra aleatória da lista
        word = random.choice(word_list)
        # Retorna a palavra em maúisculo.
        return word.upper()

    def draw_btns(BUTTONS):
        for button,letter in BUTTONS:
            btn_text = btn_font.render(letter, True, BLACK)
            btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
            pygame.draw.rect(screen, BLACK, button, 2)
            screen.blit(btn_text, btn_text_rect)


    def display_guess():
        display_word = ''

        for letter in WORD:
            if letter in GUESSED:
                display_word += f"{letter} "
            else:
                display_word += "_ "

        text = letter_font.render(display_word, True, BLACK)
        screen.blit(text, (250, 700))


    pygame.init()
    WIDTH, HEIGHT = 900, 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Games")

    game_over = False

    # colors
    FUNDO = (202, 228, 241)
    BLACK = (0,0,0)

    # Images
    IMAGES = []
    hangman_satus = 0

    for i in range(7):
        #Para rodar o jogo digite o caminho das imagens aqui! Siga o exemplo colocado, o nome final deve ser {i}.png
        image = pygame.image.load(f"C:/Users/Nomeusuario/Desktop/Jogo/Img/Sprites/{i}.png") 
        image_copy = image.copy()
        image_copy = pygame.transform.scale(image, (450, 450))
        IMAGES.append(image_copy)


    # Botões 
    ROWS = 2
    COLS = 13
    GAP = 20
    SIZE = 45
    BOXES = []

    for row in range(ROWS):
        for col in range(COLS):
            x = ((GAP * col) + GAP) + (SIZE * col) + 20
            y = ((GAP * row) + GAP) + (SIZE * row) + 800
            box = pygame.Rect(x,y,SIZE,SIZE)
            BOXES.append(box)

    A = 65
    BUTTONS = []

    for ind, box in enumerate(BOXES):
        letter = chr(A+ind)
        button = ([box, letter])
        BUTTONS.append(button)

    # Fonts
    btn_font = pygame.font.Font('Img\Berlin-sans-fb-demi-bold.ttf', 30)
    letter_font = pygame.font.Font('Img\Berlin-sans-fb-demi-bold.ttf', 60)
    game_font = pygame.font.Font('Img\Berlin-sans-fb-demi-bold.ttf', 80)


    # Word
    WORD = get_word()
    GUESSED = []

    # Title
    title = "Jogo da Forca"
    title_text = game_font.render(title, True, (255,145,76))
    title_text_rect = title_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+10))

    while True:
        print(WORD)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                clicked_pos = event.pos

                for button, letter in BUTTONS:
                    if button.collidepoint(clicked_pos):
                        GUESSED.append(letter)

                        if letter not in WORD:
                            hangman_satus += 1

                        if hangman_satus == 6:
                            game_over = True

                        BUTTONS.remove([button, letter])

        screen.fill(FUNDO)
        screen.blit(IMAGES[hangman_satus], (WIDTH//2 - 200,200))
        screen.blit(title_text, title_text_rect)
        draw_btns(BUTTONS)
        display_guess()

        won = True

        for letter in WORD:
            if letter not in GUESSED:
                won = False

        if won:
            game_over = True
            display_text = 'Voce Ganhou !!!'
            COLOR = (0,255,0)
        else:
            display_text = 'Voce Perdeu !!!'
            COLOR = (255,0,0)

            pygame.display.update()

        if game_over:
            screen.fill(FUNDO)
            game_over_text = game_font.render(display_text, True, COLOR)
            game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2 +200))
            screen.blit(game_over_text, game_over_text_rect)

            if won:
                final = pygame.image.load(os.path.join('Img','Sprites','Feliz.png'))
                final_copy = final.copy()
                final_copy = pygame.transform.scale(final, (450, 450))
                screen.blit(final_copy, (WIDTH//2 - 200,200))

            else:
                final = pygame.image.load(os.path.join('Img','Sprites','Final.png'))
                final_copy = final.copy()
                final_copy = pygame.transform.scale(final, (450, 450))
                screen.blit(final_copy, (WIDTH//2 - 200,200))
            
            pygame.display.update()
            pygame.time.delay(3000)

            
            
open_menu()
