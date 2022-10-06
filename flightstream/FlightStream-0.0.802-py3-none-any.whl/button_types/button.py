#!/usr/bin/env python3

from ast import And
from FlightStream.sources.source import Source
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer
from FlightStream.renderers.text_render import TextRender


class Button:

    COLOUR_MENU = (0, 50, 55)
    COLOUR_RED = (80, 30, 20)
    COLOUR_BLUE = (20, 30, 80)
    COLOUR_GREEN = (20, 70, 20)
    COLOUR_YELLOW = (60, 45, 0)
    COLOUR_BROWN = (85, 65, 50)
    COLOUR_BLACK = (0, 0, 0)
    COLOUR_WHITE = (255, 255, 255)
    COLOUR_INDICATOR = (35, 10, 30)

    def __init__(self):
        self.titles = []
        self.text_renderers = []
        self.actions = []
        self.sources = []
        self.icon = None
        self.background = self.COLOUR_BLACK
        self.initialise_subclass()
        self.initialise_instance()

    def initialise_subclass(self):
        pass

    def initialise_instance(self):
        pass

    def isKey(self, key):
        return self.key == key

    def get_key(self):
        return self.key

    def get_actions(self):
        return self.actions

    def has_icon(self):
        return self.icon != None

    def has_actions(self):
        return len(self.actions) > 0

    def get_icon(self):
        return self.icon

    def get_action(self, index=0):
        if self.has_actions() == False:
            return None
        return self.actions[index]

    def get_actions(self):
        if self.has_actions() == False:
            return None
        return self.actions

    def get_background(self):
        return self.background

    def get_title_count(self):
        return len(self.titles)

    def add_title(self, title, text_renderer):
        self.titles.append(title)
        self.text_renderers.append(text_renderer)

    def get_title(self, index=0):
        return self.titles[index]

    def get_title_renderer(self, index):
        return self.text_renderers[index]

    def has_sources(self):
        return len(self.sources) > 0

    def get_source_count(self):
        return len(self.sources)

    def get_source(self, index: int) -> Source:
        return self.sources[index]

    def get_sources(self):
        return self.sources

    def has_changed(self):
        for index in range(self.get_source_count()):
            source = self.sources[index]
            if source.has_changed():
                return True
        return False

    def add_action(self, action):
        self.actions.append(action)

    def add_source(self, source):
        self.sources.append(source)

    def set_background(self, background_color):
        self.background = background_color

    def set_key(self, key):
        self.key = key

    def set_title_renderer(self, index: int, text_renderer: TextRender):
        self.text_renderers[index] = text_renderer

    def show_lamp(self):
        return False

    def button_down(self, sdbr: StreamDeckButtonRenderer,  sim_integration):
        return None

    def button_up(self, sdbr: StreamDeckButtonRenderer, sim_integration):
        self.execute_actions(sdbr, sim_integration)

    def execute_actions(self, sdbr: StreamDeckButtonRenderer, sim_integration):
        if self.has_actions() == False:
            return
        for index in range(len(self.actions)):
            action = self.actions[index]
            action.execute(sdbr, sim_integration)

    def get_new_page(self):
        return None
