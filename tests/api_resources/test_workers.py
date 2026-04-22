# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from handinger import Handinger, AsyncHandinger
from tests.utils import assert_matches_type
from handinger.types import (
    Worker,
)
from handinger._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Handinger) -> None:
        worker = client.workers.create(
            input="x",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Handinger) -> None:
        worker = client.workers.create(
            input="x",
            budget="low",
            stream=True,
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.create(
            input="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.create(
            input="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Handinger) -> None:
        worker = client.workers.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Handinger) -> None:
        worker = client.workers.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            stream=True,
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.retrieve(
                worker_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_continue(self, client: Handinger) -> None:
        worker = client.workers.continue_(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_continue_with_all_params(self, client: Handinger) -> None:
        worker = client.workers.continue_(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            budget="low",
            stream=True,
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_continue(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.continue_(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_continue(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.continue_(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_continue(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.continue_(
                worker_id="",
                input="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_email(self, client: Handinger) -> None:
        worker = client.workers.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(str, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_email(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(str, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_email(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(str, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_email(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.retrieve_email(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_file(self, client: Handinger, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/workers/t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM/files/scratchpad/plan.md").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        worker = client.workers.retrieve_file(
            file_path="scratchpad/plan.md",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert worker.is_closed
        assert worker.json() == {"foo": "bar"}
        assert cast(Any, worker.is_closed) is True
        assert isinstance(worker, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_file(self, client: Handinger, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/workers/t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM/files/scratchpad/plan.md").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        worker = client.workers.with_raw_response.retrieve_file(
            file_path="scratchpad/plan.md",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert worker.is_closed is True
        assert worker.http_request.headers.get("X-Stainless-Lang") == "python"
        assert worker.json() == {"foo": "bar"}
        assert isinstance(worker, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_file(self, client: Handinger, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/workers/t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM/files/scratchpad/plan.md").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.workers.with_streaming_response.retrieve_file(
            file_path="scratchpad/plan.md",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as worker:
            assert not worker.is_closed
            assert worker.http_request.headers.get("X-Stainless-Lang") == "python"

            assert worker.json() == {"foo": "bar"}
            assert cast(Any, worker.is_closed) is True
            assert isinstance(worker, StreamedBinaryAPIResponse)

        assert cast(Any, worker.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve_file(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.retrieve_file(
                file_path="scratchpad/plan.md",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            client.workers.with_raw_response.retrieve_file(
                file_path="",
                worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_updates(self, client: Handinger) -> None:
        worker_stream = client.workers.stream_updates(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        worker_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_updates(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.stream_updates(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_updates(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.stream_updates(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream_updates(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.stream_updates(
                "",
            )


class TestAsyncWorkers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.create(
            input="x",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.create(
            input="x",
            budget="low",
            stream=True,
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.create(
            input="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.create(
            input="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            stream=True,
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.retrieve(
                worker_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_continue(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.continue_(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_continue_with_all_params(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.continue_(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            budget="low",
            stream=True,
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_continue(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.continue_(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_continue(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.continue_(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_continue(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.continue_(
                worker_id="",
                input="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_email(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(str, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_email(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(str, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_email(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(str, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_email(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.retrieve_email(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_file(self, async_client: AsyncHandinger, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/workers/t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM/files/scratchpad/plan.md").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        worker = await async_client.workers.retrieve_file(
            file_path="scratchpad/plan.md",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert worker.is_closed
        assert await worker.json() == {"foo": "bar"}
        assert cast(Any, worker.is_closed) is True
        assert isinstance(worker, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_file(self, async_client: AsyncHandinger, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/workers/t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM/files/scratchpad/plan.md").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        worker = await async_client.workers.with_raw_response.retrieve_file(
            file_path="scratchpad/plan.md",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert worker.is_closed is True
        assert worker.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await worker.json() == {"foo": "bar"}
        assert isinstance(worker, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_file(self, async_client: AsyncHandinger, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/workers/t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM/files/scratchpad/plan.md").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.workers.with_streaming_response.retrieve_file(
            file_path="scratchpad/plan.md",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as worker:
            assert not worker.is_closed
            assert worker.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await worker.json() == {"foo": "bar"}
            assert cast(Any, worker.is_closed) is True
            assert isinstance(worker, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, worker.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve_file(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.retrieve_file(
                file_path="scratchpad/plan.md",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            await async_client.workers.with_raw_response.retrieve_file(
                file_path="",
                worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_updates(self, async_client: AsyncHandinger) -> None:
        worker_stream = await async_client.workers.stream_updates(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        await worker_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_updates(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.stream_updates(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_updates(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.stream_updates(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream_updates(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.stream_updates(
                "",
            )
