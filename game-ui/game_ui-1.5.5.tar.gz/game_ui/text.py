import pygame

pygame.init()

class Text:
    def __init__(self, surface, **args):
        
        Texts.append(self)
        
        self.x, self.y = 0, 0   # начальное положение text
        self.width, self.height = 300, 300   # размер text - (ширина, высота)

        self.surface = surface   # окно на котором будет рисоваться кнопка
        self.renderSurface = pygame.Surface((self.width, self.height))   # второе окно к котором будет содержимое
        
        self.color = (150, 150, 150)   # цвет фона
        self.textColor = (255, 255, 255)   # цвет текста

        self.oldMousePos = (0, 0)   # старое положение мышки по Y [нужно для скролла]
        self.lastY = 0   # последнее положение текста по Y [нужно для отрисовки текста]

        self.text = ''   # текст text
        self.textPos = 0   # положение текста [нужно для скролла]

        """

        Настройки курсора:

        StartTime - интервал времени, через которое курсор будет появлятся - исчезать
        time - текущее время через которое курсор появится - исчезнет
        direct - указывает исчезнет ли курсор или появится при истекания времени

        """

        self.StartTime = 30
        self.time = 30
        self.direct = -1

        self.eding = True   # указывает на то, что можно ли на данный момент вводить текст в text

        self.fontSize = 30   # размер шрифта
        self.fontPath = None   # путь до шрифта, если == None, то будет использован стандартный
        self.font = pygame.font.Font(self.fontPath, self.fontSize)   # шрифт

        self.mode = 0   # режим отрисовки text
        self.render = True   # переменная, отвечающая за отрисовку text на экране, если == True, то text будет рисоваться, иначе нет.

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for arg in args:
            get = str(arg)

            if get == 'x':
                self.x = args[get]
            if get == 'y':
                self.y = args[get]
                
            if get == 'width':
                self.width = args[get]
            if get == 'height':
                self.height = args[get]

            if get == 'color':
                self.color = args[get]

            if get == 'fontSize':
                self.fontSize = args[get]
            if get == 'textColor':
                self.textColor = args[get]
            
            if get == 'font':
                self.fontPath = args[arg]

        self.font = pygame.font.Font(self.fontPath, self.fontSize)
        self.renderSurface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    # функция устанавливающая отрисовку кнопки на экране - (True or False)
    def setRender(self, value):
        if value:
            self.render = True
        elif not value:
            self.render = False
    
    # функция которая добавляет символ в текст
    def Press(self, key):

        """

        Пояснение: переменная [mode] отвечает за режим отрисовки кнопки;

        Если [mode] == 1, то в input может добавляется текст;

        """

        if self.render and self.mode == 1 and self.eding:
            keys = pygame.key.get_pressed()

            # добавление символа в текст
            if not keys[pygame.K_BACKSPACE] and not keys[pygame.K_KP_ENTER] and key != '\r' and self.mode == 1:
                self.text += key
            
            # добавление новой строки в текст
            elif not keys[pygame.K_BACKSPACE] and keys[pygame.K_KP_ENTER] or key == '\r' and self.mode == 1:
                self.text += '\n'

                if self.lastY + self.textPos + self.fontSize // 1.5 > self.rect.height:
                    self.textPos -= self.fontSize // 1.5
            
            # удаление последнего символа в тексе
            elif keys[pygame.K_BACKSPACE] and self.mode == 1 and self.text != '':
                self.text = self.text[:-1]
                if self.text != '' and self.text[-1] == '\n': self.text = self.text[:-1]
    
    # функция которая сохраняет положение мышки по Y, в дальнейшем из этого получиться
    def Scroll(self):
        self.oldMousePos = pygame.mouse.get_pos()
    
    # функция обвноляющая весь text и взоимодействие с ней
    def update(self):

        if self.render:

            if self.mode == 1:

                """

                Если [direct] == -1, то курсор будет показан
                Иначе, курсор будет спрятан

                """

                if self.direct == -1:
                    self.time -= 1
                    if self.time <= 0: self.direct = 1
                else:
                    self.time += 1
                    if self.time >= self.StartTime: self.direct = -1

            mBT = pygame.mouse.get_pressed()
            mx, my = pygame.mouse.get_pos()

            # как только ЛКМ была нажата, и при этом позиция мыши касается text
            if mBT[0] and self.rect.collidepoint(mx, my):
                newMousePos = pygame.mouse.get_pos()    

                # изменение позиции текста [для скролла]
                if self.textPos + (newMousePos[1] - self.oldMousePos[1]) < 0:
                    self.textPos += (newMousePos[1] - self.oldMousePos[1])
            
            # как только ЛКМ была нажата, и при этом позиция мыши касается text - [mode = 1]
            if mBT[0] and self.rect.collidepoint(mx, my):
                self.mode = 1
            
            # как только ЛКМ была нажата, и при этом позиция мыши не касается text - [mode = 0]
            elif mBT[0] and not self.rect.collidepoint(mx, my):
                self.mode = 0

            self.draw()
    
    def draw(self):

        # подстраивание второго окна и текста под размеры text
        if self.mode == 1 and self.renderSurface.get_width() != self.rect.width or self.renderSurface.get_height() != self.rect.height:
            self.renderSurface = pygame.Surface((self.rect.width, self.rect.height))
            self.text = self.text.replace('\n', '')

        self.renderSurface.fill(self.color)

        if self.mode == 1:
            # подстраивание текста
            while 1:
                get = self.text.split('\n')
                last = self.font.render(get[-1], 1, self.textColor)

                rect = pygame.Rect(10 + last.get_width(), 0, last.get_width(), last.get_height())
                if rect.x > self.rect.width:
                    self.text = self.text[0:-1] + '\n' + self.text[-1]

                    if self.lastY + self.textPos > self.rect.height:
                        self.textPos -= self.fontSize // 1.5

                    break
                break

        get = self.text.split('\n')

        y = 10

        # отрисовка текста
        for obj in get:

            tx = self.font.render(obj, 1, self.textColor)
            self.renderSurface.blit(tx, (10, y + self.textPos))

            y += self.fontSize // 1.3
        
        self.lastY = y
        
        # отрисовка курсора
        if self.mode == 1 and self.direct == -1:
            pygame.draw.rect(self.renderSurface, (0, 150, 255), (10 + tx.get_width() + 5, (y - self.fontSize // 1.3) + self.textPos, self.fontSize // 10, self.fontSize // 1.3))
        
        # отрисовка всего text
        self.surface.blit(self.renderSurface, (self.rect.x, self.rect.y))

Texts = []