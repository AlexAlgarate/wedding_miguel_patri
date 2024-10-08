import reflex as rx

from wedding_miguel_patri.utils import urls, utils


def image_celebration(image: str) -> rx.Component:
    """
    Create a linked celebration image component with a tooltip.

    Parameters:
    - image (str): The path or URL of the celebration image.
    - alt (str): Alternative text for the image.

    Returns:
    - rx.Component: A Reflex component representing the linked celebration image with a tooltip.

    The image is wrapped in a link that leads to a specific URL (AGROPINA_URL).
    The tooltip provides additional information about the image when hovered.
    """

    return rx.link(
        rx.image(
            src=image,
            box_shadow="""
                1px 1px 4px 1px rgba(0, 0, 0, 0.3)
                """,
            alt=utils.alt_image_celebration,
            width="100%",
        ),
        href=urls.MONTEALVAR_URL,
        is_external=True,
    )
