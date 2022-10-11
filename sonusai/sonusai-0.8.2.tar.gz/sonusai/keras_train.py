"""sonusai keras_train

usage: keras_train [-hv] (-m MODEL) (-d MIXDB) [--tloc TLOC] [-l VMIXDB] [--vloc VLOC]
                    [-e EPOCHS] [-b BATCH] [-t TSTEPS] [-p ESP] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -m MODEL, --model MODEL         Model Python file with build and/or hypermodel functions.
    -d MIXDB, --mixdb MIXDB         Mixture database JSON file.
    --tloc TLOC                     Data location.
    -l VMIXDB, --vmixdb VMIXDB      Validation split (0 - 1) or validation mixdb. [default: 0.2].
    --vloc VLOC                     Validation data location.
    -e EPOCHS --epochs EPOCHS       Number of epochs to use in training. [default: 8].
    -b BATCH, --batch BATCH         Batch size. [default: 32].
    -t TSTEPS, --tsteps TSTEPS      Timesteps. [default: 0].
    -p ESP, --patience ESP          Early stopping patience.
    -o OUTPUT, --output OUTPUT      Output directory.

Use Keras to train a model defined by a Python definition file and SonusAI genft data.

Inputs:
    MIXDB   A SonusAI mixture database JSON file
    TLOC    Optional

Validation is created from FEATURE using a split of VAL.

Results are written into subdirectory <MODEL>-<TIMESTAMP>

"""
from sonusai import logger


