import pygame
import sys
import random

# 全局定义
SCREEN_X = 600
SCREEN_Y = 600
body = []

s = 0
# 蛇类
# 点以25为单位
class Snake(object):
    # 初始化各种需要的属性 [开始时默认向右/身体块x5]
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.addnode()

    # 无论何时 都在前端增加蛇块
    def addnode(self):
        global s
        s += 1
        left, top = (0, 0)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.dirction == pygame.K_LEFT:
            node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0, node)

    # 删除最后一个块
    def delnode(self):
        global s
        s -= 1
        self.body.pop()

    # 死亡判断
    def isdead(self):
        # 撞墙
        if self.body[0].x not in range(SCREEN_X):
            return True
        if self.body[0].y not in range(SCREEN_Y):
            return True
        # 撞自己
        if self.body[0] in self.body[1:]:
            return True
        return False

    # 移动！
    def move(self):
        self.addnode()
        self.delnode()
        self.add()

    def add(self):
        global body
        global s
        t = 0
        body = []
        while t < s:
            body.append((self.body[t].x, self.body[t].y))
            t += 1


    # 改变方向 但是左右、上下不能被逆向改变
    def changedirection(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:
            if (curkey in LR) and (self.dirction in LR):
                return
            if (curkey in UD) and (self.dirction in UD):
                return
            self.dirction = curkey



# 食物类
# 方法： 放置/移除
# 点以25为单位
class Food:
    def __init__(self):
        self.rect = pygame.Rect(-50, 0, 25, 25)

    def remove(self):
        self.rect.x = -50

    def set(self):
        global body
        m = 1
        if self.rect.x == -50:
            allpos = []
            for pos in range(25, SCREEN_Y - 25, 25):
                allpos.append(pos)
                # 不靠墙太近 25 ~ SCREEN_X-25 之间
            while m:

                x = allpos[random.randint(0, 21)]
                y = allpos[random.randint(0, 21)]
                if (x, y) not in body:
                    self.rect.left = x
                    self.rect.top = y
                    print(self.rect)
                    m = 0



def show_text(screen, pos, text, color, font_bold=False, font_size=60, font_italic=False):
    # 获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("宋体", font_size)
    # 设置是否加粗属性
    cur_font.set_bold(font_bold)
    # 设置是否斜体属性
    cur_font.set_italic(font_italic)
    # 设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    # 绘制文字
    screen.blit(text_fmt, pos)


def main():
    global body
    global s
    p = 0
    t = 10
    a = 242
    b = 192
    c = 86
    pygame.init()
    screen_size = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    scores = 0
    isdead = False

    # 蛇/食物
    snake = Snake()
    food = Food()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.changedirection(event.key)
                # 死后按space重新
                if event.key == pygame.K_SPACE:
                    t = 30
                if event.key != pygame.K_SPACE:
                    t = 10
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE and isdead:
                    body = []
                    s = 0
                    return main()

        screen.fill((0, 0, 0))

        # 画蛇身 / 每一步+1分
        if not isdead:
            scores += 1
            snake.move()
        pygame.draw.rect(screen, (255, 187, 255), snake.body[0], 0)
        x, y, z = 255, 187, 255
        for rect in snake.body[1:]:
            x = x - 5
            y = y + 3
            z = z - 4
            if x <= 0:
                x, y, z = 255, 187, 255
            if y >= 255:
                x, y, z = 255, 187, 255
            if z <= 0:
                x, y, z = 255, 187, 255
            pygame.draw.rect(screen, (x, y, z), rect, 0)

        # 显示死亡文字
        isdead = snake.isdead()
        if isdead:
            show_text(screen, (100, 200), 'YOU DEAD!', (227, 29, 18), False, 100)
            show_text(screen, (150, 260), 'press space to try again...', (227, 29, 18), False, 30)

        # 食物处理 / 吃到+50分
        # 当食物rect与蛇头重合,吃掉 -> Snake增加一个Node
        if food.rect == snake.body[0]:
            scores += 50
            food.remove()
            snake.addnode()
            snake.add()
            p = 1



        # 食物投递
        food.set()
        if p == 1:
            a = random.randint(108, 253)
            b = random.randint(89, 203)
            c = random.randint(40, 107)
            if (a+b+c) % 5 == 0:
                pygame.draw.rect(screen, (255, 110, 180), food.rect, 0)
                t = 20
            elif (a+b+c) % 5 == 3:
                pygame.draw.rect(screen, (187, 255, 255), food.rect, 0)
                t = 6
            elif (a+b+c) % 5 != 0 and (a+b+c) % 5 != 3:
                pygame.draw.rect(screen, (a, b, c), food.rect, 0)
                t = 10
        if p == 0:
            pygame.draw.rect(screen, (a, b, c), food.rect, 0)
        p = 0

        # 显示分数文字
        show_text(screen, (50, 500), 'Scores: ' + str(scores), (223, 223, 223))

        pygame.display.update()
        clock.tick(t)


if __name__ == '__main__':
    main()