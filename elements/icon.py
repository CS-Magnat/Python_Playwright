from elements.base_element import BaseElement


class Icon(BaseElement):
    """
    Element wrapper for UI icons.
    Inherits all visibility and interaction checks from BaseElement.
    """

    @property
    def type_of(self) -> str:
        """Returns the specific type of this element."""
        return "icon"