import numpy as np
import os
import matplotlib.pyplot as plt
def generate_real_samples(dataset,n_samples,patch_shape):
    ix = np.random.randint(0,dataset.shape[0],n_samples)
    x = dataset[ix]
    y = np.ones((n_samples,patch_shape,patch_shape,1))
    return x ,y

def generate_fake_samples(g_model,dataset,patch_shape):
    x = g_model.predict(dataset)
    y = np.zeros((len(x), patch_shape, patch_shape, 1))
    return x,y

def save_models(step, g_model_AtoB, g_model_BtoA):
    # save the first generator model
    filename1 = f'g_model_AtoB_{step+1}.h5'
    g_model_AtoB.save(os.path.join('models','atob',filename1))
    # save the second generator model
    filename2 = f'g_model_BtoA_{step+1}.h5'
    g_model_BtoA.save(os.path.join('models','btoa',filename2))
    print(f'>Saved: {filename1} and {filename2}')

def summarize_performance(step, g_model, trainX, name, n_samples=5):
    # select a sample of input images
    X_in, _ = generate_real_samples(trainX, n_samples, 0)
    # generate translated images
    X_out, _ = generate_fake_samples(g_model, X_in, 0)
    # scale all pixels from [-1,1] to [0,1]
    X_in = (X_in + 1) / 2.0
    X_out = (X_out + 1) / 2.0
    # plot real images
    for i in range(n_samples):
        plt.subplot(2, n_samples, 1 + i)
        plt.axis('off')
        plt.imshow(X_in[i])
    # plot translated image
    for i in range(n_samples):
        plt.subplot(2, n_samples, 1 + n_samples + i)
        plt.axis('off')
        plt.imshow(X_out[i])
    # save plot to file
    filename1 = f'{name}_generated_plot_{step+1}.png'
    plt.savefig(os.path.join('eval_plots',filename1))
    plt.close()

def update_image_pool(pool, images, max_size=50):
    selected = list()
    for image in images:
        if len(pool) < max_size:
            # stock the pool
            pool.append(image)
            selected.append(image)
        elif np.random.random() < 0.5:
            # use image, but don't add it to the pool
            selected.append(image)
        else:
            # replace an existing image and use replaced image
            ix = np.random.randint(0, len(pool))
            selected.append(pool[ix])
            pool[ix] = image
    return np.asarray(selected)
