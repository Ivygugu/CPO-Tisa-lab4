# Tisa - lab4 - variant4

This repo is the Lab4 of Computational Process Organization in ITMO, 2022 spring.

## Futures with worker pool

In this variant, we implement a futures library. For that, we use
`done`, `progress`, `cancel`, `result`, `methods` to run.

## Project structure description

- `futures.py` -- includes `done`, `progress`, `cancel`, `result`, `methods`

- `futures_test.py`

## Contribution

* Chen Biao(1377681089@qq.com)
  * Implement the `futures.py`
  * Write `README.md`
  * Source code framework construction

* Guo Zhaoxin(zhaoxin_guo@163.com)
  * Implement the `futures_test.py`
  * Write `README.md`
  * Created GitHub repository

## Features

* `IsDone()`:  return True if future evaluation is complete.

* `InProgress()`: return True if future evaluated right now.

* `Result`:  return the future execution result (if the future is done);

  * raise the exception (if the future is done and raise an exception);

  * block until the future is done (if the timeout is None and future is not done);

  * raise TimeoutError after timeout (if the timeout is not None
  and the future is not done).

* `Cancel()`:  cancel a future (if the future not executed).

## Changelog

* 17.6.2022 - 2
  * update `README.md`
* 16.6.2022 - 1
  * update `futures.py` and `futures_test.py`
* 16.6.2022 - 0
  * Initial.

## Design notes

* The Python Futures module, located in concurrent.
* Futures represent operations with delays. 
* Futures will wrap the operations in the waiting state and put them in the queue.
* The status of these operations can be queried at any time.
* The results (or exceptions) can also be obtained after the operationis completed.
* Using futures in some ways can greatly reduce time.
