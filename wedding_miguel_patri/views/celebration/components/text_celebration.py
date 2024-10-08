import reflex as rx

from wedding_miguel_patri.styles import Size
from wedding_miguel_patri.utils import utils


def text_celebration() -> rx.Component:
    return rx.flex(
        rx.text(utils.wedding_place, font_weight="bold", as_="span"),
        rx.text(utils.wedding_address_street),
        rx.text(utils.wedding_address_province),
        font_size=[
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
        ],
    )
