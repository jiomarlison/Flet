from flet import *
from io import BytesIO
import qrcode
import base64


def morning(s):
    qr = qrcode.make(s)
    buffered = BytesIO()
    qr.save(buffered, format="JPEG")
    s1 = base64.b64encode(buffered.getvalue())
    resultado_qr_code = s1.decode("utf-8")
    return (resultado_qr_code)


def main(page: Page):
    page.scroll = "always"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"


    def visualizar_qr(s):
        if login.value == '' or senha.value == '':
            entrar.bgcolor = colors.RED
            page.add(Text("Insira senha e o usuario"))
            page.update()
        else:
            page.controls.clear()
            def procedtocode(e):
                url = morning([nome.value, cadastro.value])
                img = Image(src_base64=url)
                imagem_qrcode = qrcode.make([nome.value, cadastro.value])
                imagem_qrcode.save(f"QRcode {nome.value} - {cadastro.value}.PNG")
                page.add(img)
                page.update()

            nome = TextField(label="Insira o nome completo")
            cadastro = TextField(label='Digite o cadastro')
            btn = ElevatedButton("Exibir QRcode", on_click=procedtocode, bgcolor="blue", color="white")

            page.add(nome, cadastro, btn)
            page.update()


    login = TextField(label="Usuário")
    senha = TextField(label="Senha")
    entrar = ElevatedButton("entrar", on_click=visualizar_qr)
    page.add(login, senha, entrar)

flet.app(target=main)
