import torch


class Conv2dMock:
    def __init__(self, obj):
        self.__class__ = type(
            obj.__class__.__name__, (self.__class__, obj.__class__), {}
        )
        self.__dict__ = obj.__dict__
        self.in_channels = obj.in_channels
        self.out_channels = obj.out_channels
        self.kernel_size = obj.kernel_size
        self.stride = obj.stride
        self.padding = obj.padding
        self.dilation = obj.dilation
        self.mock_gradient_sink = torch.ones(1, requires_grad=True)

    def forward(self, x):
        batch_size, in_channels, in_height, in_width = x.shape
        assert self.in_channels == in_channels
        # assert self.device == x.device
        out_height = (
            in_height
            + 2 * self.padding[0]
            - self.dilation[0] * (self.kernel_size[0] - 1)
            - 1
            + self.stride[0]
        ) // self.stride[0]
        out_width = (
            in_width
            + 2 * self.padding[1]
            - self.dilation[1] * (self.kernel_size[1] - 1)
            - 1
            + self.stride[1]
        ) // self.stride[1]

        return self.mock_gradient_sink * torch.zeros(
            (batch_size, self.out_channels, out_height, out_width)
        )

class MockConvFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, weight, bias=None):
        ctx.save_for_backward(x, weight, bias)
        out_features, in_features = weight.shape
        assert x.shape[-1] == in_features
        output_shape = (*x.shape[:-1], out_features)
        output = torch.zeros(output_shape, requires_grad=True)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        x, weight, bias = ctx.saved_tensors
        grad_input = grad_weight = grad_bias = None

        if ctx.needs_input_grad[0]:
            grad_input = torch.zeros(x.shape, requires_grad=True)
        if ctx.needs_input_grad[1]:
            grad_weight = torch.zeros(weight.shape, requires_grad=True)
        if bias is not None and ctx.needs_input_grad[2]:
            grad_bias = torch.zeros(bias.shape, requires_grad=True)
        return grad_input, grad_weight, grad_bias


class MockConvModule:
    def __init__(self, obj):
        super().__init__()
        self.__class__ = type(
            obj.__class__.__name__, (self.__class__, obj.__class__), {}
        )
        self.__dict__ = obj.__dict__
        self.weight = obj.weight
        self.bias = obj.bias
        self.in_channels = obj.in_channels
        self.out_channels = obj.out_channels
        self.kernel_size = obj.kernel_size
        self.stride = obj.stride
        self.padding = obj.padding
        self.dilation = obj.dilation
 

    def forward(self, x):
        return MockConvFunction.apply(x, self.weight, self.bias)



mock_dict = {
    # torch.nn.modules.conv.Conv1d,
    torch.nn.modules.conv.Conv2d: Conv2dMock,
    # torch.nn.modules.conv.Conv3d,
    # torch.nn.modules.conv.ConvTranspose1d,
    # torch.nn.modules.conv.ConvTranspose2d,
    # torch.nn.modules.conv.ConvTranspose3d,
    # torch.nn.modules.conv.LazyConv1d,
    # torch.nn.modules.conv.LazyConv2d,
    # torch.nn.modules.conv.LazyConv3d,
    # torch.nn.modules.conv.LazyConvTranspose1d,
    # torch.nn.modules.conv.LazyConvTranspose2d,
    # torch.nn.modules.conv.LazyConvTranspose3d,
}
