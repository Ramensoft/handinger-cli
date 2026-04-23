# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import worker_create_params, worker_continue_params, worker_retrieve_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.worker import Worker
from ...types.worker_stream_updates_response import WorkerStreamUpdatesResponse

__all__ = ["WorkersResource", "AsyncWorkersResource"]


class WorkersResource(SyncAPIResource):
    @cached_property
    def schedules(self) -> SchedulesResource:
        """Manage future and recurring worker tasks."""
        return SchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ramensoft/handinger-cli#accessing-raw-response-data-eg-headers
        """
        return WorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ramensoft/handinger-cli#with_streaming_response
        """
        return WorkersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: str,
        budget: Literal["low", "standard", "high", "unlimited"] | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """
        Create a new agent worker and start it with the supplied instruction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/workers",
            body=maybe_transform(
                {
                    "input": input,
                    "budget": budget,
                    "stream": stream,
                },
                worker_create_params.WorkerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Worker,
        )

    def retrieve(
        self,
        worker_id: str,
        *,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """Retrieve the current worker state.

        Pass stream=true or request text/event-stream
        to subscribe to updates.

        Args:
          stream: Return a server-sent event stream instead of JSON.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._get(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"stream": stream}, worker_retrieve_params.WorkerRetrieveParams),
            ),
            cast_to=Worker,
        )

    def continue_(
        self,
        worker_id: str,
        *,
        input: str,
        budget: Literal["low", "standard", "high", "unlimited"] | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """
        Send another instruction to an existing worker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._post(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            body=maybe_transform(
                {
                    "input": input,
                    "budget": budget,
                    "stream": stream,
                },
                worker_continue_params.WorkerContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Worker,
        )

    def retrieve_email(
        self,
        worker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Retrieve the inbound email address for a worker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._get(
            path_template("/api/workers/{worker_id}/email", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def retrieve_file(
        self,
        file_path: str,
        *,
        worker_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Retrieve a file published from a worker workspace.

        The runtime route accepts
        nested paths after /files/.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        if not file_path:
            raise ValueError(f"Expected a non-empty value for `file_path` but received {file_path!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template("/api/workers/{worker_id}/files/{file_path}", worker_id=worker_id, file_path=file_path),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def stream_updates(
        self,
        worker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[WorkerStreamUpdatesResponse]:
        """
        Subscribe to a worker using server-sent events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template("/api/workers/{worker_id}/stream", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[WorkerStreamUpdatesResponse],
        )


class AsyncWorkersResource(AsyncAPIResource):
    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        """Manage future and recurring worker tasks."""
        return AsyncSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ramensoft/handinger-cli#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ramensoft/handinger-cli#with_streaming_response
        """
        return AsyncWorkersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: str,
        budget: Literal["low", "standard", "high", "unlimited"] | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """
        Create a new agent worker and start it with the supplied instruction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/workers",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "budget": budget,
                    "stream": stream,
                },
                worker_create_params.WorkerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Worker,
        )

    async def retrieve(
        self,
        worker_id: str,
        *,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """Retrieve the current worker state.

        Pass stream=true or request text/event-stream
        to subscribe to updates.

        Args:
          stream: Return a server-sent event stream instead of JSON.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._get(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"stream": stream}, worker_retrieve_params.WorkerRetrieveParams),
            ),
            cast_to=Worker,
        )

    async def continue_(
        self,
        worker_id: str,
        *,
        input: str,
        budget: Literal["low", "standard", "high", "unlimited"] | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """
        Send another instruction to an existing worker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._post(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            body=await async_maybe_transform(
                {
                    "input": input,
                    "budget": budget,
                    "stream": stream,
                },
                worker_continue_params.WorkerContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Worker,
        )

    async def retrieve_email(
        self,
        worker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Retrieve the inbound email address for a worker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._get(
            path_template("/api/workers/{worker_id}/email", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def retrieve_file(
        self,
        file_path: str,
        *,
        worker_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Retrieve a file published from a worker workspace.

        The runtime route accepts
        nested paths after /files/.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        if not file_path:
            raise ValueError(f"Expected a non-empty value for `file_path` but received {file_path!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/api/workers/{worker_id}/files/{file_path}", worker_id=worker_id, file_path=file_path),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def stream_updates(
        self,
        worker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[WorkerStreamUpdatesResponse]:
        """
        Subscribe to a worker using server-sent events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/api/workers/{worker_id}/stream", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[WorkerStreamUpdatesResponse],
        )


class WorkersResourceWithRawResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

        self.create = to_raw_response_wrapper(
            workers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workers.retrieve,
        )
        self.continue_ = to_raw_response_wrapper(
            workers.continue_,
        )
        self.retrieve_email = to_raw_response_wrapper(
            workers.retrieve_email,
        )
        self.retrieve_file = to_custom_raw_response_wrapper(
            workers.retrieve_file,
            BinaryAPIResponse,
        )
        self.stream_updates = to_raw_response_wrapper(
            workers.stream_updates,
        )

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        """Manage future and recurring worker tasks."""
        return SchedulesResourceWithRawResponse(self._workers.schedules)


class AsyncWorkersResourceWithRawResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

        self.create = async_to_raw_response_wrapper(
            workers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workers.retrieve,
        )
        self.continue_ = async_to_raw_response_wrapper(
            workers.continue_,
        )
        self.retrieve_email = async_to_raw_response_wrapper(
            workers.retrieve_email,
        )
        self.retrieve_file = async_to_custom_raw_response_wrapper(
            workers.retrieve_file,
            AsyncBinaryAPIResponse,
        )
        self.stream_updates = async_to_raw_response_wrapper(
            workers.stream_updates,
        )

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        """Manage future and recurring worker tasks."""
        return AsyncSchedulesResourceWithRawResponse(self._workers.schedules)


class WorkersResourceWithStreamingResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

        self.create = to_streamed_response_wrapper(
            workers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workers.retrieve,
        )
        self.continue_ = to_streamed_response_wrapper(
            workers.continue_,
        )
        self.retrieve_email = to_streamed_response_wrapper(
            workers.retrieve_email,
        )
        self.retrieve_file = to_custom_streamed_response_wrapper(
            workers.retrieve_file,
            StreamedBinaryAPIResponse,
        )
        self.stream_updates = to_streamed_response_wrapper(
            workers.stream_updates,
        )

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        """Manage future and recurring worker tasks."""
        return SchedulesResourceWithStreamingResponse(self._workers.schedules)


class AsyncWorkersResourceWithStreamingResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

        self.create = async_to_streamed_response_wrapper(
            workers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workers.retrieve,
        )
        self.continue_ = async_to_streamed_response_wrapper(
            workers.continue_,
        )
        self.retrieve_email = async_to_streamed_response_wrapper(
            workers.retrieve_email,
        )
        self.retrieve_file = async_to_custom_streamed_response_wrapper(
            workers.retrieve_file,
            AsyncStreamedBinaryAPIResponse,
        )
        self.stream_updates = async_to_streamed_response_wrapper(
            workers.stream_updates,
        )

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """Manage future and recurring worker tasks."""
        return AsyncSchedulesResourceWithStreamingResponse(self._workers.schedules)
