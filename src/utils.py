import matplotlib.pyplot as plt

def save_image(fig, filename, format = 'png'):
    path = f'docs/images/{filename}.png'

    if 'plotly.graph_objs._figure.Figure' in str(type(fig)):
        fig.write_image(path)
    else:
        fig.savefig(path, bbox_inches = 'tight')
    print(f'Successfully saved: {path}')