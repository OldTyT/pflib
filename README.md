# Python3 pushgateway library

## About

Python3 library with functions for sending metrics to `Pushgateway`.

## Install

```
pip install pflib
```

## Usage


Metric:

| Function          | Args needed                                  | Description                                                                       |
|-------------------|----------------------------------------------|-----------------------------------------------------------------------------------|
| `added_label`     | `label`(dict), `value`(any, only is decimal) | Added metric.                                                                     |
| `send`            | `none`                                       | Sends metrics from temporary file to Pushgateway and deletes the file afterwards. |
| `validate_metric` | `none`                                       | This functions use to validate metric.                                            |
| `__init__`        | `name`, `type`, `help`, `script_name`(job)   | Initializing metric. Type - all `str`.                                            |
| `__str__`         | `none`                                       | Printing metric in pushgateway format.                                            |

### Examples

Please check `example.py`

### How to use

#### Edit metric

```python
import os

from pflib import metric

file_name = os.path.basename(__file__)

my_metric = metric("metric:name1", "counter", "helpMetric", file_name)
print(my_metric.name)

# Printing - metric:name1

my_metric.name = "example"
print(my_metric.name)

# Printing - example

# For more check pls pf.py def __init__
```
