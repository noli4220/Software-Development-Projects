import flet as ft

def main(page: ft.Page):
    
    number = ft.Text(value="0", text_align=ft.TextAlign.CENTER, size=100, color=ft.colors.WHITE)

    def minus_click(e):
        number.value = str(int(number.value) - 1)
        page.update()

    def plus_click(e):
        number.value = str(int(number.value) + 1)
        page.update()

    
    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"
    page.bgcolor ="#FF97E5"
    page.window_height =700
    page.window_width =400

    petImage = ft.Image(src="https://pbs.twimg.com/media/GDHQxvCX0AAfqGR.jpg", height=200, width=200)
    title = ft.Text(value="Coquette counter", size=40, font_family="roboto", color=ft.colors.WHITE)
    minusbutton = ft.IconButton(ft.icons.REMOVE, on_click=minus_click, icon_size=40, bgcolor=ft.colors.PINK_50)
    addbutton = ft.IconButton(ft.icons.ADD, on_click=plus_click, icon_size=40, bgcolor=ft.colors.PINK_50)
    page.add(
                
            petImage,
            title, 
            minusbutton, number, addbutton, 
            )
    page.update()

ft.app(target=main)

