import scripts
import gui


def on_init():
    scripts.script_engine.start()
    scripts.update_frozen_objects.enabled = True


def on_shutdown():
    scripts.script_engine.stop()


def main():
    gui.init_gui().mainloop()


if __name__ == "__main__":
    on_init()
    main()
    on_shutdown()
