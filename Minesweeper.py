#!/usr/bin/python3
"""Minesweeper"""

import random
import pygame

pygame.init()

name = input("Enter your name: ")

mine = pygame.image.load("/Users/sherryzhang/Desktop/Minesweeper/Images/mines.png")
mine_r = pygame.image.load("/Users/sherryzhang/Desktop/Minesweeper/Images/mine_r.jpg")

green = (193, 243, 186)
white = (255, 255, 255)
black = (0, 0, 0)

width, height = 603, 703
screen = pygame.display.set_mode((width, height))
screen.fill(white)

pygame.display.set_caption("Minesweeper")

def mines(x, y):
    """Place Mines"""
    bombs = 0
    array = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for i in range(9):
        for j in range(9):
            score = random.randint(0, 10)
            if score == 0 or score == 1:
                array[i][j] = 9
                bombs += 1
    
    for f in range(x-1, x+2):
        for g in range(y-1, y+2):
            if array[f][g] == 9:
                bombs -= 1
            if 0 <= f <= 8 and 0 <= g <= 8:
                array[f][g] = 0

    array[x][y] = 0

    for i in range(9):
        for j in range(9):
            if array[i][j] != 9:
                count = 0
                for f in range(i-1, i+2):
                    for g in range(j-1, j+2):
                        if 0 <= f <= 8 and 0 <= g <= 8:
                            if array[f][g] == 9:
                                count += 1
                array[i][j] = count
    n_bombs = 81 - bombs
    return array, n_bombs

