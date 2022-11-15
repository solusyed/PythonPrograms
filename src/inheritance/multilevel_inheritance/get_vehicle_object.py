from src.inheritance.multilevel_inheritance.bicycle import BiCycle
from src.inheritance.multilevel_inheritance.hero_honda import HeroHonda


def get_vehicle_object(engine_present):
    if engine_present:
        return HeroHonda("", "", 123, 23)
    else:
        return BiCycle("hero", "")