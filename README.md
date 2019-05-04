# Choreo

Robust, reliable and resilient distributed workflow engine.
Uses [Redis](https://redis.io/) as the message broker and result backend.

## Features

* Enqueued task
* Scheduled task
* Task dependency
* Fairness
* Deduplication
* Retry mechanism
* Resilience to crash
* Transparency, inspection and monitoring

## Guiding principles (Don'ts)

* DB polling
* Visibility timeouts
* Late ACKs
* Prefetch tasks
* Worker heartbeat
