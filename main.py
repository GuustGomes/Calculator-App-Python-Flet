import flet as ft
from flet import Colors
from decimal import Decimal


botoes = [
    {'operador': 'AC', 'fonte': Colors.BLACK, 'fundo': Colors.GREY},
    {'operador': '±', 'fonte': Colors.BLACK, 'fundo': Colors.GREY},
    {'operador': '%', 'fonte': Colors.BLACK, 'fundo': Colors.GREY},
    {'operador': '/', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '7', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '8', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '9', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '*', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '4', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '5', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '6', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '-', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '1', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '2', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '3', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '+', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '0', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '.', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE_24},
    {'operador': '=', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},

]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window.resizable = False
    page.window.width = 320
    page.window.height = 480
    page.title = 'Calculadora'
    page.window.always_on_top = True

    result = ft.Text(value = '0', color = Colors.WHITE, size = 40)

    def calculate(operador, value_at):
        try:
            value = eval(value_at)

            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
        except:
            return 'Error'

        digits = min(abs(Decimal(value).as_tuple().exponent),5)
        return format(value, f'.{digits}f')

    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value='0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=', '%', '±'):
                value = calculate(operador=value[-1], value_at=value_at)

        result.value = value
        result.update()

    display = ft.Row(
        width=320,
        controls=[result],
        alignment = ft.MainAxisAlignment.END,
    )

    btn = [ft.Container(
            content=ft.Text(value=btn['operador'], color= btn['fonte']),
            width=60,
            height=60,
            bgcolor=btn['fundo'],
            border_radius= 100,
            alignment=ft.Alignment(0, 0),
            on_click=select
        )for btn in botoes]


    keyboard = ft.Row(
        width = 320,
        wrap = True,
        controls=btn,
        alignment=ft.MainAxisAlignment.END,
    )

    page.add(display, keyboard)



ft.app(target = main)