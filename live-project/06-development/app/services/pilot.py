from app.config import Settings


def is_pilot_eligible(city: str, sport: str, own_vehicle: bool, settings: Settings) -> bool:
    if own_vehicle:
        return False
    return (
        city.strip().casefold() == settings.pilot_city.strip().casefold()
        and sport.strip().casefold() == settings.pilot_sport.strip().casefold()
    )
