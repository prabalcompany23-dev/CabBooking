from app.config import Settings
from app.services.pilot import is_pilot_eligible


def test_pilot_eligible_match() -> None:
    settings = Settings(pilot_city="Bengaluru", pilot_sport="Badminton")
    assert is_pilot_eligible("Bengaluru", "Badminton", False, settings) is True
    assert is_pilot_eligible("bengaluru", "badminton", False, settings) is True


def test_pilot_ineligible_own_vehicle() -> None:
    settings = Settings(pilot_city="Bengaluru", pilot_sport="Badminton")
    assert is_pilot_eligible("Bengaluru", "Badminton", True, settings) is False


def test_pilot_ineligible_city() -> None:
    settings = Settings(pilot_city="Bengaluru", pilot_sport="Badminton")
    assert is_pilot_eligible("Mumbai", "Badminton", False, settings) is False
