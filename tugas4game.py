# Part E
# Digunakan untuk mengambil library yang akan digunakan
import pygame
import sys
from pygame import display


WIDTH, HEIGHT = 620, 460 #mengatur panjang dan lebar dari kotak windows
TITLE = "Praktikum Game Development Pertemuan 4" # untuk menatur title dari windows
font_color = (240, 248, 254) #mengatur warna font


pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT)) #membuat deklarasi dari pengaturan panjang dan lebar windows agar mudah dalam penerapannya
background = pygame.image.load("assets/sky.jpg") #mengatur background yang ingin ditampilkan

pygame.display.set_caption(TITLE) #mendeklarasikan title
font = pygame.font.SysFont("America", 28) #mengatur macam dan besar font
text = font.render("Linda Ramawati", True, font_color) #mengatur text apa yang akan diinputkan, kondisi True disini untuk bisa mewujudkan hasil title tersebut, dan juga warna dari font tersebut
clock = pygame.time.Clock() #pengaturan waktu pergerakan dari karakter

# Part D
#membuat kelas Player yang didalamnya mengatur sumbu x dan ya. reaksi untuk bertemuan dari sumbu x dan y.warna dari player/karakter. pergerakan player
#sendiri berkondisi False agar si player tidak berjalan sendiri tanpa adanya kontrol dari pemain. dan kecepatan.
class Player: 
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    # Part F
    # ini untuk mengatur dari player/ gambaran itu sendiri. agar bisa dideklarasikan lagi. maka dijadikan satu variabel yaitu draw yang berisi warna player,reaksi player
    #panjang lebar windows
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    # Part A
    # bagian ini digunakan menindaklanjutan dari kelas player yang si player tidak bisa bergerak sendiri maka di part ini akan diatur semaksimal mungkin

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


# Part B
#player ini untuk deklarasi baru 
player = Player(WIDTH/2, HEIGHT/2)


# Digunakan sebagai perulangan/kondisi 
while True:
    for event in pygame.event.get():
        #mengatur keluar game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # mengatur keyboard agar bisa berjalan
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        # pengaturan keyboard yang tidak bisa berjalan bersamaan
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

        # batasan akan player
        if player.x > 580:
            player.x = 580
        if player.x < 30:
            player.x = 10
        if player.y > 420:
            player.y = 420
        if player.y < 30:
            player.y = 10

    # Part C
    # digunakan untuk merealisasikan background,text, dll
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    win.blit(text, (220, 0))
    player.draw(win)

    # update terbaru
    player.update()
    pygame.display.flip()

    clock.tick(120)
