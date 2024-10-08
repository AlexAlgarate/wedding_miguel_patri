import reflex as rx

from wedding_miguel_patri.components import card, text_section, title_section
from wedding_miguel_patri.styles import Color, FontWeight
from wedding_miguel_patri.utils import utils

from .components import whatsapp_button


def accomodation() -> rx.Component:
    return card(
        rx.icon(
            "bed",
            size=60,
            stroke_width=0.8,
            color=Color.TITLES.value,
            max_height="auto",
        ),
        title_section(title=utils.accomodation_title),
        text_section(utils.accomodation_main_text),
        text_section(
            utils.accomodation_ask_info,
            font_weight=FontWeight.HIGH.value,
        ),
        whatsapp_button(utils.contact_bride, utils.contact_groom),
        id="contact_section",
    )
