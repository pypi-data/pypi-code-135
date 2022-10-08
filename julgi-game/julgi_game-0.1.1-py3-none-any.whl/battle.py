from __future__ import annotations

import random
from dataclasses import asdict, is_dataclass
from typing import Any

from .classes import BattleData, BattleMetaData, PostBattleData, Skill, User
from .util import get_skill_info


class BattleManager:
    def __init__(
        self,
        name1: str,
        name2: str,
        seed: str = "",
    ):
        self.user1 = User(name1)
        self.user2 = User(name2)
        self.seed = seed if seed else self.gen_seed()

        skill_info = get_skill_info("skill_ko.yml")
        self.skills = [Skill(name=k, **v) for k, v in skill_info.items()]

    @staticmethod
    def gen_seed() -> str:
        return "".join(random.choices("0123456789ABCDEF", k=8))

    def battle(self, seed: str = "", return_as_dict: bool = False) -> dict[str, Any]:
        if not seed:
            seed = self.seed
        random.seed(seed)

        # .battle 함수를 여러번 호출했을 때를 위해 hp 초기화
        self.user1.reset_hp()
        self.user2.reset_hp()

        users = [self.user1, self.user2]

        result = {"meta_data": None, "battle_data": [], "post_data": None}
        result["meta_data"] = BattleMetaData(self.user1, self.user2, self.seed)

        # 유저 스킬 설정
        for user in users:
            num = random.randint(2, min(len(self.skills), 8))
            user.skills = random.sample(self.skills, k=num)

        # i: 현재 플레이어의 인덱스, 스피드 높은 사람이 먼저
        i = 0 if self.user1.speed >= self.user2.speed else 1

        turn = 0
        while self.user1.live and self.user2.live:
            turn += 1

            user = users[i]
            other = users[1 - i]

            do_normal_attack = True

            # 스킬 사용 여부 결정
            is_use_skill = self.prob(20)

            # 명중 여부 결정
            is_hit = self.prob(user.hit)

            # 치명타 여부 결정
            is_critical = self.prob(user.critical)

            # 기타 변수 설정
            use_heal = False
            heal_amount = damage = None
            # 스킬 사용
            skill = random.choice(user.skills)
            if is_use_skill:
                amount = round(getattr(user, skill.stat) * skill.multiplier)
                do_normal_attack = False

                # 회복 스킬
                if skill.heal:
                    amount = self.randomness(amount)
                    if is_critical:
                        amount = round(amount * 1.5)
                    user.hp = min(user.hp + amount, user.max_hp)
                    use_heal = True
                    heal_amount = amount

                # 공격 스킬
                elif is_hit:
                    if is_critical:
                        amount = round(amount * 1.5)
                    amount = self.randomness(amount)
                    other.hp = max(other.hp - amount, 0)
                    damage = amount

            # 일반 공격
            if do_normal_attack and is_hit:
                amount = user.attack
                if is_critical:
                    amount = round(amount * 1.5)
                amount = self.randomness(amount)
                other.hp = max(other.hp - amount, 0)
                damage = amount

            this_turn = BattleData(
                user=user.name,
                user_hp=user.hp,
                user_max_hp=user.max_hp,
                other=other.name,
                other_hp=other.hp,
                other_max_hp=other.max_hp,
                use_skill=is_use_skill,
                skill=skill if is_use_skill else None,
                use_heal=use_heal,
                heal_amount=heal_amount,
                is_hit=is_hit,
                is_critical=is_critical,
                damage=damage,
            )

            result["battle_data"].append(this_turn)

            # 턴 종료
            i = 1 - i

        # 배틀 종료
        winner = self.user1 if self.user1.live else self.user2
        post_battle_data = PostBattleData(winner=winner.name, turns=turn)
        result["post_data"] = post_battle_data

        if return_as_dict:
            dict_result = {}
            for k, v in result.items():
                if is_dataclass(v):
                    dict_result[k] = asdict(v)
                elif isinstance(v, list) and v and is_dataclass(v[0]):
                    dict_result[k] = [asdict(c) for c in v]
                else:
                    dict_result[k] = v
            return dict_result

        return result

    @staticmethod
    def prob(p: int) -> bool:
        "p%의 확률로 True를 반환합니다."
        return p >= random.randint(1, 100)

    @staticmethod
    def randomness(v: int) -> int:
        "v의 10%의 범위 내에서 랜덤한 값을 반환합니다. 최소 1"
        return max(random.randint(round(v * 0.9), round(v * 1.1)), 1)
