"""A module providing database access."""

import asyncio

import databases
import sqlalchemy
from sqlalchemy.exc import OperationalError, DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from asyncpg.exceptions import (  # type: ignore
    CannotConnectNowError,
    ConnectionDoesNotExistError,
)

from src.config import config

metadata = sqlalchemy.MetaData()

card_table = sqlalchemy.Table(
    "Card",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("match_id", sqlalchemy.Integer),
    sqlalchemy.Column("elapsed", sqlalchemy.Integer),
    sqlalchemy.Column("card_type", sqlalchemy.String),
    sqlalchemy.Column("player", sqlalchemy.Integer)
)

country_table = sqlalchemy.Table(
    "Country",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)

goal_table = sqlalchemy.Table(
    "Goal",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("match_id", sqlalchemy.Integer),
    sqlalchemy.Column("scorer", sqlalchemy.Integer),
    sqlalchemy.Column("assister", sqlalchemy.Integer),
    sqlalchemy.Column("elapsed", sqlalchemy.Integer),
    sqlalchemy.Column("team", sqlalchemy.Integer),
    sqlalchemy.Column("goal_type", sqlalchemy.String)
)

league_table = sqlalchemy.Table(
    "League",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("country_id", sqlalchemy.Integer),
    sqlalchemy.Column("name", sqlalchemy.String)
)

match_table = sqlalchemy.Table(
    "Match",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("country_id", sqlalchemy.Integer),
    sqlalchemy.Column("league_id", sqlalchemy.Integer),
    sqlalchemy.Column("season", sqlalchemy.String),
    sqlalchemy.Column("stage", sqlalchemy.Integer),
    sqlalchemy.Column("date", sqlalchemy.Integer),
    sqlalchemy.Column("match_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("home_team_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("away_team_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_1", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_2", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_3", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_4", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_5", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_6", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_7", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_8", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_9", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_10", sqlalchemy.Integer),
    sqlalchemy.Column("home_player_11", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_1", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_2", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_3", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_4", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_5", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_6", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_7", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_8", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_9", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_10", sqlalchemy.Integer),
    sqlalchemy.Column("away_player_11", sqlalchemy.Integer),
    sqlalchemy.Column("B365H", sqlalchemy.Integer),
    sqlalchemy.Column("B365D", sqlalchemy.Integer),
    sqlalchemy.Column("B365A", sqlalchemy.Integer)
)

player_table = sqlalchemy.Table(
    "Player",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("player_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("player_name", sqlalchemy.String),
    sqlalchemy.Column("player_fifa_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("birthday", sqlalchemy.String),
    sqlalchemy.Column("height", sqlalchemy.Integer),
    sqlalchemy.Column("weight", sqlalchemy.Integer)
)

player_attributes_table = None #TODO

team_table = sqlalchemy.Table(
    "Team",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("team_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("team_fifa_api_id", sqlalchemy.Integer),
    sqlalchemy.Column("team_long_name", sqlalchemy.String),
    sqlalchemy.Column("team_short_name", sqlalchemy.String)
)

team_attributes_table = None #TODO

db_uri = (
    f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}/{config.DB_NAME}"
)

engine = create_async_engine(
    db_uri,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

database = databases.Database(
    db_uri,
    force_rollback=True,
)


async def init_db(retries: int = 5, delay: int = 5) -> None:
    """Function initializing the DB.

    Args:
        retries (int, optional): Number of retries of connect to DB.
            Defaults to 5.
        delay (int, optional): Delay of connect do DB. Defaults to 2.
    """
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.execute(sqlalchemy.text("SELECT 1"))
            return
        except (
                OperationalError,
                DatabaseError,
                CannotConnectNowError,
                ConnectionRefusedError,
                ConnectionDoesNotExistError,
        ) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(delay)

    raise ConnectionError("Could not connect to DB after several retries.")
