from src.inheritance.MultiLevel.bicycle import BiCycle
from src.inheritance.MultiLevel.hero_honda import HeroHonda


def get_vehicle_object(engine_present):
    if engine_present:
        return HeroHonda("", "", 123, 23)
    else:
        return BiCycle("hero", "")