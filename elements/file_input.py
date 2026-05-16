from elements.base_element import BaseElement
import allure
from tools.logger import get_logger


logger = get_logger("FILE_INPUT")

class FileInput(BaseElement):
    """
    Element wrapper for file upload inputs (<input type="file">).
    
    Provides specialized methods for attaching files to the DOM.
    """

    @property
    def type_of(self) -> str:
        """Returns the specific type of this element."""
        return "file input"


    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        """
        Uploads a local file by providing its path to the input element.
        """
        step = f'Set file "{file}" to the {self.type_of} "{self.name}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(file)