# Tisa-lab4-variant4

This repo is the Lab4 of Computational Process Organization in ITMO, 2022 spring.

### Futures with worker pool

In this variant, we implement a futures library . For that, we use done , progress, cancel, result, methods to run.

## Project structure description

* done() – return True if future evaluation is complete;

* InProgress() – return True if future evaluated right now;

* Result(timeout=None) return the future execution result (if the future is done);

  **–** raise the exception (if the future is done and raise an exception);

  **–** block until the future is done (if the timeout is None and future is not done);

  **–** raise TimeoutError after timeout (if the timeout is not None and the future is not done).

* •Cancel() – cancel a future (if the future not executed).


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

* `convert()`: Converts the original formula to a postfix expression.
* `visualize`: visualize dataflow. 
* `evaluate`: Evaluate result of the expression.

## Changelog

* 20.5.2022 - 2
  * update `README.md`
* 14.6.2022 - 1
  * update `futures.py` and `futures_test.py`
* 11.6.2022 - 0
  * Initial.

## Design notes

* The Python Futures module, located in concurrent.futures and asyncio, both represent operations with delays. Futures will wrap the operations in the waiting state and put them in the queue. The status of these operations can be queried at any time. Of course, their results (or exceptions) can also be obtained after the operation is completed. Using futures in some ways can greatly reduce time
