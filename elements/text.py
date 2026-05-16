from elements.base_element import BaseElement


class Text(BaseElement):
    """
    Element wrapper for generic text containers (e.g., <p>, <span>, headers).
    Inherits all visibility and interaction checks from BaseElement.
    """

    @property
    def type_of(self) -> str:
        """Returns the specific type of this element."""
        return "text"