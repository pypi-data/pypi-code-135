""" jouissance.pt.arch """

import numpy as np
import torch


class DownSample(torch.nn.Module):
    """ a downsampling block """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        _in, filters, size,
        stride=2, apply_batchnorm=True, drop_rate=0.0
    ):
        """ definitions """

        super().__init__()

        self.main = torch.nn.Sequential()

        self.main.add_module(
            "conv2d",
            torch.nn.Conv2d(
                _in, filters, size, stride=stride, padding=(1, 1), bias=False
            )
        )

        if apply_batchnorm:
            self.main.add_module(
                "batchnorm2d",
                torch.nn.BatchNorm2d(filters)
            )

        if drop_rate > 0:
            self.main.add_module(
                "drop",
                torch.nn.Dropout2d(drop_rate)
            )

        self.main.add_module(
            "act",
            torch.nn.PReLU()
        )

    def forward(self, _input):
        """ move """

        return self.main(_input)


class UpSample(torch.nn.Module):
    """ an upsampling block """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        _in,
        stride=2, drop_rate=0.0, act="normal"
    ):
        """ definitions """

        super().__init__()

        self.main = torch.nn.Sequential()

        self.main.add_module(
            "upsample",
            torch.nn.Upsample(
                scale_factor=stride, mode="bilinear",
            )
        )

        self.main.add_module(
            "batchnorm2d",
            torch.nn.BatchNorm2d(_in)
        )

        if drop_rate > 0:
            self.main.add_module(
                "dropout",
                torch.nn.Dropout2d(drop_rate)
            )

        if act == "exit":
            self.main.add_module(
                "tanh",
                torch.nn.Tanh()
            )
        else:
            self.main.add_module(
                "prelu",
                torch.nn.PReLU()
            )

    def forward(self, _input):
        """ move """

        return self.main(_input)


class DenseDisc(torch.nn.Module):
    """ dense disc """

    def __init__(
        self,
        conditions_shape=(3, 128, 256),
        scenes_shape=(1, 128, 256),
    ):
        """ defs """
        super().__init__()
        self.conditions_shape = conditions_shape
        self.scenes_shape = scenes_shape

    def forward(self, _con, _sce):
        """ move """
        # pylint: disable=no-member
        hold = _con
        if self.conditions_shape[1] != self.scenes_shape[1] \
                or self.conditions_shape[2] != self.scenes_shape[2]:
            hold = UpSample(
                self.conditions_shape[0],
                stride=(
                    self.scenes_shape[1]//self.conditions_shape[1],
                    self.scenes_shape[2]//self.conditions_shape[2]
                )
            )(_con)

        _input = torch.cat([_sce, hold], axis=1)
        _out = torch.nn.BatchNorm2d(
            self.conditions_shape[0]+self.scenes_shape[0])(_input)
        steps = int(np.log2(np.min(
            [self.scenes_shape[1], self.scenes_shape[2]])))
        feats = self.conditions_shape[0]+self.scenes_shape[0]
        for _ in range(steps):
            _out = DownSample(
                feats,
                filters=64, size=3, drop_rate=0.2, stride=2,
                apply_batchnorm=False,
            )(_out)
            feats = 64
            _res = _out
            _out = DownSample(
                feats,
                filters=64, size=3, drop_rate=0.2, stride=1,
                apply_batchnorm=False,
            )(_out)
            _out = torch.add(_res, _out)
            _out = torch.nn.BatchNorm2d(feats)(_out)

        _out = torch.nn.Flatten()(_out)
        _out = torch.nn.Dropout(0.2)(_out)

        _out = torch.nn.LazyLinear(1, dtype=torch.float32)(_out)

        _out = torch.nn.Tanh()(_out)

        return _out


class UNetModel(torch.nn.Module):
    """ a unet-like generation model """

    def __init__(
        self,
        conditions_shape=(3, 128, 256),
        scenes_shape=(1, 128, 256),
        use_latent=True,
    ):
        """ defs """
        super().__init__()
        self.conditions_shape = conditions_shape
        self.scenes_shape = scenes_shape
        self.use_latent = use_latent

    def forward(self, _con, _lat=None):
        """ move """
        # pylint: disable=no-member
        _input = _con
        if self.use_latent:
            if _lat is None:
                raise ValueError("latent var is requires")
            _input = torch.cat([_con, _lat], axis=1)
        skips = []
        steps = int(np.log2(np.min(
            [self.conditions_shape[-2], self.conditions_shape[-1]]
        )))
        feats = self.conditions_shape[0] + \
            self.conditions_shape[0] * (self.use_latent)
        _out = _input
        for _ in range(steps):
            _out = DownSample(
                feats,
                filters=64, size=3, drop_rate=0.2, stride=2)(_out)
            feats = 64
            _res = _out
            _out = DownSample(
                feats,
                filters=64, size=3, stride=1)(_out)
            _out = torch.add(_res, _out)
            skips.append(_out)

        skips = reversed(skips[:-1])

        stepsagain = int(np.log2(np.min(
            [self.scenes_shape[-2], self.scenes_shape[-1]]
        )))
        for _, skip in zip(range(steps-1), skips):
            _out = UpSample(
                feats,
                drop_rate=0.2, stride=2)(_out)
            _res = _out
            _out = UpSample(
                feats,
                stride=1)(_out)
            _out = torch.add(_res, _out)
            _out = torch.cat([_out, skip], axis=1)
            feats += skip.shape[1]

        passcounter = 1
        for _ in range(steps, stepsagain):
            if passcounter == 1:
                _out = UpSample(
                    feats, stride=4)(_out)
                _res = _out
                _out = UpSample(
                    feats, stride=1)(_out)
                _out = torch.add(_res, _out)
            passcounter = passcounter*-1

        if abs(stepsagain-steps) % 2 == 0:
            _out = UpSample(
                feats, stride=2)(_out)

        _out = torch.nn.Conv2d(
            feats, self.scenes_shape[0], 3, stride=1, padding=(1, 1), bias=True
        )(_out)
        _out = torch.nn.Sigmoid()(_out)

        return _out
