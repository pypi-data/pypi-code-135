import matplotlib.pyplot as plt


def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


def plot_results(*args):
    number_image = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_image, figsize=(12, 4))
    name_lst = ['image {}'.format(i) for i in range(1, number_image)]
    name_lst.append('Result')
    for ax, title_name, image in zip(axis, name_lst, args):
        ax.set_title(title_name)
        ax.inshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()


def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    cor_lst = ['red', 'green', 'blue']
    for index, (ax, cor) in enumerate(zip(axis, cor_lst)):
        ax.set_title('{} histogram'.format(cor.title()))
        ax.hist(image[:, :, index].ravel(), bins=256, cor=cor, alpha=0.8)
    fig.tight_layout()
    plt.show()