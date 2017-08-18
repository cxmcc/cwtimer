
import boto3
import logging
import time


class cwtimer:
    def __init__(self, namespace=None, metric_name=None, dimensions={},
                 report_on_failure=False, **kwargs):
        self.report_on_failure = report_on_failure
        assert namespace
        assert metric_name
        assert dimensions
        self.namespace = namespace
        self.metric_name = metric_name
        self.dimensions = [
            {'Name': n, 'Value': v} for n, v in dimensions.items()
        ]
        self.cw = boto3.client('cloudwatch', **kwargs)
        self._logger = logging.getLogger('cwtimer')

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.report_on_failure and exc_type is not None:
            return
        self.end = time.time()
        self.interval = self.end - self.start
        metric_data = {
            'MetricName': self.metric_name,
            'Dimensions': self.dimensions,
            'Value': self.interval,
            'Unit': 'Seconds',
        }
        try:
            self.cw.put_metric_data(
                Namespace=self.namespace,
                MetricData=[metric_data],
            )
        except Exception:
            self._logger.exception('Failed to report timing metrics.')
