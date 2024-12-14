"""A module containing DTO models for output Matches."""
from typing import Optional, Iterable

from asyncpg import Record
from pydantic import BaseModel, ConfigDict

from src.infrastructure.dto.carddto import CardDTO
from src.infrastructure.dto.goaldto import GoalDTO


class MatchDTO(BaseModel):
    """A model representing DTO for match data."""
    id: int
    country_id: int
    league_id: int
    season: str
    stage: int
    date: str
    match_api_id: int
    home_team_api_id: int
    away_team_api_id: int
    home_team_goal: int
    away_team_goal: int
    home_player_1: Optional[int] = None
    home_player_2: Optional[int] = None
    home_player_3: Optional[int] = None
    home_player_4: Optional[int] = None
    home_player_5: Optional[int] = None
    home_player_6: Optional[int] = None
    home_player_7: Optional[int] = None
    home_player_8: Optional[int] = None
    home_player_9: Optional[int] = None
    home_player_10: Optional[int] = None
    home_player_11: Optional[int] = None
    away_player_1: Optional[int] = None
    away_player_2: Optional[int] = None
    away_player_3: Optional[int] = None
    away_player_4: Optional[int] = None
    away_player_5: Optional[int] = None
    away_player_6: Optional[int] = None
    away_player_7: Optional[int] = None
    away_player_8: Optional[int] = None
    away_player_9: Optional[int] = None
    away_player_10: Optional[int] = None
    away_player_11: Optional[int] = None
    goals: Optional[Iterable[GoalDTO]] = None
    cards: Optional[Iterable[CardDTO]] = None
    B365H: Optional[float] = None
    B365D: Optional[float] = None
    B365A: Optional[float] = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_record(cls, record: Record) -> "MatchDTO":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            MatchDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),
            country_id=record_dict.get("country_id"),
            league_id=record_dict.get("league_id"),
            season=record_dict.get("season"),
            stage=record_dict.get("stage"),
            date=record_dict.get("date"),
            match_api_id=record_dict.get("match_api_id"),
            home_team_api_id=record_dict.get("home_team_api_id"),
            away_team_api_id=record_dict.get("away_team_api_id"),
            home_team_goal=record_dict.get("home_team_goal"),
            away_team_goal=record_dict.get("away_team_goal"),
            home_player_1=record_dict.get("home_player_1"),
            home_player_2=record_dict.get("home_player_2"),
            home_player_3=record_dict.get("home_player_3"),
            home_player_4=record_dict.get("home_player_4"),
            home_player_5=record_dict.get("home_player_5"),
            home_player_6=record_dict.get("home_player_6"),
            home_player_7=record_dict.get("home_player_7"),
            home_player_8=record_dict.get("home_player_8"),
            home_player_9=record_dict.get("home_player_9"),
            home_player_10=record_dict.get("home_player_10"),
            home_player_11=record_dict.get("home_player_11"),
            away_player_1=record_dict.get("away_player_1"),
            away_player_2=record_dict.get("away_player_2"),
            away_player_3=record_dict.get("away_player_3"),
            away_player_4=record_dict.get("away_player_4"),
            away_player_5=record_dict.get("away_player_5"),
            away_player_6=record_dict.get("away_player_6"),
            away_player_7=record_dict.get("away_player_7"),
            away_player_8=record_dict.get("away_player_8"),
            away_player_9=record_dict.get("away_player_9"),
            away_player_10=record_dict.get("away_player_10"),
            away_player_11=record_dict.get("away_player_11"),
            goal=parse_goal_xml(record_dict.get("goal")),
            shoton=record_dict.get("shoton"),# TODO dodac shoton,shotoff i foulcommit tak jak goal wyżej^
            shotoff=record_dict.get("shotoff"),
            foulcommit=record_dict.get("foulcommit"),
            card=record_dict.get("card"),
            cross=record_dict.get("cross"),
            corner=record_dict.get("corner"),
            possession=record_dict.get("possession"),
            B365H=record_dict.get("B365H"),
            B365D=record_dict.get("B365D"),
            B365A=record_dict.get("B365A")

        )
