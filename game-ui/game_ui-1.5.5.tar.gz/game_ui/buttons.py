import pygame

pygame.init()

class Button:
    def __init__(self, surface, **args):
        
        Buttons.append(self)
        
        self.x, self.y = 0, 0    # начальоне положение кнопки
        self.width, self.height = 100, 100 # размер кнопки - (ширина, высота)
        self.surface = surface     # окно на котором будет рисоваться кнопка
        
        self.color = (150, 150, 150)   # цвет кнопки
        self.pressedColor = (80, 80, 80)   # цвет кнопки когда она нажата
        self.selectedColor = (120, 120, 120)   # цвет кнопки когда курсор наведен на нее

        self.func = None   # функция которая будет вызываться при нажатии кнопки

        self.defaultText = ''   # текст кнопки
        self.textColor = (255, 255, 255)   # цвет текста
        self.text = self.defaultText
        self.pressedText = self.text   # текст кнопки когда кнопка нажата

        self.fontSize = 50   # размер шрифта
        self.fast = False    # говорит о том будет ли вызываться функция после отжатия кнопки или до тех пор пока кнопка нажата
        self.fontPath = None    # путь до шрифта, если == None, то будет использован стандартный
        self.font = pygame.font.Font(self.fontPath, self.fontSize)

        self.mode = 0   # режим отрисовки кнопки
        self.press = False
        self.render = True  # переменная, отвечающая за отрисовку кнопки на экране, если == True, то кнопка будет рисоваться, иначе нет.
        self.borderRadius = -1  # уровень сглаживания углов у кнопки, если == -1, то сглаживание не будет
        
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
            if get == 'pressedColor':
                self.pressedColor = args[get]
            if get == 'selectedColor':
                self.selectedColor = args[get]
            if get == 'func':
                self.func = args[get]
            if get == 'text':
                self.defaultText = args[get]
            if get == 'fast':
                self.fast = args[get]
            if get == 'pressedText':
                self.pressedText = args[get]
            if get == 'fontSize':
                self.fontSize = args[get]
            if get == 'textColor':
                self.textColor = args[get]
            
            if get == 'font':
                self.fontPath = args[arg]
            
            if get == 'borderRadius':
                self.borderRadius = args[arg]
            
        self.text = self.defaultText
        self.pressedText = self.text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font(self.fontPath, self.fontSize)
    
    # функция устанавливающая отрисовку кнопки на экране - (True or False)
    def setRender(self, value):
        if value == True:
            self.render = True
        elif value == False:
            self.render = False
    
    # функция обвноляющая всю кнопку и взоимодействие с ней
    def update(self):
        
        if self.render:
            mousePos = pygame.mouse.get_pos()
            mBT = pygame.mouse.get_pressed()
            
            # если переменная fast == False
            if not self.fast:
                """

                Пояснение: переменная [mode] отвечает за режим отрисовки кнопки;

                Если [mode] == 0, то кнопка будет отрисоваться в обычном цвете;
                Если [mode] == 1, то кнопка будет отрисоваться в режиме нажатия на кнопку;
                Если [mode] == 2, то кнопка будет отрисоваться в режиме выбранная кнопка;

                """

                # как только ЛКМ была нажата, и позиция мыши касалась кнопки - [mode = 1]
                if mBT[0] and self.rect.collidepoint(mousePos) and not self.press:
                    self.text = self.pressedText
                    self.mode = 1
                    self.press = True

                # как только ЛКМ была отжата, и позиция мыши не касалась кнопки, и при этом до этого ЛКМ была нажата - [mode = 0]
                if not mBT[0] and self.press and self.rect.collidepoint(mousePos):
                    self.text = self.defaultText
                    if self.func != None:
                        self.func()
                    self.mode = 0
                    self.press = False
                
                # как только позиция мыши не касается кнопки, и при этом ЛКМ была нажата - [mode = 0]
                if not self.rect.collidepoint(mousePos) and self.press and mBT[0]:
                    self.text = self.defaultText
                    self.mode = 0
                    self.press = False
                
                # как только позиция мыши касается кнопки, и при этом ЛКМ не была нажата - [mode = 2]
                if self.rect.collidepoint(mousePos) and not self.press and not mBT[0]:
                    self.mode = 2
                
                # как только позиция мыши не касается кнопки, и ЛКМ не была нажата - [mode = 0]
                if not self.rect.collidepoint(mousePos) and not self.press and not mBT[0]:
                    self.mode = 0
            
            # иначе
            if self.fast:

                # как только ЛКМ была нажата, и позиция мыши касалась кнопки - [mode = 1]
                if mBT[0] and self.rect.collidepoint(mousePos):
                    self.text = self.pressedText
                    self.mode = 1
                    if self.func != None:
                        self.func()
                    self.press = True
                
                # как только ЛКМ была отжата, и при этом позиция мыши касалась кнопки - [mode = 0]
                if not mBT[0] and self.press and self.rect.collidepoint(mousePos):
                    self.text = self.defaultText
                    self.mode = 0
                    self.press = False
                
                # как только позиция мыши не касается кнопки, и при этом ЛКМ была нажата - [mode = 0]
                if not self.rect.collidepoint(mousePos) and self.press and mBT[0]:
                    self.text = self.defaultText
                    self.mode = 0
                    self.press = False
                
                # как только позиция мыши касается кнопки, и при этом ЛКМ не была нажата - [mode = 2]
                if self.rect.collidepoint(mousePos) and not self.press and not mBT[0]:
                    self.mode = 2
                
                # как только позиция мыши не касается кнопки, и при этом ЛКМ не была нажата - [mode = 0]
                if not self.rect.collidepoint(mousePos) and not self.press and not mBT[0]:
                    self.mode = 0

            self.draw()
            
    def draw(self):

        # отрисовка кнопки от зависимости переменной [mode]
        if self.mode == 0:
            pygame.draw.rect(self.surface, self.color, self.rect, 0, self.borderRadius)
        elif self.mode == 1:
            pygame.draw.rect(self.surface, self.pressedColor, self.rect, 0, self.borderRadius)
        elif self.mode == 2:
            pygame.draw.rect(self.surface, self.selectedColor, self.rect, 0, self.borderRadius)
        
        # отрисовка текста кнопки
        text = self.font.render(self.text, 1, self.textColor)
        textWin = text.get_rect(center=(self.rect.x + self.width // 2, self.rect.y + self.height // 2))
        self.surface.blit(text, textWin)

Buttons = []