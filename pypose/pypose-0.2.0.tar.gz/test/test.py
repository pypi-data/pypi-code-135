import torch
from torch import nn
from torch.autograd.functional import jacobian
import pypose as pp


def aten_error_func(input):
    return pp.RxSO3(input) @ torch.randn(3)


def test_error():
    jacargs = {
        "vectorize": True,
        "strategy": "reverse-mode",
    }  # works when vectorize is False
    return jacobian(aten_error_func, torch.randn(5), **jacargs)


if __name__ == "__main__":
    print(test_error())