import matplotlib.pyplot as plt
import numpy as np
import imageio.v3
import os

def draw_branch(ax, x, y, depth, starting_angle, starting_length, angle_change, length_modifier):
    if depth == 0:
        return
    
    # Calculate branch endpoints
    x_end = x + starting_length * np.cos(starting_angle)
    y_end = y + starting_length * np.sin(starting_angle)
    
    # Draw branch
    ax.plot([x, x_end], [y, y_end], 'brown', lw=2)

    # Calculate new length and depth    
    new_length = starting_length * length_modifier
    new_depth = depth - 1

    # Calculate left and right angles    
    angle_left = starting_angle + angle_change
    angle_right = starting_angle - angle_change
    
    # Draw branches recursively
    draw_branch(ax, x_end, y_end, new_depth, angle_left, new_length, angle_change, length_modifier)
    draw_branch(ax, x_end, y_end, new_depth, angle_right, new_length, angle_change, length_modifier)

def draw_tree(depth, angle, length, angle_change, length_modifier):
    fig, ax = plt.subplots(figsize = (8, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Starting point
    x, y = 0, 0
    
    # Draw tree with n levels
    draw_branch(ax, x, y, depth, angle, length, angle_change, length_modifier)
    
    return fig

# Parameters:
# path              - path for folder where to save files,
# gif_name          - generated gif name,
# delete_files      - specifies whether to delete intermediate files used for generating,
# iterations        - number of iterations used to generate fractal,
# starting_angle    - starting angle of a binary tree,
# starting_length   - starting length of a binary tree,
# angle_change      - change in branch angle with each iteration,
# length_modifier   - modifier in branch length in each iteration,
def create_tree_gif(path = './', gif_name = 'tree_animation.gif', delete_files = True, iterations = 6, starting_angle = np.pi / 2, starting_length = 1, angle_change = np.pi / 6, length_modifier = 0.7):
    filename = f'{path}{gif_name}';
    filenames = []
    for i in range(iterations + 1):
        fig = draw_tree(i, starting_angle, starting_length, angle_change, length_modifier)
        img_filename = f"{path}tree_{i}.png"
        fig.savefig(img_filename)
        plt.close(fig)
        filenames.append(img_filename)
    
    with imageio.get_writer(filename, mode = 'I') as writer:
        for img_filename in filenames:
            image = imageio.imread(img_filename)
            writer.append_data(image)
            if delete_files:
                os.remove(img_filename)

create_tree_gif('./gifs/')