def main():
    from docopt import docopt

    import sonusai
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    model_name = args['--model']
    mixdb_name = args['--mixdb']
    genft_location = args['--genft']
    epochs = int(args['--epochs'])
    batch_size = int(args['--batch'])
    timesteps = int(args['--tsteps'])
    es_p = args['--patience']
    v_split = args['--vmixdb']
    output_dir = args['--output']

    # TODO: handle vmixdb: float or mixdb.json files
    if v_split < 0 or v_split > 1:
        logger.exception('--val must be between 0 and 1')
        raise SystemExit(1)

    from os import makedirs
    from os import walk
    from os.path import basename
    from os.path import join
    from os.path import splitext

    import h5py
    import keras2onnx
    import keras_tuner as kt
    import numpy as np
    import tensorflow as tf
    from tensorflow.keras import backend as kb
    from tensorflow.keras.callbacks import EarlyStopping

    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.data_generator import KerasFromH5
    from sonusai.mixture import get_class_count_from_mixids
    from sonusai.mixture import load_mixdb
    from sonusai.mixture import new_mixdb_from_mixids
    from sonusai.utils import create_onnx_from_keras
    from sonusai.utils import import_keras_model
    from sonusai.utils import create_ts_name
    from sonusai.utils import stratified_shuffle_split_mixid

    if genft_location is None:
        genft_location = splitext(mixdb_name)[0]

    model_tail = basename(model_name)
    model_root = splitext(model_tail)[0]

    if output_dir is None:
        output_dir = create_ts_name(model_root)

    makedirs(output_dir, exist_ok=True)
    base_name = join(output_dir, model_root)

    # Setup logging file
    create_file_handler(join(output_dir, 'keras_train.log'))
    update_console_handler(verbose)
    initial_log_messages('keras_train')

    # Check dims and model build before we read large dataset and make subdir and start logging
    logger.info(f'TF ver: {tf.__version__}')
    logger.info(f'Keras ver: {tf.keras.__version__}')
    logger.info(f'Keras2onnx ver: {keras2onnx.__version__}')

    mixdb = load_mixdb(mixdb_name)
    num_mixtures = len(mixdb.mixtures)
    logger.info(f'Found {num_mixtures} mixtures with {mixdb.num_classes} classes from {mixdb_name}')

    # Import model definition file
    model = import_keras_model(model_name)
    logger.info(f'Successfully imported {model_tail}, testing default model build')

    logger.info('Building default model')
    try:
        hypermodel = model.MyHyperModel()
    except Exception as e:
        logger.exception(f'Error: build_model() in {model_tail} failed: {e}.')
        raise SystemExit(1)

    if hypermodel.feature != mixdb.feature:
        logger.warning(f'Overriding feature: default = {hypermodel.feature}; specified = {mixdb.feature}.')

    if hypermodel.num_classes != mixdb.num_classes:
        logger.warning(f'Overriding num_classes: default = {hypermodel.num_classes}; specified = {mixdb.num_classes}.')

    if hypermodel.timesteps != timesteps:
        logger.info(f'Overriding timesteps: default = {hypermodel.timesteps}; specified = {timesteps}.')

    if hypermodel.batch_size != batch_size:
        logger.info(f'Overriding batch_size: default = {hypermodel.batch_size}; specified = {batch_size}.')

    logger.info('Building specified model')
    try:
        hypermodel = model.MyHyperModel(feature=mixdb.feature,
                                        num_classes=mixdb.num_classes,
                                        timesteps=timesteps,
                                        batch_size=batch_size)
        built_model = hypermodel.build_model(kt.HyperParameters())
    except Exception as e:
        logger.exception(f'Error: build_model() in {model_tail} failed: {e}.')
        raise SystemExit(1)

    logger.info(f'Successfully built using {model_tail}, summary:')
    kb.clear_session()
    logger.info('')
    built_model.summary(print_fn=logger.info)
    logger.info(f'User shape parameters: batch_size {batch_size}, timesteps {timesteps}, '
                f'flatten={hypermodel.flatten}, add1ch={hypermodel.add1ch}')
    logger.info(f'Model build above with default hyper-parameters, in_shape: {hypermodel.input_shape}, '
                f'num_classes {mixdb.num_classes}')
    logger.info(f'Compiled with optimizer: {built_model.optimizer.get_config()}')
    logger.info('')

    # v_split from --val arg or default = 0.2
    logger.info(f'Calculating validation data using split of {v_split}')
    use_strat = False
    if use_strat:
        t_mixid, v_mixid, t_num_mixid, v_num_mixid = stratified_shuffle_split_mixid(mixdb, vsplit=v_split)
        logger.info(f'Split {len(v_mixid)} validation mixtures')
    else:
        mxsplit = int(np.ceil((1 - v_split) * num_mixtures))
        t_mixid = list(range(mxsplit))
        v_mixid = list(range(mxsplit, num_mixtures))
        logger.info(f'Split {len(v_mixid)} validation mixtures without stratification.')

    v_datagen = KerasFromH5(mixdb=mixdb,
                            mixids=v_mixid,
                            location=genft_location,
                            batch_size=batch_size,
                            timesteps=timesteps,
                            flatten=hypermodel.flatten,
                            add1ch=hypermodel.add1ch,
                            shuffle=False)

    # Prepare class weighting
    class_featcnt = np.ceil(np.array(get_class_count_from_mixids(mixdb, t_mixid)) / mixdb.feature_step_samples)
    if mixdb.truth_mutex:
        oweight = 16.0
        logger.info(f'Detected single-label mode (truth_mutex), setting other weight to {oweight}')
        class_featcnt[-1] = class_featcnt[-1] / oweight

    # Use SonusAI DataGenerator to create training+truth on the fly
    logger.info(f'Split {len(t_mixid)} training mixtures')
    t_datagen = KerasFromH5(mixdb=mixdb,
                            mixids=t_mixid,
                            location=genft_location,
                            batch_size=batch_size,
                            timesteps=timesteps,
                            flatten=hypermodel.flatten,
                            add1ch=hypermodel.add1ch,
                            shuffle=True)

    # TODO: If hypermodel.es exists, then use it; otherwise use default here
    if es_p is None:
        es = EarlyStopping(monitor='val_loss',
                           mode='min',
                           verbose=1,
                           patience=8)
    else:
        es = EarlyStopping(monitor='val_loss',
                           mode='min',
                           verbose=1,
                           patience=es_p)

    ckpt_callback = tf.keras.callbacks.ModelCheckpoint(filepath=base_name + '-ckpt-weights.h5',
                                                       save_weights_only=True,
                                                       monitor='val_loss',
                                                       mode='min',
                                                       save_best_only=True)

    logger.info('')
    logger.info(f'Training with no class weighting and early stopping patience = {es.patience}')
    logger.info('')

    history = built_model.fit(t_datagen,
                              batch_size=batch_size,
                              epochs=epochs,
                              validation_data=v_datagen,
                              shuffle=False,
                              callbacks=[es, ckpt_callback])

    # Save history into numpy file
    history_name = base_name + '-history'
    np.save(history_name, history.history)
    # Note: Reload with history=np.load(history_name, allow_pickle='TRUE').item()
    logger.info(f'Saved training history to numpy file {history_name}.npy')

    # Find checkpoint file and load weights for prediction and model save
    checkpoint_name = None
    for path, dirs, files in walk(output_dir):
        for f in files:
            if "ckpt" in f:
                checkpoint_name = f

    if checkpoint_name is not None:
        logger.info('Using best checkpoint for prediction and model exports')
        built_model.load_weights(join(output_dir, checkpoint_name))
    else:
        logger.info('Using last epoch for prediction and model exports')

    # save for later model export(s)
    weight_name = base_name + '.h5'
    built_model.save(weight_name)

    logger.info(f'Saved trained model to {weight_name}')
    # Save to ONNX format with specified batch and timestep sizes
    onnx_name = base_name + '.onnx'
    try:
        create_onnx_from_keras(keras_model=built_model,
                               is_flattened=hypermodel.flatten,
                               has_timestep=(timesteps != 0),
                               has_channel=hypermodel.add1ch,
                               is_mutex=mixdb.truth_mutex,
                               feature=mixdb.feature,
                               filename=onnx_name)
    except Exception as e:
        logger.warning(f'Failed to create ONNX model, no file saved: {e}.')
    logger.info(f'Wrote model to onnx file {onnx_name}')

    # Compute prediction metrics on validation data using saved best checkpoint
    # t_mixid, v_mixid, or entire dataset mixdb
    v_mixdb = new_mixdb_from_mixids(mixdb, v_mixid)
    v_predict = built_model.predict(x=v_datagen, batch_size=batch_size, verbose=1)
    v_predict_name = base_name + '-valpredict.h5'
    with h5py.File(v_predict_name, 'w') as f:
        f.create_dataset('predict', data=v_predict)
        f.attrs['mixdb'] = v_mixdb.to_json()

    logger.info(f'Wrote prediction and truth to file {v_predict_name}')
    # Create and save onnx model with timesteps, batch = 1
    if timesteps > 0:
        # only set to 1 if nonzero (exists)
        timesteps = 1
    hypermodelp = model.MyHyperModel(feature=mixdb.feature,
                                     num_classes=mixdb.num_classes,
                                     timesteps=timesteps,
                                     batch_size=1)

    built_modelp = hypermodelp.build_model(kt.HyperParameters())
    # load weights from previously saved HDF5
    built_modelp.load_weights(weight_name)
    # save a prediction version of model to base_name-pred-onnx
    b1_onnx_name = base_name + '-b1.onnx'
    create_onnx_from_keras(keras_model=built_modelp,
                           is_flattened=hypermodel.flatten,
                           has_timestep=(timesteps != 0),
                           has_channel=hypermodel.add1ch,
                           is_mutex=mixdb.truth_mutex,
                           feature=mixdb.feature,
                           filename=b1_onnx_name)
    logger.info(f'Wrote inference model (batch_size=1) to onnx file {b1_onnx_name}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        exit()
