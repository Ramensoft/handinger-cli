# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WorkerSchedule", "UnionMember0", "UnionMember1", "UnionMember2", "UnionMember3"]


class UnionMember0(BaseModel):
    id: str

    budget: Literal["low", "standard", "high", "unlimited"]

    input: str

    next_run_at: datetime = FieldInfo(alias="nextRunAt")

    type: Literal["scheduled"]


class UnionMember1(BaseModel):
    id: str

    budget: Literal["low", "standard", "high", "unlimited"]

    delay_in_seconds: int = FieldInfo(alias="delayInSeconds")

    input: str

    next_run_at: datetime = FieldInfo(alias="nextRunAt")

    type: Literal["delayed"]


class UnionMember2(BaseModel):
    id: str

    budget: Literal["low", "standard", "high", "unlimited"]

    cron: str

    input: str

    next_run_at: datetime = FieldInfo(alias="nextRunAt")

    type: Literal["cron"]


class UnionMember3(BaseModel):
    id: str

    budget: Literal["low", "standard", "high", "unlimited"]

    input: str

    interval_seconds: int = FieldInfo(alias="intervalSeconds")

    next_run_at: datetime = FieldInfo(alias="nextRunAt")

    type: Literal["interval"]


WorkerSchedule: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3]
