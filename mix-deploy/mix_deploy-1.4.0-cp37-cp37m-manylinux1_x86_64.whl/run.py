import mix_deploy
import numpy as np
from functools import reduce
import argparse

def set_arg():
    parser = argparse.ArgumentParser(description='mix_stc_infer args info')
    parser.add_argument('--repeat', dest='REPEAT', default=100, type=int, help='repeat times of the model (default 100)')
    parser.add_argument('--config', dest='CONFIG', type=str, required=True, help='config json path of the model')
    parser.add_argument('--thread_num', dest='THREAD_NUM', type=int, default=8, help='how many thread to create (default = 8)')
    parser.add_argument('--profiling', dest='PROFILING', action='store_true',  help='whether use profiler')
    return parser

if __name__ == '__main__':
    parser = set_arg()
    arg_class = parser.parse_args()
    config_json = arg_class.CONFIG
    thread_num = arg_class.THREAD_NUM
    repeat = arg_class.REPEAT
    profiling = arg_class.PROFILING
    throughput = 0
    latency = 0
    cycle = 0
    stc_infer = mix_deploy.STCInference(config_json, thread_num)

    input_info_list = stc_infer.GetInputInfo()
    input_dtype_list = stc_infer.GetDtype()
    input_dict = {}
    for index, input_info in enumerate(input_info_list):
        input_dtype = input_dtype_list[index]
        input_name, input_shape = input_info
        input_shape_size = reduce(lambda x, y : x * y, input_shape)
        input_dict[input_name] = np.random.rand(input_shape_size).astype(input_dtype).reshape(input_shape)

    tvm_out = stc_infer.Run(input_dict, repeat = repeat, profiling = profiling)
    cycle = stc_infer.GetCycle()
    latency = stc_infer.GetLatency()
    throughput = stc_infer.GetThroughput()

    print(tvm_out)
    print('npu cycle:', cycle)
    print('latency:', latency)
    print('throughput:', throughput)
