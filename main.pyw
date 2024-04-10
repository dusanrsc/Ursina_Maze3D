# importing modules and sub-modules
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# special variables
# meta data
__name__ = "Maze3D"
__version__ = "v1.0"

# game lists
# level_blank = [
# [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
# [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

level1 = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
[1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1],
[1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
[1,0,0,0,0,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1],
[1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1],
[1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1,1,1],
[1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1],
[1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
[1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
[1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1],
[1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
[1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1],
[1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,1],
[1,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1],
[1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1],
[1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1],
[1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,2,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

# color constants
RED = color.red
GREEN = color.green
BLUE = color.blue

BLACK = color.black
WHITE = color.white

ALPHA = GREEN

# creating main app window
app = Ursina()

# window settings
window.exit_button.enabled = False
window.fps_counter.enabled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.fullscreen = False

# game functions
# input function
def input(key):
	# fullscreen or window
	if key == "f" and window.fullscreen == False:
		window.fullscreen = True
	elif key == "f" and window.fullscreen == True:
		window.fullscreen = False

# update function
def update():
	if held_keys["escape"]:
		pass

# drawing chessboard from chessboard list
for row_index, row in enumerate(level1, start=1):
	for col_index, tile in enumerate(row, start=1):
		if tile == 1:
			wall = Entity(parent=scene, model="cube", texture="grass", color=color.rgb(255, 255, 255, 255), position=(col_index, 0, row_index), scale=(1, 3.5, 1), collider="box")
		if tile == 2:
			exit = Button(parent=scene, model="sphere", color=color.rgb(255, 0, 0, 200), position=(col_index, -1, row_index), scale=(0.5, 0.5, 0.5), collider="mesh")
			exit.on_click = lambda: print("Level Finished!")
		else:
			pass

# sky
sky = Sky(texture="sky_sunset")

# player
player = FirstPersonController(position=(2, -2, 2))

# ground
ground = Entity(parent=scene, model="cube", color=color.rgb(255, 255, 255, 50), position=(10.5, -2, 10.5), scale=(19.5, 0.1, 19.5), collider="mesh")

# running the app
app.run()