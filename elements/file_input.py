from elements.base_element import BaseElement
import allure

# class FileInput(BaseElement):
#     def set_input_files(self, file: str, **kwargs):
#         locator = self.get_locator(**kwargs)
#         locator.set_input_files(file)

class FileInput(BaseElement):

    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "file input"


    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        with allure.step(f'Set file "{file}" to the {self.type_of} "{self.name}"'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)