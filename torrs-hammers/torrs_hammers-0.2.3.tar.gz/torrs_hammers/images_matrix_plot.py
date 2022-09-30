from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
from skimage import io


def images_matrix_plot(pDir, images_names,
                       output_name='images_matrix',
                       x_title='X Title', y_title='Y title',
                       height=3000, width=3000,
                       show=False,
                       save_png=True,
                       save_html=True):
    m = int(np.ceil(np.sqrt(len(images_names))))

    fig = make_subplots(m, m, horizontal_spacing=.01, vertical_spacing=.01,
                        x_title=x_title, y_title=y_title)

    for i, img in enumerate(images_names):
        curr_img = io.imread(pDir + img)
        r, c = i // m + 1, i % m + 1
        fig.add_trace(go.Image(z=curr_img), row=r, col=c)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

    fig.update_layout(height=height, width=width, template='presentation')
    if save_png:
        fig.write_image(f'{output_name}.png')
    if save_html:
        fig.write_image(f'{output_name}.html')
    if show:
        fig.show()