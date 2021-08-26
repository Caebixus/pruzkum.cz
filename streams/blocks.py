from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class CardBlock(blocks.StructBlock):
    """ Cards with team """

    title = blocks.CharBlock(required=True, help_text="Napiš jméno a příjmení zaměstnance")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("prijmeni", blocks.CharBlock(required=True, max_length=40)),
                ("description", blocks.TextBlock(required=False, max_length=200)),
                ("phone", blocks.CharBlock(required=False, max_length=100)),
                ("email", blocks.CharBlock(required=False, max_length=60)),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "group"
        label = "Lidé"

class HeaderMenuBlock(blocks.StructBlock):
    """ Header menu """

    button_text = blocks.CharBlock(required=True, max_length=20)
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)


    class Meta:
        template = "home/header_menu_blocks.html"
        icon = "home"
        label = "navigační menu"
