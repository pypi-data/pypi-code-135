# model settings
model = dict(
    type='SwAV',
    backbone=dict(
        type='ResNet',
        depth=50,
        in_channels=3,
        out_indices=[4],  # 0: conv-1, x: stage-x
        norm_cfg=dict(type='SyncBN'),
        zero_init_residual=True),
    neck=dict(
        type='SwAVNeck',
        in_channels=2048,
        hid_channels=2048,
        out_channels=128,
        with_avg_pool=True),
    head=dict(
        type='SwAVHead',
        feat_dim=128,  # equal to neck['out_channels']
        epsilon=0.05,
        temperature=0.1,
        num_crops=[2, 6],
    ))
