from flet import *
import flet as ft


def main(page: Page):
    page.title = "Contratar Serviços"
    page.bgcolor = colors.WHITE
    page.window_height = 800
    page.window_width = 600
    page.window_maximizable = False
    page.window_resizable = False

    def esqueceu_senha(e):
        page.controls.clear()
        print('ola')
        pass

    titulo = Text("Contrate um Serviço"
                  , color=colors.TEAL
                  , size=50
                  , text_align=alignment.center
                  )

    email = Text("Email", color=colors.BLACK, size=30)

    entrada_email = TextField(
        label="Digite seu email"
        , hint_text="Digite o email cadastrado"
        , color=colors.TEAL
        , icon=icons.EMAIL
    )

    senha = Text("Senha", color=colors.BLACK, size=30)

    entrada_senha = TextField(
        label="Digite sua senha"
        , hint_text="Digite a senha cadastrado"
        , color=colors.TEAL
        , icon=icons.PASSWORD
        , password=True
    )

    btn_entrar = ElevatedButton(
        text="Entrar"
        , color=colors.BLACK
        , bgcolor=colors.WHITE10
        , width=150
    )
    esqueceu_senha = Text("Não tem conta, Realize seu ", spans=[
        ft.TextSpan("Cadastro"
                    , TextStyle(weight=ft.FontWeight.BOLD)
                    , on_click=esqueceu_senha
                    , ), ]
                          , color=colors.BLACK
                          )

    page.add(titulo, email, entrada_email, senha, entrada_senha, esqueceu_senha, btn_entrar)


ft.app(target=main)
