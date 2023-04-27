
screen room_1_scene_1_buttons:

    use directions

    imagebutton:
        xpos (1024-105) ypos (173-117)
        auto "images/scene/room_1/object/room_1_scene_1_girl_paint_1_%s.png"
        # # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("girl_paint_highlight")

    imagebutton:
        xpos (1280-210) ypos (720-278)
        auto "images/scene/room_1/object/room_1_scene_1_table_1_%s.png"
        # # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_table_highlight")

screen room_1_scene_2_buttons:

    use directions

    imagebutton:
        xpos 415 ypos 66
        auto "images/scene/room_1/object/scene_2_girl_paint_highlight_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("girl_paint_highlight")

    imagebutton:
        xpos (748-157) ypos (467-102)
        auto "images/scene/room_1/object/room_1_scene_2_table_1_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_table_highlight")

    imagebutton:
        xpos (1280-231) ypos (250-86)
        auto "images/scene/room_1/object/room_1_scene_2_photos_1_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_photos_highlight")

screen room_1_scene_3_buttons:

    use directions

    imagebutton:
        xpos 797 ypos 168
        auto "images/scene/room_1/object/scene_3_photos_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_photos_highlight")

    imagebutton:
        xpos 536 ypos 378
        auto "images/scene/room_1/object/scene_3_table_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_table_highlight")

    imagebutton:
        xpos 0 ypos 0
        auto "images/scene/room_1/object/room_1_scene_3_girl_paint_1_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("girl_paint_highlight")

screen room_1_scene_4_buttons:

    use directions

    imagebutton:
        xpos 783 ypos 392
        auto "images/scene/room_1/object/room_1_scene_4_door_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_door2")

    imagebutton:
        xpos (280-153) ypos (481-107)
        auto "images/scene/room_1/object/room_1_scene_4_table_1_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_table_highlight")

    imagebutton:
        xpos (423-84) ypos (217-52)
        auto "images/scene/room_1/object/room_1_scene_4_photos_1_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_photos_highlight")

screen room_1_scene_5_buttons:

    use directions

    imagebutton:
        xpos (671-95) ypos (392-67)
        auto "images/scene/room_1/object/room_1_scene_5_door_2_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_door2")

    imagebutton:
        xpos (1051-124) ypos (479-107)
        auto "images/scene/room_1/object/room_1_scene_5_door_3_%s.png"
        # hover_sound "audio/sound_effect/item_hover.mp3"
        action Jump("room1_door3")



label room1_door2:

    if (girl_paint_clicked_cnt > 1): #  & (room_1_wall_shelf_clicked_cnt > 1)

        "門把可以轉動。"

        $ room_1_door_2_trigger = 1

        menu:

            "是否進入房間？"

            "進入房間":

                $ start_room = 2
                $ start_scene = 4

                # play sound "audio/sound_effect/door_open.wav" volume 0.5

                jump ending

            "再等等":

                call scene_non_trigger from _call_scene_non_trigger_3

    else:

        "門已上鎖。"

        call scene_non_trigger from _call_scene_non_trigger_4 # from _call_scene_non_trigger

    # hide window


label room1_door3:

    if (room_1_door_2_trigger >= 1) & (room_2_table_2_trigger >= 1):

        "門把可以轉動。"

        $ room_1_door_3_trigger = 1

        menu:

            "是否進入房間？"

            "進入房間":

                $ start_room = 3
                $ start_scene = 1

                # play sound "audio/sound_effect/door_open.wav" volume 0.5

                stop music

                # play music room_3_bgm

                call scene_non_trigger from _call_scene_non_trigger_5

            "再等等":

                call scene_non_trigger from _call_scene_non_trigger_6


    else:

        "門已上鎖。"

    call scene_non_trigger from _call_scene_non_trigger_7 # from _call_scene_non_trigger


label room1_photos_highlight:

    scene zoom_in_scene_3_photos with fade

    "左側擺著婚紗照。照片中的新人看起來幸福洋溢。"

    "沒什麼其他線索。"

    $ room_1_photos_clicked_cnt += 1

    call scene_non_trigger from _call_scene_non_trigger_8

label room1_table_highlight:

    scene zoom_in_scene_3_table with fade

    "十幾年前的雜誌。"

    "雜誌標題：身心靈的調劑，療養與退休生活的最佳首選——烙岩鎮。"

    "愜意生活就應該伴隨鳥鳴花香，一起來探索美妙的大自然。烙岩鎮不僅醫療與教育資源充足，更被評選為本國自然環境保留最完整的市鎮之一。"

    player_f "似乎是地方特色專欄？"

    "沒什麼其他線索。"

    $ room_1_table_clicked_cnt += 1

    call scene_non_trigger from _call_scene_non_trigger_9

label girl_paint_highlight:

    if room_3_mirror_1_trigger >= 1:

        scene zoom_girl_paint_clicked with fade

        player_f fear "這張畫像 ...."

        player_f fear "為什麼變成了我的臉呢？！"

        $ room_1_girl_paint_1_trigger += 1

    elif girl_paint_clicked_cnt == 0:

        scene zoom_girl_paint with fade

        "幼齡女孩的畫像。目測年齡大約是小學年紀？"

        "沒什麼其他線索。"

    else:

        scene zoom_girl_paint_clicked with fade

        "幼齡女孩的畫像。"

        "畫像似乎和第一次看有些不同？"

        "女孩的皮膚有些異常。"

        player_f "看起來是燒燙傷導致的疤痕 ..."

    $ girl_paint_clicked_cnt += 1

    call scene_non_trigger from _call_scene_non_trigger_1

label back_to_room_1:

    # play sound "audio/sound_effect/door_open.wav" volume 0.5

    $ start_scene = 5
    $ start_room = 1

    call scene_non_trigger from _call_scene_non_trigger_10

label ending:

    scene black with dissolve

    stop music

    # stop add_bgm

    play music "audio/bgm/bgm_logo_opening.mp3" noloop

    show player

    "試玩結束，謝謝您撥冗體驗這款測試遊戲～"

    "歡迎到官方頁面免費下載遊戲：點我到官方網站！"

    "嚴正申明：關於遊戲相關的音樂、音效、圖像並非本人所有，是採用非商用授權之來源。"

    "音樂：Creative Commons Music by Jason Shaw on {a=https://audionautix.com/}Audionautix.com{/a} "

    "音效：Sound Effect from {a=https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6038}Pixabay{\a}"

    "遊戲室內圖：{a=https://3d.homestyler.com/}Homestyler.com{/a}"

    "角色（女兒）圖片：{a=https://charat.me/en/genesis/create/}charat.me{/a}"

    "若有任何心得，都歡迎分享給遊戲製作人：gt.bianalyst@gmail.com"

    "開發相關內容，都會分享在{a=https://www.bianalyst-gt.com/}部落格{/a}，也歡迎點擊支持唷！"

    scene black with fade

    $ MainMenu(confirm=False)()
