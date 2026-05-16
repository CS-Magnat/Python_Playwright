from elements.base_element import BaseElement


class Image(BaseElement):
    """
    Element wrapper for image tags (<img>).
    Inherits all visibility and interaction checks from BaseElement.
    """

    @property
    def type_of(self) -> str:
        """Returns the specific type of this element."""
        return "image"