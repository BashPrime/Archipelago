from enum import Enum
from typing import Dict, List
from BaseClasses import Item

class MetroidPrime2Item(Item):
    game: str = "Metroid Prime 2: Echoes"

class SuitUpgrade(Enum):
    # Beams
    Power_Beam = "Power Beam"
    Dark_Beam = "Dark Beam"
    Light_Beam = "Light_Beam"
    Annihilator_Beam = "Annihilator Beam"
    Charge_Beam = "Charge Beam"
    # Morph Ball
    Morph_Ball = "Morph Ball"
    Boost_Ball = "Boost Ball"
    Spider_Ball = "Spider Ball"
    Morph_Ball_Bomb = "Morph Ball Bomb"
    Power_Bomb = "Power Bomb"
    Cannon_Ball = "Cannon Ball"
    # Suits
    Varia_Suit = "Varia Suit"
    Dark_Suit = "Dark Suit"
    Light_Suit = "Light Suit"
    # Movement Systems
    Space_Jump_Boots = "Space Jump Boots"
    Gravity_Boost = "Gravity Boost"
    Grapple_Beam = "Grapple Beam"
    Screw_Attack = "Screw Attack"
    # Visors
    Combat_Visor = "Combat Visor"
    Scan_Visor = "Scan Visor"
    Dark_Visor = "Dark Visor"
    Echo_Visor = "Echo Visor"
    # Translators
    Violet_Translator = "Violet Translator"
    Amber_Translator = "Amber Translator"
    Emerald_Translator = "Emerald Translator"
    Cobalt_Translator = "Cobalt Translator"
    # Missiles
    Missile_Launcher = "Missile Launcher"
    Seeker_Launcher = "Seeker_Launcher"
    # Beam Combos
    Super_Missile = "Super Missile"
    Darkburst = "Darkburst"
    Sunburst = "Sunburst"
    Sonic_Boom = "Sonic Boom"
    # Expansions
    Energy_Tank = "Energy Tank"
    Missile_Expansion = "Missile Expansion"
    Power_Bomb_Expansion = "Power Bomb Expansion"
    Beam_Ammo_Expansion = "Beam Ammo Expansion"

class ProgressiveUpgrade(Enum):
    Progressive_Missile = "Progressive Missile"
    Progressive_Suit = "Progressive Suit"
    Progressive_Grapple = "Progressive Grapple"

PROGRESSIVE_ITEM_MAPPING: Dict[ProgressiveUpgrade, List[SuitUpgrade]] = {
    ProgressiveUpgrade.Progressive_Missile: {
        SuitUpgrade.Missile_Launcher,
        SuitUpgrade.Seeker_Launcher
    },
    ProgressiveUpgrade.Progressive_Suit: {
        SuitUpgrade.Dark_Suit,
        SuitUpgrade.Light_Suit
    },
    ProgressiveUpgrade.Progressive_Grapple: {
        SuitUpgrade.Grapple_Beam,
        SuitUpgrade.Screw_Attack
    }
}
