import matplotlib.pyplot as plt


def plot_imagem(imagem):
    plt.figure(figsize=(12, 4))
    plt.imshow(imagem, cmap='gray')
    plt.axis('off')
    plt.show()


def plot_resultado(*args):
    numero_imagem = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=numero_imagem, figsize=(12, 4))
    nomes_lst = ['Imagem {}'.format(i) for i in range(1, numero_imagem)]
    nomes_lst.append("Resultado")
    for ax, nome, imagem in zip(axis, nomes_lst, args):
        ax.set_title(nome)
        ax.imshow(imagem, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()


def plot_histograma(imagem):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(
        12, 4), sharex=True, sharey=True)
    cor_lst = ['red', 'green', 'blue']
    for index, (ax, cor) in enumerate(zip(axis, cor_lst)):
        ax.set_title('{} histogram'.format(cor.title()))
        ax.hist(imagem[:, :, index].ravel(), bins=256, cor=cor, alpha=0.8)
    fig.tight_layout()
    plt.show()
