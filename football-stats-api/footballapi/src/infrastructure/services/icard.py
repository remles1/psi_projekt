"""Module containing card service abstractions."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from abc import ABC, abstractmethod



class ICardService(ABC):
    """An abstract class representing protocol of card service."""

    @abstractmethod
    async def get_all_cards(self) -> Iterable[Any]:
        """The abstract getting all cards from the data storage.

        Returns:
            Iterable[Any]: Cards in the data storage.
        """

    @abstractmethod
    async def get_by_match(self, match_id: int) -> Iterable[Any]:
        """The abstract getting cards given in a certain match.

        Args:
            match_id (int): The id of the match.

        Returns:
            Iterable[Any]: Cards assigned to the match.
        """

    @abstractmethod
    async def get_by_player(self, player: int) -> Iterable[Any]:
        """The abstract getting airports assigned to particular continent.

        Args:
            player (int): The player_api_id of the player.

        Returns:
            Iterable[Any]: Every card given to a player.
        """

    @abstractmethod
    async def get_by_id(self, id: int) -> Any | None:
        """The abstract getting a card by provided id.

        Args:
            id (int): The id of the card.

        Returns:
            Any | None: The card details.
        """
