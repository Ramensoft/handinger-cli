# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ScheduleCreateParams",
    "When",
    "WhenUnionMember0",
    "WhenUnionMember1",
    "WhenUnionMember2",
    "WhenUnionMember3",
]


class ScheduleCreateParams(TypedDict, total=False):
    input: Required[str]

    when: Required[When]

    budget: Literal["low", "standard", "high", "unlimited"]


class WhenUnionMember0(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    type: Required[Literal["scheduled"]]


class WhenUnionMember1(TypedDict, total=False):
    delay_in_seconds: Required[Annotated[int, PropertyInfo(alias="delayInSeconds")]]

    type: Required[Literal["delayed"]]


class WhenUnionMember2(TypedDict, total=False):
    cron: Required[str]

    type: Required[Literal["cron"]]


class WhenUnionMember3(TypedDict, total=False):
    interval_seconds: Required[Annotated[int, PropertyInfo(alias="intervalSeconds")]]

    type: Required[Literal["interval"]]


When: TypeAlias = Union[WhenUnionMember0, WhenUnionMember1, WhenUnionMember2, WhenUnionMember3]
