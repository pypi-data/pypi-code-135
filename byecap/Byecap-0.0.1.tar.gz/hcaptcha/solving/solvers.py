import imagehash

from ..challenges import Challenge
from .exceptions import *
from hashlib import sha1
from typing import Union
import random
import redis


class Solver:
    def __init__(
            self,
            database: Union[redis.Redis],
            min_answers: int = 3
    ):
        """Used for solving hCaptcha challenges.
        
        :param database: :class:`Redis` or :class:`Mapping` object to be used for storing tile IDs and counts.
        :param min_answers: minimum amount of answers to be submitted for a challenge."""
        self._database = database
        self._min_answers = min_answers

    def solve(self, challenge: Challenge) -> str:
        if challenge.token:
            return challenge.token
        if challenge.mode != "image_label_binary":
            raise UnsupportedChallenge(
                f"Unsupported challenge mode: '{challenge.mode}'")
        question_hash = sha1(challenge.question["en"].encode()).hexdigest()
        for tile in challenge.tiles:
            image_hash = sha1(tile.data).hexdigest()
            tile.custom_id = f"CACHED_DATA[{challenge.mode}:::{question_hash}:::{image_hash}:::DORT_GEN]"
            tile.score = self._get_tile_score(tile)
            tile.selected = False
        challenge.tiles.sort(
            key=lambda _tile: _tile.score or random.uniform(0, 0.97),
            reverse=True)
        n_answers = max(self._min_answers,
                        len(list(filter(lambda t: t.score >= 1, challenge.tiles))))
        for index in range(n_answers):
            tile = challenge.tiles[index]
            tile.selected = True
            challenge.answer(tile)

        challenge.submit()
        for tile in challenge.tiles:
            if not tile.selected:
                continue
            self._incr_tile_score(tile, 1)
        return challenge.token

    def _get_tile_score(self, tile):
        return int(self._database.get(tile.custom_id) or 0)

    def _incr_tile_score(self, tile, delta):
        self._database.incrby(tile.custom_id, delta)
