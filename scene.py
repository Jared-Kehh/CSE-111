# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_snowman(canvas, scene_width, scene_height)
    draw_snowflakes(canvas, scene_width, scene_height)
    draw_trees(canvas, scene_width, scene_height)
    draw_cloud(canvas, 510, 320)
    draw_cloud(canvas, 550, 340)
    draw_cloud(canvas, 450, 340)
    draw_cloud(canvas, 420, 315)
    draw_cloud(canvas, 370, 345)
    draw_cloud(canvas, 800, 340)
    draw_cloud(canvas, 850, 320)
    draw_cloud(canvas, 900, 340)
    draw_cloud(canvas, 925, 325)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="white")

def draw_snowman(canvas, scene_width, scene_height):
    draw_oval(canvas, 50, 100, 150, 200, fill = "white")
    draw_oval(canvas, 50, 175, 150, 275, fill = "white")
    draw_oval(canvas, 50, 250, 150, 350, fill = "white")
    draw_line(canvas, 140, 240, 200, 250, fill = "tomato4")
    draw_line(canvas, 65, 240, 5, 250, fill = "tomato4")
    draw_oval(canvas, 90, 315, 80, 305, fill = "black")
    draw_oval(canvas, 120, 315, 110, 305, fill = "black")
    draw_oval(canvas, 105, 300, 95, 290, fill = "orange")
    draw_oval(canvas, 105, 190, 95, 200, fill = "black")
    draw_oval(canvas, 105, 220, 95, 210, fill = "black")
    draw_oval(canvas, 105, 240, 95, 230, fill = "black")

def draw_snowflakes(canvas, scene_width, scene_height):
    draw_oval(canvas, 150, 380, 160, 390, 
        fill = "white", outline = "white")
    draw_oval(canvas, 170, 350, 180, 360, 
        fill = "white", outline = "white")
    draw_oval(canvas, 200, 400, 210, 410, 
        fill = "white", outline = "white")
    draw_oval(canvas, 230, 320, 240, 330, 
        fill = "white", outline = "white")
    draw_oval(canvas, 270, 370, 280, 380, 
        fill = "white", outline = "white")
    draw_oval(canvas, 330, 380, 340, 390, 
        fill = "white", outline = "white")
    draw_oval(canvas, 370, 410, 380, 420, 
        fill = "white", outline = "white")
    draw_oval(canvas, 400, 350, 410, 360, 
        fill = "white", outline = "white")
    draw_oval(canvas, 420, 430, 430, 440, 
        fill = "white", outline = "white")
    draw_oval(canvas, 450, 290, 460, 300, 
        fill = "white", outline = "white")
    draw_oval(canvas, 470, 360, 480, 370, 
        fill = "white", outline = "white")
    draw_oval(canvas, 500, 450, 510, 460, 
        fill = "white", outline = "white")
    draw_oval(canvas, 520, 360, 530, 370, 
        fill = "white", outline = "white")
    draw_oval(canvas, 540, 330, 550, 340, 
        fill = "white", outline = "white")
    draw_oval(canvas, 570, 300, 580, 310, 
        fill = "white", outline = "white")
    draw_oval(canvas, 600, 385, 610, 395, 
        fill = "white", outline = "white")
    draw_oval(canvas, 650, 400, 660, 410, 
        fill = "white", outline = "white")
    draw_oval(canvas, 690, 390, 700, 400, 
        fill = "white", outline = "white")
    draw_oval(canvas, 730, 420, 740, 430, 
        fill = "white", outline = "white")

def draw_trees(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 300, 60, 320, 120, fill="brown")
    draw_polygon(canvas, 240, 110, 310, 350, 380, 110,
            fill="forestGreen")

    draw_rectangle(canvas, 660, 90, 680, 150, fill="brown")
    draw_polygon(canvas, 600, 140, 670, 400, 740, 140,
            fill="forestGreen")

def draw_cloud(canvas, peak_x, peak_y):

    cloud_one = peak_x - 200
    cloud_two = peak_y + 110
    cloud_three = peak_x - 160
    cloud_four = peak_y + 120
    cloud_five = peak_x - 270
    cloud_six = peak_y + 150
    draw_oval(canvas, cloud_one, cloud_two, cloud_three, 
        cloud_four, fill = "white", outline = "white")
    draw_oval(canvas, cloud_five, cloud_two, cloud_three, 
        cloud_six, fill = "white", outline = "white")


# Call the main function so that
# this program will start executing.
main()