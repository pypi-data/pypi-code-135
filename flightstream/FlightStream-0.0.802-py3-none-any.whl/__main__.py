#!/usr/bin/env python3
import sys
import threading

from StreamDeck.DeviceManager import DeviceManager
from FlightStream.pages.page_main import PageMain
from FlightStream.stream_deck_integration.stream_deck_renderer import StreamDeckPageRenderer


def key_change_callback(deck, key, state):
    global renderer
    renderer.key_change_callback(deck, key, state)

def main():
    global renderer
    streamdecks = DeviceManager().enumerate()
    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()
        print("Opened {}".format(deck.deck_type()))
        deck.set_brightness(60)

        renderer.set_stream_deck(deck)
        renderer.set_current_page(PageMain())
        renderer.render_page()

        deck.set_key_callback(key_change_callback)

        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        for t in threading.enumerate():
            try:
                t.join()
                print('Exit')
                sys.exit()
            except RuntimeError:
                pass

if __name__ == "__main__":
    renderer = StreamDeckPageRenderer()
    main()
