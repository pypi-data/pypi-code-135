from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict


class PartialUpdate(TypedDict):
    uuid: str
    trainer: int
    update_time: str
    xp: Optional[int]
    trainer_level: Optional[int]
    total_xp: Optional[int]
    modified_extra_fields: List[str]


class Update(TypedDict):
    total_xp: NotRequired[int]
    trainer_level: NotRequired[int]
    pokedex_caught: NotRequired[int]
    pokedex_seen: NotRequired[int]
    gymbadges_gold: NotRequired[int]
    gym_gold: NotRequired[int]
    travel_km: NotRequired[str]
    pokedex_entries: NotRequired[int]
    capture_total: NotRequired[int]
    evolved_total: NotRequired[int]
    hatched_total: NotRequired[int]
    pokestops_visited: NotRequired[int]
    unique_pokestops: NotRequired[int]
    big_magikarp: NotRequired[int]
    battle_attack_won: NotRequired[int]
    battle_training_won: NotRequired[int]
    small_rattata: NotRequired[int]
    pikachu: NotRequired[int]
    unown: NotRequired[int]
    pokedex_entries_gen2: NotRequired[int]
    raid_battle_won: NotRequired[int]
    legendary_battle_won: NotRequired[int]
    berries_fed: NotRequired[int]
    hours_defended: NotRequired[int]
    pokedex_entries_gen3: NotRequired[int]
    challenge_quests: NotRequired[int]
    max_level_friends: NotRequired[int]
    trading: NotRequired[int]
    trading_distance: NotRequired[int]
    pokedex_entries_gen4: NotRequired[int]
    great_league: NotRequired[int]
    ultra_league: NotRequired[int]
    master_league: NotRequired[int]
    photobomb: NotRequired[int]
    pokedex_entries_gen5: NotRequired[int]
    pokemon_purified: NotRequired[int]
    rocket_grunts_defeated: NotRequired[int]
    rocket_giovanni_defeated: NotRequired[int]
    buddy_best: NotRequired[int]
    pokedex_entries_gen6: NotRequired[int]
    pokedex_entries_gen7: NotRequired[int]
    pokedex_entries_gen8: NotRequired[int]
    seven_day_streaks: NotRequired[int]
    unique_raid_bosses_defeated: NotRequired[int]
    raids_with_friends: NotRequired[int]
    pokemon_caught_at_your_lures: NotRequired[int]
    wayfarer: NotRequired[int]
    total_mega_evos: NotRequired[int]
    unique_mega_evos: NotRequired[int]
    trainers_referred: NotRequired[int]
    mvt: NotRequired[int]
    battle_hub_stats_wins: NotRequired[int]
    battle_hub_stats_battles: NotRequired[int]
    battle_hub_stats_stardust: NotRequired[int]
    battle_hub_stats_streak: NotRequired[int]
    type_normal: NotRequired[int]
    type_fighting: NotRequired[int]
    type_flying: NotRequired[int]
    type_poison: NotRequired[int]
    type_ground: NotRequired[int]
    type_rock: NotRequired[int]
    type_bug: NotRequired[int]
    type_ghost: NotRequired[int]
    type_steel: NotRequired[int]
    type_fire: NotRequired[int]
    type_water: NotRequired[int]
    type_grass: NotRequired[int]
    type_electric: NotRequired[int]
    type_psychic: NotRequired[int]
    type_ice: NotRequired[int]
    type_dragon: NotRequired[int]
    type_dark: NotRequired[int]
    type_fairy: NotRequired[int]


class ReadUpdate(Update):
    uuid: str
    trainer: int
    update_time: str
    xp: NotRequired[int]
    total_xp: Optional[int]
    trainer_level: Optional[int]
    badge_travel_km: NotRequired[str]
    badge_pokedex_entries: NotRequired[int]
    badge_capture_total: NotRequired[int]
    badge_evolved_total: NotRequired[int]
    badge_hatched_total: NotRequired[int]
    badge_pokestops_visited: NotRequired[int]
    badge_unique_pokestops: NotRequired[int]
    badge_big_magikarp: NotRequired[int]
    badge_battle_attack_won: NotRequired[int]
    badge_battle_training_won: NotRequired[int]
    badge_small_rattata: NotRequired[int]
    badge_pikachu: NotRequired[int]
    badge_unown: NotRequired[int]
    badge_pokedex_entries_gen2: NotRequired[int]
    badge_raid_battle_won: NotRequired[int]
    badge_legendary_battle_won: NotRequired[int]
    badge_berries_fed: NotRequired[int]
    badge_hours_defended: NotRequired[int]
    badge_pokedex_entries_gen3: NotRequired[int]
    badge_challenge_quests: NotRequired[int]
    badge_max_level_friends: NotRequired[int]
    badge_trading: NotRequired[int]
    badge_trading_distance: NotRequired[int]
    badge_pokedex_entries_gen4: NotRequired[int]
    badge_great_league: NotRequired[int]
    badge_ultra_league: NotRequired[int]
    badge_master_league: NotRequired[int]
    badge_photobomb: NotRequired[int]
    badge_pokedex_entries_gen5: NotRequired[int]
    badge_pokemon_purified: NotRequired[int]
    badge_rocket_grunts_defeated: NotRequired[int]
    badge_rocket_giovanni_defeated: NotRequired[int]
    badge_buddy_best: NotRequired[int]
    badge_pokedex_entries_gen6: NotRequired[int]
    badge_pokedex_entries_gen7: NotRequired[int]
    badge_pokedex_entries_gen8: NotRequired[int]
    badge_seven_day_streaks: NotRequired[int]
    badge_unique_raid_bosses_defeated: NotRequired[int]
    badge_raids_with_friends: NotRequired[int]
    badge_pokemon_caught_at_your_lures: NotRequired[int]
    badge_wayfarer: NotRequired[int]
    badge_total_mega_evos: NotRequired[int]
    badge_unique_mega_evos: NotRequired[int]
    badge_trainers_referred: NotRequired[int]
    badge_mvt: NotRequired[int]
    badge_type_normal: NotRequired[int]
    badge_type_fighting: NotRequired[int]
    badge_type_flying: NotRequired[int]
    badge_type_poison: NotRequired[int]
    badge_type_ground: NotRequired[int]
    badge_type_rock: NotRequired[int]
    badge_type_bug: NotRequired[int]
    badge_type_ghost: NotRequired[int]
    badge_type_steel: NotRequired[int]
    badge_type_fire: NotRequired[int]
    badge_type_water: NotRequired[int]
    badge_type_grass: NotRequired[int]
    badge_type_electric: NotRequired[int]
    badge_type_psychic: NotRequired[int]
    badge_type_ice: NotRequired[int]
    badge_type_dragon: NotRequired[int]
    badge_type_dark: NotRequired[int]
    badge_type_fairy: NotRequired[int]
    data_source: str


class CreateUpdate(Update):
    trainer: int
    update_time: str
    data_source: str


class EditUpdate(Update):
    pass
