import pygame
import sys

# 初始化 Pygame
pygame.init()

# 窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("控制球到达终点")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 球（玩家）属性
ball_radius = 20
ball_x = 50
ball_y = HEIGHT // 2
ball_speed = 5

# 终点区域（矩形）
target_rect = pygame.Rect(WIDTH - 100, HEIGHT // 2 - 50, 80, 100)

# 游戏状态
game_over = False
win = False

# 时钟控制帧率
clock = pygame.time.Clock()
FPS = 60

# 主循环
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if win:
                game_over = True

    keys = pygame.key.get_pressed()
    if not win:
        if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
            ball_x -= ball_speed
        if keys[pygame.K_RIGHT] and ball_x + ball_radius < WIDTH:
            ball_x += ball_speed
        if keys[pygame.K_UP] and ball_y - ball_radius > 0:
            ball_y -= ball_speed
        if keys[pygame.K_DOWN] and ball_y + ball_radius < HEIGHT:
            ball_y += ball_speed

        if target_rect.collidepoint(ball_x, ball_y):
            win = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, target_rect)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    if win:
        font = pygame.font.Font(None, 74)
        text = font.render("你赢了！", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
        font_small = pygame.font.Font(None, 36)
        sub_text = font_small.render("按任意键退出", True, BLACK)
        sub_rect = sub_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60))
        screen.blit(sub_text, sub_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()