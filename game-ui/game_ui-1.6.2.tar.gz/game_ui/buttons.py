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

        self.image = None   # изоброжение кнопки, если == None, то будет рисоваться обычная кнопка с вашимы настройками
        self.imageWidth = None   # ширина изоброжения
        self.imageHeight = None   # высота изоброжения

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
        self.fillSize = 0   # уровень заливки кнопки, если == 0, то будет заливаться полностью

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for arg in args:

            if arg == 'x':
                self.x = args[arg]
            elif arg == 'y':
                self.y = args[arg]
                
            elif arg == 'width':
                self.width = args[arg]
            elif arg == 'height':
                self.height = args[arg]

            elif arg == 'color':
                self.color = args[arg]
            elif arg == 'pressedColor':
                self.pressedColor = args[arg]
            elif arg == 'selectedColor':
                self.selectedColor = args[arg]
            elif arg == 'func':
                self.func = args[arg]
            elif arg == 'text':
                self.defaultText = args[arg]
            elif arg == 'fast':
                self.fast = args[arg]
            elif arg == 'pressedText':
                self.pressedText = args[arg]
            elif arg == 'fontSize':
                self.fontSize = args[arg]
            elif arg == 'textColor':
                self.textColor = args[arg]
            
            elif arg == 'font':
                self.fontPath = args[arg]
            
            elif arg == 'borderRadius':
                self.borderRadius = args[arg]
            elif arg == 'fillSize':
                self.fillSize = args[arg]
            
            elif arg == 'image':
                if args[arg] != None:
                    self.image = pygame.image.load(args[arg]).convert()
                    self.imageWidth = self.image.get_width()
                    self.imageHeight = self.image.get_height()
            elif arg == 'imageWidth':
                self.imageWidth = args[arg]
            elif arg == 'imageHeight':
                self.imageHeight = args[arg]
            
            else:
                print(f'GameUI_Error: "{arg}" is not defined')
            
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

            if self.image != None:
                if self.image.get_width() != self.imageWidth or self.image.get_height() != self.imageHeight: self.image = pygame.transform.scale(self.image, (self.imageWidth, self.imageHeight))
            
            if self.image == None: self.rect.width = self.width; self.rect.height = self.height
            else: self.rect.width = self.imageWidth; self.rect.height = self.imageHeight

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

        if self.image == None:
            # отрисовка кнопки от зависимости переменной [mode]
            if self.mode == 0:
                pygame.draw.rect(self.surface, self.color, self.rect, self.fillSize, self.borderRadius)
            elif self.mode == 1:
                pygame.draw.rect(self.surface, self.pressedColor, self.rect, self.fillSize, self.borderRadius)
            elif self.mode == 2:
                pygame.draw.rect(self.surface, self.selectedColor, self.rect, self.fillSize, self.borderRadius)
            
            # отрисовка текста кнопки
            if self.text != '':
                text = self.font.render(self.text, 1, self.textColor)
                textWin = text.get_rect(center=(self.rect.x + self.width // 2, self.rect.y + self.height // 2))
                self.surface.blit(text, textWin)
        else:
            self.surface.blit(self.image, self.rect)

            if self.text != '':
                text = self.font.render(self.text, 1, self.textColor)
                textWin = text.get_rect(center=(self.rect.x + self.imageWidth // 2, self.rect.y + self.imageHeight // 2))
                self.surface.blit(text, textWin)

Buttons = []