class grid():
    """Create Grid"""
    def __init__(self, i, j, x, y, w, h, screen):
        self.rect = pygame.Rect(x, y, w, h)
        self.txt_surface = ""
        self.i = i
        self.j = j
        self.status = 0
        self.color = green
        self.color_o = white
        self.txt_color = white
        self.txt_bg_color = (200, 200, 200)
        self.mine_color = (255, 0, 0)
        self.center = [x + w/2, y + h/2]
        self.screen = screen
        self.zero_looped = 0
        self.open = 0
    def drawgrid(self):
        """Draw Grid"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color_o, self.rect, 2)

    def drawtxt(self):
        """Draw Text"""
        pygame.draw.rect(self.screen, self.txt_bg_color, self.rect)
        if matrix[self.i][self.j] == 0:
            self.txt_surface = font.render(" ", True, self.txt_color)
        else:
            self.txt_surface = font.render(str(matrix[self.i][self.j]), True, self.txt_color)
        self.screen.blit(self.txt_surface, (self.rect.x+21, self.rect.y+15))

    def drawmine(self):
        """Draw Mines"""
        pygame.draw.circle(self.screen, self.mine_color, self.center, 15)

font = pygame.font.Font('freesansbold.ttf', 42)
text = font.render('RESET', True, black)
text_rect = pygame.draw.rect(screen, white, (0, 603, 106, 32))
screen.blit(text, (0, 603))

mine_squares = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for i in range(9):
    for j in range(9):
        x = i * 67
        y = j * 67
        mine_squares[i][j] = grid(i, j, x, y, 67, 67, screen)
        mine_squares[i][j].drawgrid()

zero_status = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def explode(i, j):
    """EXPLODE"""
    screen.blit(mine_r, (i * 67, j * 67))

def open_clicked(i, j):
    """Open Squares"""
    if matrix[i][j] == 9:
        explode(i, j)
        return
    else:
        mine_squares[i][j].drawtxt()
        mine_squares[i][j].status = 2
        mine_squares[i][j].open = 1

def open_zero(i, j):
    """Open Zeros"""
    mine_squares[i][j].zero_looped = 1
    for m in range(i-1, i+2):
        for n in range(j-1, j+2):
            if 0 <= m <= 8 and 0 <= n <= 8:
                mine_squares[m][n].drawtxt()
                mine_squares[m][n].status = 2
                mine_squares[m][n].open = 1
    for m in range(i-1, i+2):
        for n in range(j-1, j+2):
            if 0 <= m <= 8 and 0 <= n <= 8:
                if matrix[m][n] == 0 and mine_squares[m][n].zero_looped == 0:
                    open_zero(m, n)
                    mine_squares[i][j].status = 2
                    mine_squares[m][n].open = 1

def show():
    """Show Mines"""
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 9:
                screen.blit(mine, (i * 67, j * 67))

def red():
    """Show Bombs"""
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 9:
                pygame.draw.rect(screen, (255, 0, 0), (i*67, j*67, 67, 67))

end_game = 0
timer_switch = 0
end_time = 0
start_time = 0
click = 0
n_bombs = 2
while True:
    mouse = pygame.mouse.get_pos()
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()

    if end_game == 1:
        for event in pygame.event.get():
            if left_pressed:
                if text_rect.collidepoint(mouse):
                    for i in range(9):
                        for j in range(9):
                            x = i * 67
                            y = j * 67
                            mine_squares[i][j] = grid(i, j, x, y, 67, 67, screen)
                            mine_squares[i][j].drawgrid()
                    click = 0
                    end_game = 0
                    start_time = 0
                    end_time = 0
                    timer_switch = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
    else:
        for event in pygame.event.get():
            if left_pressed:
                for i in range(9):
                    for j in range(9):
                        if mine_squares[i][j].rect.collidepoint(mouse):
                            if click == 0:
                                matrix, n_bombs = mines(i, j)
                                open_zero(i, j)
                                #red()
                                start_time = pygame.time.get_ticks()
                                click = 1
                            elif click == 1:
                                if matrix[i][j] == 9:
                                    show()
                                    explode(i, j)
                                    text = font.render('RIP.', True, (187, 183, 183))
                                    screen.blit(text, (0, 0))
                                    end_game = 1
                                elif matrix[i][j] == 0:
                                    open_zero(i, j)
                                    mine_squares[i][j].status = 2
                                else:
                                    open_clicked(i, j)
                    if text_rect.collidepoint(mouse):
                        for i in range(9):
                            for j in range(9):
                                x = i * 67
                                y = j * 67
                                mine_squares[i][j] = grid(i, j, x, y, 67, 67, screen)
                                mine_squares[i][j].drawgrid()
                        click = 0
                        end_game = 0
                        start_time = 0
                        end_time = 0
                        timer_swtich = 0

            if right_pressed:
                for i in range(9):
                    for j in range(9):
                        if mine_squares[i][j].rect.collidepoint(mouse):
                            if mine_squares[i][j].open != 1:
                                if zero_status[i][j] == 0:
                                    mine_squares[i][j].status = 1
                                    mine_squares[i][j].mine_color = (255, 187, 187)
                                    mine_squares[i][j].drawmine()
                                    zero_status[i][j] = 1
                                elif zero_status[i][j] == 1:
                                    pygame.draw.rect(screen, green, (i*67, j * 67, 67, 67))
                                    pygame.draw.rect(screen, white, (i*67, j * 67, 67, 67), 2)
                                    zero_status[i][j] = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

    open_num = 0
    for i in range (9):
        for j in range(9):
            if mine_squares[i][j].status == 2:
                open_num += 1
    
    if open_num == n_bombs:
        time = (pygame.time.get_ticks() - start_time)/1000
        end_game = 1
        win = 0
        font = pygame.font.Font('freesansbold.ttf', 42)
        text = font.render("YOU WON", True, black)
        screen.blit(text, (0, 0))

    if end_game == 1 and timer_switch == 0:
        end_time = pygame.time.get_ticks()
        with open("/Users/sherryzhang/Desktop/Minesweeper/records.txt", "r") as f:
            old_records = f.readlines()

        for i in range(len(old_records)):
            if int(old_records[i].split()[0]) > time:
                old_records[i] = (f"{int(time)} {name} \n")
                print(old_records[i])
                break

        with open("/Users/sherryzhang/Desktop/Minesweeper/records.txt", "w+") as f:
            for i in old_records:
                f.write(f"{i}")
                
        font_record = pygame.font.Font('freesansbold.ttf', 37)

        record = font_record.render("Records: ", True, black)
        record_1 = font_record.render(f"1. {old_records[0]}", True, black)
        record_2 = font_record.render(f"2. {old_records[1]}", True, black)
        record_3 = font_record.render(f"3. {old_records[2]}", True, black)

        screen.blit(record, (0, 40))
        screen.blit(record_1, (0, 70))
        screen.blit(record_2, (0, 100))
        screen.blit(record_3, (0, 130))
        timer_switch = 1
    
    if start_time == 0:
        time = 0

    else:
        if end_time == 0:
            time = (pygame.time.get_ticks() - start_time)/1000
        
        elif end_time != 0:
            time = (end_time - start_time)/1000

    pygame.draw.rect(screen, white, (0, 653, 100, 40))
    text_time = font.render(f"{time: 04.0f}", True, black)
    screen.blit(text_time, (0, 653))

    pygame.display.flip()
