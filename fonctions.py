import pyMeow as pm
import time

class fct():
    
    def initialisation():
        pm.overlay_init()
        pm.set_fps(60)
        pm.toggle_mouse()
        # pm.gui_fade(0.9)
        color_black = pm.get_color("black")
        color_white = pm.get_color("white")
        color_red = pm.get_color("red")
        color_green = pm.get_color("green")
        color_blue = pm.get_color("blue")
        map_full = pm.load_texture("map_full.png")
        width, height = pm.get_screen_width(), pm.get_screen_height()
        show_menu = False

        return map_full, width, height, show_menu, color_black, color_white, color_red, color_green, color_blue


    def menu_status(show_menu):
        if pm.key_pressed(0x60) :
            if show_menu == False :
                show_menu = True
            else :
                show_menu = False
            print(show_menu)
            time.sleep(0.5)
        return show_menu


    def grab_data():
        player_x, player_y = [1350, 4700]
        return player_x, player_y

    def draw_pointer(x_pointer, y_pointer, color):
        pointer_thickness = 20
        pm.draw_pixel(x_pointer, y_pointer, color)
        pm.draw_line(x_pointer-pointer_thickness/2, y_pointer, x_pointer+pointer_thickness/2, y_pointer, color, 1)
        pm.draw_line(x_pointer, y_pointer-pointer_thickness/2, x_pointer, y_pointer+pointer_thickness/2, color, 1)


