from elements.base_element import BaseElement
import allure

from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("FILE_INPUT")  # Инициализируем logger

# class FileInput(BaseElement):
#     def set_input_files(self, file: str, **kwargs):
#         locator = self.get_locator(**kwargs)
#         locator.set_input_files(file)

class FileInput(BaseElement):

    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "file input"


    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        step = f'Set file "{file}" to the {self.type_of} "{self.name}"'
        with allure.step(step):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            locator.set_input_files(file)