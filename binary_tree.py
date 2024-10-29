
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
    ax.plot([x, x_end], [y, y_end], 'brown', lw = 2)

    # Calculate new length and depth
    new_length = starting_length * length_modifier

    # Calculate left and right angles    
    angle_left = starting_angle + angle_change
    angle_right = starting_angle - angle_change
    
    # Draw branches recursively
    draw_branch(ax, x_end, y_end, depth - 1, angle_left, new_length, angle_change, length_modifier)
    draw_branch(ax, x_end, y_end, depth - 1, angle_right, new_length, angle_change, length_modifier)

def draw_tree(depth, angle, length, angle_change, length_modifier):
    fig, ax = plt.subplots(figsize = (8, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw tree with n levels
    draw_branch(ax, 0, 0, depth, angle, length, angle_change, length_modifier)
    
    return fig

# Parameters:
# path              - path for folder where to save files,
# gif_name          - generated gif name,
# generate_gif      - specifies whether a gif of tree cosntruction should be generated,
# keep_files        - specifies whether to keep temporary files used for generating,
# depth             - depth of a binary tree,
# starting_angle    - starting angle of a binary tree,
# starting_length   - starting length of a binary tree,
# angle_change      - change in branch angle with each iteration,
# length_modifier   - modifier in branch length in each iteration,
def create_tree_gif(path = './', gif_name = 'tree_animation.gif', generate_gif = True, keep_files = True, depth = 13, starting_angle = np.pi / 2, starting_length = 0.6, angle_change = np.pi / 6, length_modifier = 0.6):
    if not generate_gif and not keep_files:
        fig = draw_tree(depth, starting_angle, starting_length, angle_change, length_modifier)
        return
    
    filename = f'{path}{gif_name}'
    filenames = []
    for i in range(1, depth + 1):
        fig = draw_tree(i, starting_angle, starting_length, angle_change, length_modifier)
        img_filename = f"{path}tree_{i}.png"
        fig.savefig(img_filename)
        if i != depth:
            plt.close(fig)
        filenames.append(img_filename)

    if generate_gif:
        with imageio.get_writer(filename, mode = 'I') as writer:
                image = imageio.imread(img_filename)
                writer.append_data(image)

    if not keep_files:
        for img_filename in filenames:
            os.remove(img_filename)


create_tree_gif('./gifs/', generate_gif = False, keep_files = False)
plt.show()