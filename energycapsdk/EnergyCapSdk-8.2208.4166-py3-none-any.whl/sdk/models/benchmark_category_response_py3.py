# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BenchmarkCategoryResponse(Model):
    """BenchmarkCategoryResponse.

    :param benchmark_category_id: Benchmark Category Id
    :type benchmark_category_id: int
    :param benchmark_category_info: Benchmark Category Info
    :type benchmark_category_info: str
    """

    _attribute_map = {
        'benchmark_category_id': {'key': 'benchmarkCategoryId', 'type': 'int'},
        'benchmark_category_info': {'key': 'benchmarkCategoryInfo', 'type': 'str'},
    }

    def __init__(self, *, benchmark_category_id: int=None, benchmark_category_info: str=None, **kwargs) -> None:
        super(BenchmarkCategoryResponse, self).__init__(**kwargs)
        self.benchmark_category_id = benchmark_category_id
        self.benchmark_category_info = benchmark_category_info
