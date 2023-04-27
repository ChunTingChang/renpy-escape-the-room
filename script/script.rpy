# scene

# image main_menu = Movie(play="images/menu.webm")

image dark_1_room_3_scene_1 = im.MatrixColor(
    "images/scene/room_3/scene/room_3_scene_1.jpeg",
    im.matrix.brightness(-0.5))

image dark_2_room_3_scene_1 = im.MatrixColor(
    "images/scene/room_3/scene/room_3_scene_1.jpeg",
    im.matrix.brightness(-0.2))

# player

define gui.name_text_color = '#7a7979'
define player_f = Character('？？？', image = 'player')
# ""
define father = Character('爸爸') # , image = 'player'
define mother = Character('媽媽')

# image side player = "images/character/player.png"

image player = "images/character/girl_delight.png"
image side player = "images/character/side_girl_worried.png"
image side player fear = "images/character/side_girl_fear.png"

define start_room = 1
define start_scene = 5

define scenes_viewed = [ ]

# room_1

define girl_paint_clicked_cnt = 0

define room_1_photos_clicked_cnt = 0

define room_1_table_clicked_cnt = 0

# define room_1_wall_shelf_clicked_cnt = 0

define room_1_door_2_trigger = 0

define room_1_door_3_trigger = 0

define room_1_girl_paint_1_trigger = 0

# room_2

define room_2_wall_deco_1_clicked_cnt = 0

define room_2_clothing_1_clicked_cnt = 0

define room_2_clothing_2_clicked_cnt = 0

define room_2_bag_1_clicked_cnt = 0

define room_2_photos_2_clicked_cnt = 0

define room_2_table_2_clicked_cnt = 0

define room_2_box_1_clicked_cnt = 0

define room_2_clothing_2_trigger = 0

define room_2_box_1_trigger = 0

define room_2_table_2_trigger = 0

# room_3

define room_3_mirror_1_clicked_cnt = 0

define room_3_candle_1_clicked_cnt = 0

define room_3_candle_2_clicked_cnt = 0

define room_3_mirror_1_trigger = 0

# audio

# init python:
#     renpy.music.register_channel(name='add_bgm', mixer = 'music', loop=True)

# define audio.main_bgm = "audio/bgm/for_test.ogg" # 測試
define audio.main_bgm = "audio/bgm/main_bgm.mp3" # 正式
# define audio.laptop_bgm = "audio/bgm/laptop_bgm.ogg"

# define audio.room_3_bgm = "audio/bgm/room_3_bgm.ogg"
# define audio.memory_bgm = "audio/bgm/memory_bgm.ogg"
# define audio.memory_part2_tense_bgm = "audio/bgm/memory_part2_sound.ogg"
# define audio.fire_bgm = "audio/bgm/fireplace.mp3"
# define audio.sound_effect_item_hover = "audio/sound_effect/item_hover.mp3"

# $ config.window_auto_hide = ['call screen', 'scene'] #  'scene', 'call screen', 'menu', "say-centered"

# define scene_2_clicked_cnt = 0
screen directions:
# https://www.youtube.com/watch?v=4O3uqLpvnKE
    if start_room == 1:

        if start_scene <> 1:

            imagebutton:
                xalign 0.2 yalign 0.9
                auto "images/direction_button/left_button_%s.png"
                action [ToggleVariable("start_scene", start_scene-1), Jump("scene_non_trigger")]

        if start_scene <> 5:

            imagebutton:
                xalign 0.8 yalign 0.9
                auto "images/direction_button/right_button_%s.png"
                action [ToggleVariable("start_scene", start_scene+1), Jump("scene_non_trigger")]

    elif start_room == 2:

        if start_scene <> 1:

            imagebutton:
                xalign 0.2 yalign 0.9
                auto "images/direction_button/left_button_%s.png"
                action [ToggleVariable("start_scene", start_scene-1), Jump("scene_non_trigger")]

        if start_scene <> 4:

            imagebutton:
                xalign 0.8 yalign 0.9
                auto "images/direction_button/right_button_%s.png"
                action [ToggleVariable("start_scene", start_scene+1), Jump("scene_non_trigger")]


label start:

    play music main_bgm volume 1.0 fadein 1.0

    "你相信死後的世界嗎？"

    "你知道嗎？即便生前活得多麼痛苦 ... "

    "死後並不會解脫。"

    "而是會不斷重複死前的過程。"

    pause 0.3

    $ renpy.scene()
    $ renpy.show("room_%s_scene_%s" %(start_room, start_scene))
    $ renpy.with_statement(fade)

    player_f "....."

    player_f "這裡是？"

    player_f fear "（向前走了幾步）"

    $ start_scene = 4

    $ renpy.scene()
    $ renpy.show("room_%s_scene_%s" %(start_room, start_scene))
    $ renpy.with_statement(fade)

    player_f "冷靜下來，想辦法出去吧。"

    "請透過視窗下方箭頭切換畫面"

    window hide

    call scene_non_trigger from _call_scene_non_trigger_13


label scene_non_trigger:

    $ renpy.scene()

    $ renpy.show("room_%s_scene_%s" %(start_room, start_scene))

    $ renpy.with_statement(fade)

    if girl_paint_clicked_cnt == 2:

        play sound "audio/sound_effect/door_open.mp3"

        "傳來了門鎖打開的聲音。"

        $ girl_paint_clicked_cnt += 1

    elif room_2_table_2_trigger == 1:

        play sound "audio/sound_effect/door_open.mp3"

        "傳來了門鎖打開的聲音。"

        $ room_2_table_2_trigger += 1

    elif room_3_mirror_1_trigger == 1:

        play add_bgm fire_bgm

        "從畫像傳來奇怪的聲音"

        "聽起來像是什麼東西燒起來了？"

        $ room_3_mirror_1_trigger += 1

    elif room_1_girl_paint_1_trigger == 1:

        player_f "畫像真的是我自己嗎？"

        player_f fear "再回去剛才的房間，看看鏡子吧 ..."

        $ room_1_girl_paint_1_trigger += 1




    $ renpy.call_screen("room_%s_scene_%s_buttons" % (start_room, start_scene))
