"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from src.infrastructure.repositories.carddb import CardRepository
from src.infrastructure.repositories.countrydb import \
    CountryRepository
from src.infrastructure.repositories.goaldb import GoalRepository
from src.infrastructure.services.card import CardService
from src.infrastructure.services.country import CountryService
from src.infrastructure.services.goal import GoalService


class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""
    country_repository = Singleton(CountryRepository)
    card_repository = Singleton(CardRepository)
    goal_repository = Singleton(GoalRepository)

    country_service = Factory(
        CountryService,
        repository=country_repository,
    )

    card_service = Factory(
        CardService,
        repository=card_repository
    )

    goal_service = Factory(
        GoalService,
        repository=goal_repository
    )