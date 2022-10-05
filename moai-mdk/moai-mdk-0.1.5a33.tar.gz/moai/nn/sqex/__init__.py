import moai.nn.convolution as mic
import moai.nn.activation as mia
import moai.nn.linear as milin
import moai.nn.sampling.spatial.downsample as mids

from moai.networks.lightning.factory import HRNet, StackedHourglass

import torch
import omegaconf.omegaconf
import functools
import toolz
import typing

__all__ = ['SqueezeExcite']

#NOTE: from https://github.com/xvjiarui/GCNet/blob/029db5407dc27147eb1d41f62b09dfed8ec88837/mmdet/ops/gcb/context_block.py#L64
class Attention2d(torch.nn.Module):
    def __init__(self,
        features:       int,
    ):
        super(Attention2d, self).__init__()
        self.conv = torch.nn.Conv2d(features, 1, kernel_size=1)
        self.softmax = torch.nn.Softmax(dim=2)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        b, c, h, w = x.shape        
        y = x.view(b, c, h * w).unsqueeze(1)
        mask = self.conv(x)        
        mask = torch.nn.functional.softmax(
            mask.view(b, 1, h * w), dim=-1
        ).unsqueeze(-1)
        context = torch.matmul(y, mask)
        return context.view(b, c, 1, 1)

class GlobalAveragePool(torch.nn.Module):
    def __init__(self,   
        dims:       int,
        features:   int,        
    ):
        super(GlobalAveragePool, self).__init__()
        self.pool_func = functools.partial(
            getattr(torch.nn.functional, f"adaptive_avg_pool{dims}d"),
            output_size=1
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.pool_func(x)

__SQUEEZE__ = {
    'average1d':    functools.partial(GlobalAveragePool, dims=1),
    'average2d':    functools.partial(GlobalAveragePool, dims=2),
    'average3d':    functools.partial(GlobalAveragePool, dims=3),
    'attention2d':  Attention2d,
    'none':         torch.nn.Identity,
}

def make_channel_conv(
    type:               str,
    in_features:        int,
    out_features:       int,
    operation_params:   dict,
    activation_type:    str,
    activation_params:  dict,
):
    return mic.make_conv_block(
        block_type=type,
        convolution_type=type, 
        in_features=in_features, 
        out_features=out_features,
        activation_type=activation_type,
        convolution_params=toolz.merge(
            operation_params, 
            {'kernel_size': 1, 'padding': 0, 'stride': 1}
        ),
        activation_params=toolz.merge({'inplace': True}, activation_params)
    )

def make_channel_linear(
    type:               str,
    in_features:        int,
    out_features:       int,
    operation_params:   dict,
    activation_type:    str,
    activation_params:  dict,
):
    return milin.make_linear_block(
        block_type=type,
        linear_type=type, 
        in_features=in_features, 
        out_features=out_features,
        activation_type=activation_type,
        linear_params=operation_params,
        activation_params=toolz.merge({'inplace': True}, activation_params),
    )

__OPERATIONS__ = {
    'conv2d':   functools.partial(make_channel_conv, type='conv2d'),
    'linear':   functools.partial(make_channel_linear, type='linear'),
}

def make_channel(
    operation_type:     str,
    activation_type:    str,
    in_features:        int,    
    operation_params:   dict=None,    
    activation_params:  dict=None,
    ratio:              typing.Union[float, int]=0.5,
):
    inter_features = int(in_features * ratio)\
        if isinstance(ratio, float) else in_features // ratio
    return torch.nn.Sequential(
            __OPERATIONS__[operation_type](
                in_features=in_features,
                out_features=inter_features, 
                operation_params=operation_params or { },
                activation_type=activation_type or 'none',
                activation_params=activation_params or { }
            ),
            __OPERATIONS__[operation_type](
                in_features=inter_features,
                out_features=in_features,
                operation_params=operation_params or { },
                activation_type='none',
                activation_params={ }
            ),
            torch.nn.Unflatten(1, (in_features, 1, 1)) \
                if 'linear' in operation_type else torch.nn.Identity()
        )

def make_spatial(
    operation_type:     str,
    activation_type:    str,
    in_features:        int,    
    operation_params:   dict=None,
    activation_params:  dict=None,
    ratio:              float=1.0,
):
    return make_channel_conv(
        type=operation_type,
        in_features=in_features,
        out_features=1,
        operation_params=operation_params or { },
        activation_type=activation_type,
        activation_params=activation_params or { },        
    )

__EXCITE__ = {
    'channel': make_channel,
    'spatial': make_spatial,
    #TODO: 'channel_spatial': #NOTE: with max of channel and spatial, see https://github.com/ai-med/squeeze_and_excitation/blob/acdd26e7e3956b8e3d3b32663a784ebd64c844dd/squeeze_and_excitation/squeeze_and_excitation_3D.py#L119
}

#NOTE: it is an activation
#TODO: check with bias as well: https://github.com/JYPark09/SENet-PyTorch/blob/6f1eae93256e5181baea8d5102473c6cba6500fa/network.py#L6
class SqueezeExcite(torch.nn.Module):
    def __init__(self,
        features:       int,
        squeeze:        omegaconf.DictConfig, # type: 'averageXd', # one of ['averageXd', 'attentionXd']
        excite:         omegaconf.DictConfig, # delta: activation_{type|params}, # ratio \in [0, 1], # operation_{type|params}: one of ['convXd', 'linear']
        mode:           str='mul',
    ):
        super(SqueezeExcite, self).__init__()
        self.squeeze = __SQUEEZE__[squeeze.type](features=features)
        self.excite = __EXCITE__[excite.type](
            operation_type=excite.operation.type,
            activation_type=toolz.get_in(['activation', 'type'], excite, 'none'),
            in_features=features,
            operation_params=excite.operation.params or { },
            activation_params=toolz.get_in(['activation', 'params'], excite, { }),
            ratio=excite.ratio,
        )
        self.mode = getattr(torch, mode)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        squeezed = self.squeeze(x)
        excited = self.excite(squeezed)
        return self.mode(torch.sigmoid(excited), x)

if __name__ == '__main__':
    FEATURES = 32
    t = torch.rand(5, FEATURES, 24, 32)
    se = SqueezeExcite(
        features=FEATURES,
        # ''' TRADITIONAL Squeeze-n-Excite '''
        squeeze=omegaconf.DictConfig({
            'type': 'average2d',
            # 'type': 'attention2d',
        }),        
        excite=omegaconf.DictConfig({
            'type': 'channel',
            'operation': {
                # 'type': 'linear',
                'type': 'conv2d',
            },
            'activation': {
                'type': 'bn2d_relu',
                # 'type': 'relu_bn2d',
                # 'type': 'relu',
            },
            'ratio': 16, # 0.25,
        }),
        # ''' Spatial Squeeze-n-Excite '''
        # squeeze=omegaconf.DictConfig({
        #     'type': 'none',
        # }),        
        # excite=omegaconf.DictConfig({
        #     'type': 'spatial',
        #     'operation': {
        #         'type': 'conv2d',
        #         'params': {
        #             'bias': False,
        #         }
        #     },
        # }),
        # mode='mul',        
    )
    res = se(t)
    print(res.shape)