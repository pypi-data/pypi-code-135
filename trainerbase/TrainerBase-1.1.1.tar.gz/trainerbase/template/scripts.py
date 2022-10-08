from trainerbase.gameobject import GameObject
from trainerbase.scriptengine import ScriptEngine

import objects


script_engine = ScriptEngine()


@script_engine.register_script
def update_frozen_objects():
    GameObject.update_frozen_objects()
