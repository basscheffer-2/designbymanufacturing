import numpy as np
import json
from input_series import *


def design(**kwargs):
    params = json.load("design_defaults.json")
    params.update(kwargs)

    return _vase_v1(**params)


def _vase_v1(**kwargs):
    # make dia series
    height = np.random.rand()*kwargs["max-height"]
    layers = height//kwargs["layer-height"]
    sel_inp = ["smoothness", "max-angle", "max-width", "min-base-width", "noise"]
    dia_array = random_line(layers, *(kwargs[k] for k in sel_inp))

    # make polygon sequence

    # make loft