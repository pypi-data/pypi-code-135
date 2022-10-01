import tensorflow as tf
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2
import os

def convert (model, path, summary = False, as_text = False):
    full_model = tf.function (lambda x: model (x))
    full_model = full_model.get_concrete_function (tf.TensorSpec (model.inputs[0].shape, model.inputs[0].dtype))

    frozen_func = convert_variables_to_constants_v2 (full_model)
    frozen_func.graph.as_graph_def ()

    if summary:
        layers = [op.name for op in frozen_func.graph.get_operations ()]
        print("-" * 60)
        print("Frozen model layers: ")
        for layer in layers:
            print(layer)
        print("-" * 60)
        print("Frozen model inputs: ")
        print(frozen_func.inputs)
        print("Frozen model outputs: ")
        print(frozen_func.outputs)

    tf.io.write_graph(graph_or_graph_def = frozen_func.graph,
                    logdir = path,
                    name = "frozen_graph.pb",
                    as_text = as_text)

    return os.path.join (path, 'frozen_graph.pb')
