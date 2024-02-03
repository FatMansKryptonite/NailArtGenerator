import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def read_png_to_np_array(path: str) -> np.array:
    image = Image.open(path).convert('L')
    return np.array(image)


def calculate_dot_coordinates(image_array: np.array, num_dots: int) -> np.array:
    dot_coordinate_array = np.random.rand(num_dots, 2)



    return dot_coordinate_array


def plot_dots(dot_coordinate_array: np.array, canvas_ratio: float = 1.0) -> None:
    x = dot_coordinate_array[:, 0]
    y = dot_coordinate_array[:, 1]
    plt.scatter(x, y, marker='.', s=1, color='k')
    ax = plt.gca()
    ax.set_aspect(canvas_ratio, adjustable='box')

    plt.pause(100)


if __name__ == '__main__':
    array = read_png_to_np_array(r"C:\Users\IvarCashinEriksson\Pictures\Screenshot 2023-03-31 134024.png")
    dot_coordinate_array = calculate_dot_coordinates(array, num_dots=1000)
    plot_dots(dot_coordinate_array, canvas_ratio=2.0)

