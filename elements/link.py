from elements.base_element import BaseElement


class Link(BaseElement):
    """
    Element wrapper for hyperlink tags (<a>).
    Inherits all visibility and interaction checks from BaseElement.
    """

    @property
    def type_of(self) -> str:
        """Returns the specific type of this element."""
        return "link"