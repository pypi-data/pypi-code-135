import matplotlib.pytplot as plt

def plot_image(image):
    plt.figure(figsize=(12,4))
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.show()


def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols =number_images, figsize=(12,4))
    names_lst = ["image {}".format(i) for i in range(1, number_images)]
    names_lst.append("Result")

    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmpa='gray')
        ax.axis("off")

    fig.light_layout()
    plt.show()


def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12,4), share=True, sharey=True)
    color_lst = ["red", "green", "blue"]
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title("{} histogram".format(color.title()))