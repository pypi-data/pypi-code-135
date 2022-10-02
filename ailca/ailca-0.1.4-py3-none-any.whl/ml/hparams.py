from itertools import product
from ailca.ml.util import *
from ailca.data.base import Dataset
from ailca.data.util import get_data_loader


def optimize_hparams(model: Model,
                     dataset: Dataset,
                     hparams: dict):
    dataset_train, dataset_val = dataset.split(ratio_train=0.8)
    keys, vals = zip(*hparams.items())
    combs = [dict(zip(keys, p)) for p in product(*vals)]
    init_state_dict = deepcopy(model.state_dict()) if isinstance(model, PyTorchModel) else None
    best_hparams = None
    best_score = -1e+8

    for c in combs:
        score = None

        if isinstance(model, SKLearnModel):
            _model = SKLearnModel(alg=model.alg_id, **c)
            _model.fit(dataset_train)
            score = r2_score(dataset_val.y, _model.predict(dataset_val))
        elif isinstance(model, PyTorchModel):
            batch_size = c['batch_size'] if 'batch_size' in c.keys() else 64
            grad_name = c['gradient_method'] if 'gradient_method' in c.keys() else 'adam'
            init_lr = c['init_lr'] if 'init_lr' in c.keys() else 1e-3
            l2_reg = c['l2_reg'] if 'l2_reg' in c.keys() else 1e-6
            loss_name = c['loss_func'] if 'loss_func' in c.keys() else 'mae'

            model.load_state_dict(deepcopy(init_state_dict))
            loader_train = get_data_loader(dataset_train, batch_size=batch_size, shuffle=True)
            optimizer = get_optimizer(model, gradient_method=grad_name, init_lr=init_lr, l2_reg=l2_reg)
            loss_func = get_loss_func(loss_func=loss_name)

            for n in range(0, 100):
                _ = model.fit(loader_train, optimizer, loss_func)
            score = r2_score(dataset_val.y, model.predict(dataset_val))

        if score > best_score:
            best_hparams = c
            best_score = score

    return best_hparams, best_score
