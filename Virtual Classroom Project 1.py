#References: https://flet.dev/docs/controls/floatingactionbutton/, https://flet.dev/docs/controls/page/#fonts, https://flet.dev/blog/using-custom-fonts-in-flet-app/, https://flet.dev/docs/controls/container, https://flet.dev/docs/guides/python/colors/, https://flet-controls-gallery.fly.dev/colors/colorpalettes
import flet as ft

def main(page: ft.Page):
    page.title = "Virtual Classroom"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.auto_scroll = True
    page.scroll = ft.ScrollMode.HIDDEN
    page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100, height= 40)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    page.add(
        ft.Row(
            [
                ft.Stack(
                    [
                        ft.Container(
                            bgcolor= ft.colors.INDIGO_900,
                            width=1500,
                            height=100,
                            alignment=ft.alignment.center,
                            padding= 200,
                        ),

                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    "                                                  VIRTUAL CLASSROOM",
                                    ft.TextStyle(
                                        size=50,
                                        weight=ft.FontWeight.BOLD,
                                        font_family="Kanit",
                                        foreground=ft.Paint(
                                            color=ft.colors.GREY_50,
                                            stroke_width=11,
                                            stroke_join=ft.StrokeJoin.ROUND,
                                            style=ft.PaintingStyle.STROKE,
                                        ),
                                    ),
                                ),
                            ],
                        ),

                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    "                                                  VIRTUAL CLASSROOM",
                                    ft.TextStyle(
                                        size=50,
                                        weight=ft.FontWeight.BOLD,
                                        font_family="Kanit",
                                        foreground=ft.Paint(
                                            color=ft.colors.ORANGE_600,
                                            stroke_width=6,
                                            stroke_join=ft.StrokeJoin.ROUND,
                                            style=ft.PaintingStyle.STROKE,
                                        ),
                                    ),
                                ),
                            ],
                        ),

                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    "                                                  VIRTUAL CLASSROOM",
                                    ft.TextStyle(
                                        size=50,
                                        weight=ft.FontWeight.BOLD,
                                        font_family="Kanit",
                                        color=ft.colors.GREY_50,
                                    ),
                                ),
                            ],
                        ),
                    ],
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.count = 1

    def fab_pressed(e):
        page.add(
            ft.Row(
            [   
                ft.CupertinoTextField(
                placeholder_text= f"Student {page.count}", width= 600),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click, icon_color= ft.colors.INDIGO_900),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click, icon_color= ft.colors.INDIGO_900),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        page.show_snack_bar(
            ft.SnackBar(ft.Text("Student added successfully!", font_family="Kanit"), open=True, bgcolor= ft.colors.INDIGO_900)
        )
        page.count += 1

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=fab_pressed, bgcolor=ft.colors.ORANGE_600,
    )
    page.add(ft.Text(spans=[ft.TextSpan("Students", ft.TextStyle(size=30,weight=ft.FontWeight.BOLD,font_family="Kanit", color=ft.colors.INDIGO_900))]))

ft.app(target=main)