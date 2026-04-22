# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from handinger import Handinger, AsyncHandinger
from tests.utils import assert_matches_type
from handinger._utils import parse_datetime
from handinger.types.workers import WorkerSchedule, ScheduleListResponse, ScheduleCancelResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Handinger) -> None:
        schedule = client.workers.schedules.create(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            when={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "scheduled",
            },
        )
        assert_matches_type(WorkerSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Handinger) -> None:
        schedule = client.workers.schedules.create(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            when={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "scheduled",
            },
            budget="low",
        )
        assert_matches_type(WorkerSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Handinger) -> None:
        response = client.workers.schedules.with_raw_response.create(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            when={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "scheduled",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(WorkerSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Handinger) -> None:
        with client.workers.schedules.with_streaming_response.create(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            when={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "scheduled",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(WorkerSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.schedules.with_raw_response.create(
                worker_id="",
                input="x",
                when={
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "type": "scheduled",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Handinger) -> None:
        schedule = client.workers.schedules.list(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Handinger) -> None:
        response = client.workers.schedules.with_raw_response.list(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Handinger) -> None:
        with client.workers.schedules.with_streaming_response.list(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.schedules.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Handinger) -> None:
        schedule = client.workers.schedules.cancel(
            schedule_id="sch_01HZY31W2SZJ8MJ2FQTR3M1K9D",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Handinger) -> None:
        response = client.workers.schedules.with_raw_response.cancel(
            schedule_id="sch_01HZY31W2SZJ8MJ2FQTR3M1K9D",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Handinger) -> None:
        with client.workers.schedules.with_streaming_response.cancel(
            schedule_id="sch_01HZY31W2SZJ8MJ2FQTR3M1K9D",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.schedules.with_raw_response.cancel(
                schedule_id="sch_01HZY31W2SZJ8MJ2FQTR3M1K9D",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.workers.schedules.with_raw_response.cancel(
                schedule_id="",
                worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            )


class TestAsyncSchedules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHandinger) -> None:
        schedule = await async_client.workers.schedules.create(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            when={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "scheduled",
            },
        )
        assert_matches_type(WorkerSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHandinger) -> None:
        schedule = await async_client.workers.schedules.create(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            when={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "scheduled",
            },
            budget="low",
        )
        assert_matches_type(WorkerSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.schedules.with_raw_response.create(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            when={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "scheduled",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(WorkerSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.schedules.with_streaming_response.create(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            input="x",
            when={
                "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "scheduled",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(WorkerSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.schedules.with_raw_response.create(
                worker_id="",
                input="x",
                when={
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "type": "scheduled",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHandinger) -> None:
        schedule = await async_client.workers.schedules.list(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.schedules.with_raw_response.list(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.schedules.with_streaming_response.list(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.schedules.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncHandinger) -> None:
        schedule = await async_client.workers.schedules.cancel(
            schedule_id="sch_01HZY31W2SZJ8MJ2FQTR3M1K9D",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.schedules.with_raw_response.cancel(
            schedule_id="sch_01HZY31W2SZJ8MJ2FQTR3M1K9D",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.schedules.with_streaming_response.cancel(
            schedule_id="sch_01HZY31W2SZJ8MJ2FQTR3M1K9D",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.schedules.with_raw_response.cancel(
                schedule_id="sch_01HZY31W2SZJ8MJ2FQTR3M1K9D",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.workers.schedules.with_raw_response.cancel(
                schedule_id="",
                worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            )
