# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import pytest  # noqa: F401

import theseus as th

from .common import run_nonlinear_least_squares_check


def test_gauss_newton():
    run_nonlinear_least_squares_check(th.GaussNewton, {})
