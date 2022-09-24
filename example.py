import os
import logging

from pflib import metric


file_name = os.path.basename(__file__)
log_file = f"/var/log/{file_name}.log"


logging.basicConfig(filename=log_file,
                    filemode='a',
                    format='[%(levelname)s.%(name)s %(asctime)s] %(message)s',
                    datefmt="%Y/%m/%d:%H:%M:%S",
                    level=logging.DEBUG)

logging.info(f"Script {file_name} start.")


my_metric = metric("metric:name1", "counter", "helpMetric", file_name)
my_metric.added_label({"label": "data1", "metric": "data"}, 1)
my_metric.added_label({"label": "data2", "metric": "data"}, 2)
my_metric2 = metric("metric:name2", "gauge", "helpMetric2", file_name)
my_metric2.added_label({}, 10)
my_metric.send()
my_metric2.send()

logging.info(f"Script {file_name} ended.")
