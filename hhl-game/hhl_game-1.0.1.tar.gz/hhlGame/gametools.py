from .g_functions import *

class GameFun:

    def __init__(self):
        pass

    def addAnimationController(self) -> AnimationController:
        print('添加动画控制器')
        self.animation_controller = AnimationController(self, self.action_controller, self.event_controller, self.update_controller)

    def addActionController(self) -> ActionController:
        print('添加动作控制器')
        self.action_controller = ActionController(self.scene, self, self.event_controller, self.update_controller)

    def addCharacterController(self) -> CharacterController:
        self.character_controller = CharacterController(self.scene, self, self.action_controller, self.event_controller, self.update_controller)

    def addCollisionController(self, collision_range=3, collision_size=(30, 30, 30, 30), obj_range=(1, 1, 1, 1)) -> CollisionController:
        self.collision_controller = CollisionController(self, collision_range, collision_size, obj_range, self.action_controller, self.event_controller, self.update_controller)

