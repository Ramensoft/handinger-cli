# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Worker", "File", "Output", "OutputContent", "Source", "Costs", "Usage"]


class File(BaseModel):
    filename: Optional[str] = None

    media_type: str = FieldInfo(alias="mediaType")

    url: str


class OutputContent(BaseModel):
    text: str

    type: Literal["output_text"]


class Output(BaseModel):
    id: str

    content: List[OutputContent]

    role: Literal["assistant"]

    status: Literal["completed"]

    type: Literal["message"]


class Source(BaseModel):
    id: str

    title: Optional[str] = None

    type: Literal["url"]

    url: str


class Costs(BaseModel):
    internal_cost_usd: float = FieldInfo(alias="internalCostUsd")

    api_model_cost_usd: float = FieldInfo(alias="modelCostUsd")

    sandbox_cost_usd: float = FieldInfo(alias="sandboxCostUsd")

    tool_cost_usd: float = FieldInfo(alias="toolCostUsd")


class Usage(BaseModel):
    cache_read_tokens: int = FieldInfo(alias="cacheReadTokens")

    cache_write_tokens: int = FieldInfo(alias="cacheWriteTokens")

    cost_usd: float = FieldInfo(alias="costUsd")

    input_tokens: int = FieldInfo(alias="inputTokens")

    output_tokens: int = FieldInfo(alias="outputTokens")

    reasoning_tokens: int = FieldInfo(alias="reasoningTokens")

    steps: int

    total_tokens: int = FieldInfo(alias="totalTokens")

    credits: Optional[int] = None


class Worker(BaseModel):
    id: str

    created_at: Optional[int] = None

    error: None = None

    files: List[File]

    incomplete_details: None = None

    messages: List[object]

    metadata: Dict[str, object]

    object: Literal["worker"]

    output: List[Output]

    output_text: str

    running: bool

    sources: List[Source]

    status: Literal["running", "completed", "pending"]

    costs: Optional[Costs] = None

    usage: Optional[Usage] = None
