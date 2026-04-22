# Workers

Types:

```python
from handinger.types import (
    CreateWorker,
    Worker,
    WorkerRetrieveEmailResponse,
    WorkerStreamUpdatesResponse,
)
```

Methods:

- <code title="post /api/workers">client.workers.<a href="./src/handinger/resources/workers/workers.py">create</a>(\*\*<a href="src/handinger/types/worker_create_params.py">params</a>) -> <a href="./src/handinger/types/worker.py">Worker</a></code>
- <code title="get /api/workers/{workerId}">client.workers.<a href="./src/handinger/resources/workers/workers.py">retrieve</a>(worker_id, \*\*<a href="src/handinger/types/worker_retrieve_params.py">params</a>) -> <a href="./src/handinger/types/worker.py">Worker</a></code>
- <code title="post /api/workers/{workerId}">client.workers.<a href="./src/handinger/resources/workers/workers.py">continue\_</a>(worker_id, \*\*<a href="src/handinger/types/worker_continue_params.py">params</a>) -> <a href="./src/handinger/types/worker.py">Worker</a></code>
- <code title="get /api/workers/{workerId}/email">client.workers.<a href="./src/handinger/resources/workers/workers.py">retrieve_email</a>(worker_id) -> str</code>
- <code title="get /api/workers/{workerId}/files/{filePath}">client.workers.<a href="./src/handinger/resources/workers/workers.py">retrieve_file</a>(file_path, \*, worker_id) -> BinaryAPIResponse</code>
- <code title="get /api/workers/{workerId}/stream">client.workers.<a href="./src/handinger/resources/workers/workers.py">stream_updates</a>(worker_id) -> str</code>

## Schedules

Types:

```python
from handinger.types.workers import WorkerSchedule, ScheduleListResponse, ScheduleCancelResponse
```

Methods:

- <code title="post /api/workers/{workerId}/schedules">client.workers.schedules.<a href="./src/handinger/resources/workers/schedules.py">create</a>(worker_id, \*\*<a href="src/handinger/types/workers/schedule_create_params.py">params</a>) -> <a href="./src/handinger/types/workers/worker_schedule.py">WorkerSchedule</a></code>
- <code title="get /api/workers/{workerId}/schedules">client.workers.schedules.<a href="./src/handinger/resources/workers/schedules.py">list</a>(worker_id) -> <a href="./src/handinger/types/workers/schedule_list_response.py">ScheduleListResponse</a></code>
- <code title="delete /api/workers/{workerId}/schedules/{scheduleId}">client.workers.schedules.<a href="./src/handinger/resources/workers/schedules.py">cancel</a>(schedule_id, \*, worker_id) -> <a href="./src/handinger/types/workers/schedule_cancel_response.py">ScheduleCancelResponse</a></code>
