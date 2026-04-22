# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkerCreateParams"]


class WorkerCreateParams(TypedDict, total=False):
    input: Required[str]

    budget: Literal["low", "standard", "high", "unlimited"]

    stream: bool
