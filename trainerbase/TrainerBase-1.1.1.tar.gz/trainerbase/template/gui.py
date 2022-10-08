import typing
import tkinter.ttk
import tkinter.messagebox

import trainerbase.gameobject
import trainerbase.scriptengine
import trainerbase.codeinjection
import objects
import scripts
import injections


def set_entry_text(entry: tkinter.ttk.Entry, text: str):
    entry.delete(0, tkinter.END)
    entry.insert(0, text)


def add_gameobject_to_gui(
    parent_frame: tkinter.ttk.LabelFrame,
    readable_name: str,
    row: int,
    gameobject: trainerbase.gameobject.GameObject,
    before_set: typing.Callable = int,
):
    def on_frozen_state_change():
        gameobject.frozen = gameobject.value if frozen_state.get() else None

    def on_value_get():
        set_entry_text(text, gameobject.value)

    def on_value_set():
        new_value = before_set(text.get())
        if gameobject.frozen is None:
            gameobject.value = new_value
        else:
            gameobject.frozen = new_value

    column = 0

    label = tkinter.ttk.Label(parent_frame, text=readable_name)
    label.grid(row=row, column=column)
    column += 1

    frozen_state = tkinter.BooleanVar(value=gameobject.frozen is not None)
    frozen_checkbutton = tkinter.ttk.Checkbutton(
        parent_frame,
        command=on_frozen_state_change,
        var=frozen_state,
    )
    frozen_checkbutton.grid(row=row, column=column)
    column += 1

    text = tkinter.ttk.Entry(parent_frame, width=20)
    text.grid(row=row, column=column)
    column += 1

    button_get = tkinter.ttk.Button(parent_frame, text="get", command=on_value_get)
    button_get.grid(row=row, column=column)
    column += 1

    button_set = tkinter.ttk.Button(parent_frame, text="set", command=on_value_set)
    button_set.grid(row=row, column=column)


def add_script_to_gui(
    parent_frame: tkinter.ttk.LabelFrame,
    row: int,
    script: trainerbase.scriptengine.Script,
):
    def on_script_state_change():
        script.enabled = script_state.get()

    label = tkinter.ttk.Label(parent_frame, text=script.callback.__name__)
    label.grid(row=row, column=0)

    script_state = tkinter.BooleanVar(value=script.enabled)
    script_checkbutton = tkinter.ttk.Checkbutton(
        parent_frame,
        command=on_script_state_change,
        var=script_state,
    )
    script_checkbutton.grid(row=row, column=1)


def add_codeinjection_to_gui(
    parent_frame: tkinter.ttk.LabelFrame,
    readable_name: str,
    row: int,
    injection: trainerbase.codeinjection.CodeInjection,
):
    def on_codeinjection_state_change():
        if injection_state.get():
            injection.inject()
        else:
            injection.eject()

    label = tkinter.ttk.Label(parent_frame, text=readable_name)
    label.grid(row=row, column=0)

    injection_state = tkinter.BooleanVar(value=False)
    injection_checkbutton = tkinter.ttk.Checkbutton(
        parent_frame,
        command=on_codeinjection_state_change,
        var=injection_state,
    )
    injection_checkbutton.grid(row=row, column=1)


def init_gui() -> tkinter.Tk:
    window = tkinter.Tk()
    window.title("Trainer Base")
    window.resizable(False, False)

    # ScriptEngine
    def on_scriptengine_check():
        if scripts.script_engine.should_run:
            tkinter.messagebox.showinfo("ScriptEngine", "It's OK!")
        else:
            tkinter.messagebox.showerror("ScriptEngine", "Stopped.")

    frame_scripts = tkinter.ttk.LabelFrame(window, text="Scripts")
    for row, script in enumerate(scripts.script_engine.scripts):
        add_script_to_gui(frame_scripts, row, script)
    check_scriptengine_status = tkinter.ttk.Button(
        frame_scripts, text="Check ScriptEngine", command=on_scriptengine_check
    )
    check_scriptengine_status.grid(row=row + 1, column=0)
    frame_scripts.grid(row=0, column=0)

    # CodeInjection
    frame_codeinjection = tkinter.ttk.LabelFrame(window, text="Code Injection")
    # add_codeinjection_to_gui(...)
    frame_codeinjection.grid(row=1, column=0)

    return window
