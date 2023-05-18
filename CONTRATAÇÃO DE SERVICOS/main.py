import flet as ft
from PIL import Image

def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 800
    page.window_resizable = False
    page.title = "Contratação de Serviços"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("CONTRATAÇÃO DE SERVIÇOS", ), bgcolor=ft.colors.SURFACE_VARIANT, ),
                    ft.ElevatedButton("Realizar Login", on_click=lambda _: page.go("/LOGIN")),
                    ft.ElevatedButton("Realizar Cadastro", on_click=lambda _: page.go("/CADASTRO")),

                ], bgcolor=ft.colors.WHITE12, vertical_alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        if page.route == "/LOGIN":
            page.views.append(
                ft.View(
                    "/LOGIN",
                    [
                        ft.AppBar(title=ft.Text("LOGIN"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.Text("Contratação de Serviços Gerais", text_align=ft.TextAlign.CENTER,
                                color=ft.colors.WHITE, size=30, height=50, width=800, font_family="Consolas"),

                        ft.Text(" REALIZAR LOGIN", text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, size=40,
                                font_family="Tahoma", ),

                        ft.TextField(label="Email ou Usuário", hint_text="Digite seu Email ou usuário",
                                     icon=ft.icons.EMAIL_SHARP,
                                     bgcolor=ft.colors.SURFACE, text_size=20, autofocus=True, border_radius=1,
                                     border_color=ft.colors.LIGHT_GREEN_ACCENT),

                        ft.TextField(label="Senha", hint_text="Digite sua Senha", icon=ft.icons.PASSWORD_SHARP,
                                     password=True,
                                     bgcolor=ft.colors.SURFACE, text_size=20, autofocus=True, border_radius=1,
                                     border_color=ft.colors.LIGHT_GREEN_ACCENT),
                        ft.Text("Não tem conta, Realize seu ", spans=[
                            ft.TextSpan("Cadastro", ft.TextStyle(weight=ft.FontWeight.BOLD),
                                        on_click=lambda _: page.go("/CADASTRO"), ), ]
                                ),

                        ft.ElevatedButton(text="FAZER LOGIN", on_click=lambda _: page.go("/LOGIN"), height=60, ),

                        ft.ElevatedButton("PAGINA INICIAL", on_click=lambda _: page.go("/")),
                    ], bgcolor=ft.colors.WHITE12, vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/CADASTRO":
            page.views.append(
                ft.View(
                    "/CADASTRO",
                    [
                        ft.AppBar(title=ft.Text("CADASTRO"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("REALIZE O SEU CADASTRO", text_align=ft.TextAlign.CENTER,
                                color=ft.colors.WHITE, size=30, height=50, width=800, font_family="Consolas", ),
                        ft.TextField(label="Nome", hint_text="Escreva seu primeiro Nome",
                                     bgcolor=ft.colors.SURFACE, text_size=20, autofocus=True, border_radius=1,
                                     border_color=ft.colors.LIGHT_GREEN_ACCENT),
                        ft.TextField(label="Sobrenome", hint_text="Escreva seu(s) sobrenome(s)",
                                     bgcolor=ft.colors.SURFACE, text_size=20, autofocus=True, border_radius=1,
                                     border_color=ft.colors.LIGHT_GREEN_ACCENT),


                        ft.ElevatedButton("PAGINA INICIAL", on_click=lambda _: page.go("/")),
                    ], bgcolor=ft.colors.WHITE12, vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
