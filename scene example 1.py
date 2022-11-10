# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def draw_pine_tree(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)"""

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 70
    skirt_right = peak_x + 70
    skirt_bottom = peak_y - 210
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 260

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")

def draw_fence(canvas):
        x_start = 0
        y_start = 50
        x_sep = 50
        for i in range(10):
                draw_rectangle(canvas, x_start, 0, y_start, 200, fill = "blue")
                draw_rectangle(canvas, x_sep, 0, y_start, 200, fill = "blue")
                y_start = 500


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_pine_tree(canvas, 500, 350)
    draw_pine_tree(canvas, 600, 280)
    draw_fence(canvas)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)
main()