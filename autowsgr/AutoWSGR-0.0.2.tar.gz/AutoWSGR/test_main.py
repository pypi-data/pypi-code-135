import datetime
import os
import sys
import time

import keyboard as kd

from constants.settings import S
from constants.global_attribute import event_pressed
from constants.ui import UI
from controller.run_timer import Timer
from fight.battle import BattlePlan
from fight.exercise import NormalExercisePlan
from fight.normal_fight import NormalFightPlan
from game.game_operation import Expedition, GainBounds, RepairByBath
# from ocr.ship_name import recognize_ship

sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(__file__))

S.DEBUG = False


def start_script(device_name="emulator-5554", account=None, password=None):
    """启动脚本,返回一个 Timer 记录器

    Returns:
        Timer: 该模拟器的记录器
    """
    timer = Timer()
    timer.setup(device_name, account, password, True)
    
    return timer

def listener(event: kd.KeyboardEvent):
    on_press = event_pressed
    if (event.event_type == 'down'):
        if (event.name in on_press):
            return
        on_press.add(event.name)
    if (event.event_type == 'up'):
        on_press.discard(event.name)

    if ('ctrl' in on_press and 'alt' in on_press and 'c' in on_press):
        global script_end
        script_end = 1
        print("Script end by user request")
        quit()


if __name__ == "__main__":
    # timer = start_script(account="1558718963", password=1558718963)
    timer = start_script()
    # battleship_plan = BattlePlan(timer, 'plans/battle/hard_Battleship.yaml', 'plans/default.yaml')
    # aircraftcarrier_plan = BattlePlan(timer, 'plans/battle/hard_aircraftcarrier.yaml', 'plans/default.yaml')
    battle_plan = BattlePlan(timer, 'data/plans/battle/hard_destroyer.yaml')
    fight_plan = NormalFightPlan(timer, "data/plans/normal_fight/9-1BF.yaml")
    expedition_plan = Expedition(timer)
    start_time = last_time = time.time()
    
    ret = "success"
    while ret == "success":
        ret = battle_plan.run()

    # ret = "success"
    # while ret == "success":
    #     ret = fight_plan.run()

    #     if time.time() - last_time >= 5*60:
    #         expedition_plan.run(True)
    #         GainBounds(timer)
    #         last_time = time.time()

    while True:
        RepairByBath(timer)
        expedition_plan.run(True)
        GainBounds(timer)
        time.sleep(360)
