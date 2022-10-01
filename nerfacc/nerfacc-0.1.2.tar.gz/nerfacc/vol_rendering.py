from typing import Optional, Tuple

import torch
from torch import Tensor

import nerfacc.cuda as _C


def accumulate_along_rays(
    weights: Tensor,
    ray_indices: Tensor,
    values: Optional[Tensor] = None,
    n_rays: Optional[int] = None,
) -> Tensor:
    """Accumulate volumetric values along the ray.

    Note:
        This function is only differentiable to `weights` and `values`.

    Args:
        weights: Volumetric rendering weights for those samples. Tensor with shape \
            (n_samples,).
        ray_indices: Ray index of each sample. IntTensor with shape (n_samples). \
            It can be obtained from `unpack_to_ray_indices(packed_info)`.
        values: The values to be accmulated. Tensor with shape (n_samples, D). If \
            None, the accumulated values are just weights. Default is None.
        n_rays: Total number of rays. This will decide the shape of the ouputs. If \
            None, it will be inferred from `ray_indices.max() + 1`.  If specified \
            it should be at least larger than `ray_indices.max()`. Default is None.

    Returns:
        Accumulated values with shape (n_rays, D). If `values` is not given then we return \
            the accumulated weights, in which case D == 1.

    Examples:

    .. code-block:: python

        # Rendering: accumulate rgbs, opacities, and depths along the rays.
        colors = accumulate_along_rays(weights, ray_indices, values=rgbs, n_rays=n_rays)
        opacities = accumulate_along_rays(weights, ray_indices, values=None, n_rays=n_rays)
        depths = accumulate_along_rays(
            weights,
            ray_indices,
            values=(t_starts + t_ends) / 2.0,
            n_rays=n_rays,
        )
        # (n_rays, 3), (n_rays, 1), (n_rays, 1)
        print(colors.shape, opacities.shape, depths.shape)

    """
    assert ray_indices.dim() == 1 and weights.dim() == 1
    if not weights.is_cuda:
        raise NotImplementedError("Only support cuda inputs.")
    if values is not None:
        assert (
            values.dim() == 2 and values.shape[0] == weights.shape[0]
        ), "Invalid shapes: {} vs {}".format(values.shape, weights.shape)
        src = weights[:, None] * values
    else:
        src = weights[:, None]

    if ray_indices.numel() == 0:
        assert n_rays is not None
        return torch.zeros((n_rays, src.shape[-1]), device=weights.device)

    if n_rays is None:
        n_rays = int(ray_indices.max()) + 1
    else:
        assert n_rays > ray_indices.max()

    ray_indices = ray_indices.int()
    index = ray_indices[:, None].long().expand(-1, src.shape[-1])
    outputs = torch.zeros((n_rays, src.shape[-1]), device=weights.device)
    outputs.scatter_add_(0, index, src)
    return outputs


def render_weight_from_density(
    packed_info,
    t_starts,
    t_ends,
    sigmas,
    early_stop_eps: float = 1e-4,
) -> torch.Tensor:
    """Compute transmittance weights from density.

    Args:
        packed_info: Stores information on which samples belong to the same ray. \
            See :func:`nerfacc.ray_marching` for details. Tensor with shape (n_rays, 2).
        t_starts: Where the frustum-shape sample starts along a ray. Tensor with \
            shape (n_samples, 1).
        t_ends: Where the frustum-shape sample ends along a ray. Tensor with \
            shape (n_samples, 1).
        sigmas: The density values of the samples. Tensor with shape (n_samples, 1).
        early_stop_eps: The epsilon value for early stopping. Default is 1e-4.
    
    Returns:
        transmittance weights with shape (n_samples,).

    Examples:

    .. code-block:: python

        rays_o = torch.rand((128, 3), device="cuda:0")
        rays_d = torch.randn((128, 3), device="cuda:0")
        rays_d = rays_d / rays_d.norm(dim=-1, keepdim=True)

        # Ray marching with near far plane.
        packed_info, t_starts, t_ends = ray_marching(
            rays_o, rays_d, near_plane=0.1, far_plane=1.0, render_step_size=1e-3
        )
        # pesudo density
        sigmas = torch.rand((t_starts.shape[0], 1), device="cuda:0")
        # Rendering: compute weights and ray indices.
        weights = render_weight_from_density(
            packed_info, t_starts, t_ends, sigmas, early_stop_eps=1e-4
        )
        # torch.Size([115200, 1]) torch.Size([115200])
        print(sigmas.shape, weights.shape)

    """
    if not sigmas.is_cuda:
        raise NotImplementedError("Only support cuda inputs.")
    weights = _RenderingDensity.apply(
        packed_info, t_starts, t_ends, sigmas, early_stop_eps
    )
    return weights


