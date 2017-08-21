cwtimer
=======

'cwtimer' does one simple thing, track the timing of a 'with' statement block and report to AWS Cloudwatch.

Install
-------

.. code-block:: shell
 
    $ pip install cwtimer

Example
-------

.. code-block:: python

    from cwtimer import cwtimer
    import time
    
    with cwtimer(namespace='MyNameSpace', metric_name='MyMetric',
                 dimensions={'MyDimension': 'Value'}):
        time.sleep(1)
        # 1.0s reported to cloudwatch metric

Simpler
-------

.. code-block:: python

    from functools import partial
    from cwtimer import cwtimer
    import time

    mytimer = partial(
        cwtimer,
        namespace='MyNameSpace',
        metric_name='MyMetric',
        dimensions={'MyDimension': 'Value'},
    )

    with mytimer():
        time.sleep(1)
        # 1.0s reported
