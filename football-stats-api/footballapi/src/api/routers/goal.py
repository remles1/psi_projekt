"""A module containing country endpoints."""

from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.goal import Goal
from src.infrastructure.dto.goaldto import GoalDTO
from src.infrastructure.services.icountry import ICountryService
from src.infrastructure.services.igoal import IGoalService

router = APIRouter()


@router.get("/all", response_model=Iterable[Goal], status_code=200)
@inject
async def get_all_goals(
        service: IGoalService = Depends(Provide[Container.goal_service]),
) -> Iterable:
    """An endpoint for getting all goals. (HUGE AMOUNT)

    Args:
        service (IGoalService): The injected service dependency.

    Returns:
        Iterable: The goal attributes collection.
    """

    goals = await service.get_all_goals()

    return goals


@router.get("/{match_id}", response_model=Iterable[GoalDTO], status_code=200)
@inject
async def get_goals_by_match(
        match_id: int,
        service: IGoalService = Depends(Provide[Container.goal_service]),
) -> Iterable:
    """An endpoint for getting all countries.

    Args:
        match_id (int): The id of the match.
        service (ICountryService, optional): The injected service dependency.

    Returns:
        Iterable: The country attributes collection.
    """

    goals = await service.get_by_match(match_id)

    return goals