def render_weight_from_alpha(
    packed_info,
    alphas,
    early_stop_eps: float = 1e-4,
) -> Tuple[torch.Tensor, ...]:
    """Compute transmittance weights from density.

    Args:
        packed_info: Stores information on which samples belong to the same ray. \
            See :func:`nerfacc.ray_marching` for details. Tensor with shape (n_rays, 2).
        alphas: The opacity values of the samples. Tensor with shape (n_samples, 1).
        early_stop_eps: The epsilon value for early stopping. Default is 1e-4.
    
    Returns:
        transmittance weights with shape (n_samples,).

    Examples:

    .. code-block:: python

        rays_o = torch.rand((128, 3), device="cuda:0")
        rays_d = torch.randn((128, 3), device="cuda:0")
        rays_d = rays_d / rays_d.norm(dim=-1, keepdim=True)

        # Ray marching with near far plane.
        packed_info, t_starts, t_ends = ray_marching(
            rays_o, rays_d, near_plane=0.1, far_plane=1.0, render_step_size=1e-3
        )
        # pesudo opacity
        alphas = torch.rand((t_starts.shape[0], 1), device="cuda:0")
        # Rendering: compute weights and ray indices.
        weights = render_weight_from_alpha(
            packed_info, alphas, early_stop_eps=1e-4
        )
        # torch.Size([115200, 1]) torch.Size([115200])
        print(alphas.shape, weights.shape)

    """
    if not alphas.is_cuda:
        raise NotImplementedError("Only support cuda inputs.")
    weights = _RenderingAlpha.apply(packed_info, alphas, early_stop_eps)
    return weights


@torch.no_grad()
def render_visibility(
    packed_info: torch.Tensor,
    alphas: torch.Tensor,
    early_stop_eps: float = 1e-4,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Filter out invisible samples given alpha (opacity).

    Args:
        packed_info: Stores information on which samples belong to the same ray. \
            See :func:`nerfacc.ray_marching` for details. Tensor with shape (n_rays, 2).
        alphas: The opacity values of the samples. Tensor with shape (n_samples, 1).
        early_stop_eps: The epsilon value for early stopping. Default is 1e-4.
    
    Returns:
        A tuple of tensors.

            - **visibility**: The visibility mask for samples. Boolen tensor of shape \
                (n_samples,).
            - **packed_info_visible**: The new packed_info for visible samples. \
                Tensor shape (n_rays, 2). It should be used if you use the visiblity \
                mask to filter out invisible samples.

    Examples:

    .. code-block:: python

        rays_o = torch.rand((128, 3), device="cuda:0")
        rays_d = torch.randn((128, 3), device="cuda:0")
        rays_d = rays_d / rays_d.norm(dim=-1, keepdim=True)

        # Ray marching with near far plane.
        packed_info, t_starts, t_ends = ray_marching(
            rays_o, rays_d, near_plane=0.1, far_plane=1.0, render_step_size=1e-3
        )
        # pesudo opacity
        alphas = torch.rand((t_starts.shape[0], 1), device="cuda:0")
        # Rendering but only for computing visibility of each samples.
        visibility, packed_info_visible = render_visibility(
            packed_info, alphas, early_stop_eps=1e-4
        )
        t_starts_visible = t_starts[visibility]
        t_ends_visible = t_ends[visibility]
        # torch.Size([115200, 1]) torch.Size([1283, 1])
        print(t_starts.shape, t_starts_visible.shape)

    """
    visibility, packed_info_visible = _C.rendering_alphas_forward(
        packed_info.contiguous(),
        alphas.contiguous(),
        early_stop_eps,
        True,  # compute visibility instead of weights
    )
    return visibility, packed_info_visible


class _RenderingDensity(torch.autograd.Function):
    """Rendering transmittance weights from density."""

    @staticmethod
    def forward(
        ctx,
        packed_info,
        t_starts,
        t_ends,
        sigmas,
        early_stop_eps: float = 1e-4,
    ):
        packed_info = packed_info.contiguous()
        t_starts = t_starts.contiguous()
        t_ends = t_ends.contiguous()
        sigmas = sigmas.contiguous()
        weights = _C.rendering_forward(
            packed_info,
            t_starts,
            t_ends,
            sigmas,
            early_stop_eps,
            False,  # not doing filtering
        )[0]
        if ctx.needs_input_grad[3]:  # sigmas
            ctx.save_for_backward(
                packed_info,
                t_starts,
                t_ends,
                sigmas,
                weights,
            )
            ctx.early_stop_eps = early_stop_eps
        return weights

    @staticmethod
    def backward(ctx, grad_weights):
        grad_weights = grad_weights.contiguous()
        early_stop_eps = ctx.early_stop_eps
        (
            packed_info,
            t_starts,
            t_ends,
            sigmas,
            weights,
        ) = ctx.saved_tensors
        grad_sigmas = _C.rendering_backward(
            weights,
            grad_weights,
            packed_info,
            t_starts,
            t_ends,
            sigmas,
            early_stop_eps,
        )
        return None, None, None, grad_sigmas, None


class _RenderingAlpha(torch.autograd.Function):
    """Rendering transmittance weights from alpha."""

    @staticmethod
    def forward(
        ctx,
        packed_info,
        alphas,
        early_stop_eps: float = 1e-4,
    ):
        packed_info = packed_info.contiguous()
        alphas = alphas.contiguous()
        weights = _C.rendering_alphas_forward(
            packed_info,
            alphas,
            early_stop_eps,
            False,  # not doing filtering
        )[0]
        if ctx.needs_input_grad[1]:  # alphas
            ctx.save_for_backward(
                packed_info,
                alphas,
                weights,
            )
            ctx.early_stop_eps = early_stop_eps
        return weights

    @staticmethod
    def backward(ctx, grad_weights):
        grad_weights = grad_weights.contiguous()
        early_stop_eps = ctx.early_stop_eps
        (
            packed_info,
            alphas,
            weights,
        ) = ctx.saved_tensors
        grad_sigmas = _C.rendering_alphas_backward(
            weights,
            grad_weights,
            packed_info,
            alphas,
            early_stop_eps,
        )
        return None, grad_sigmas, None
