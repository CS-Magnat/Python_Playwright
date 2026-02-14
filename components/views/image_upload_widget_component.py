from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.input import Input
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # Используем компонент EmptyViewComponent
        self.preview_empty_view = EmptyViewComponent(page, identifier)

        # self.preview_image = page.get_by_test_id(f'{identifier}-image-upload-widget-preview-image')
        # self.image_upload_info_icon = page.get_by_test_id(f'{identifier}-image-upload-widget-info-icon')
        # self.image_upload_info_title = page.get_by_test_id(f'{identifier}-image-upload-widget-info-title-text')
        # self.image_upload_info_description = page.get_by_test_id(
        #     f'{identifier}-image-upload-widget-info-description-text'
        # )
        self.preview_image = Image(page,f'{identifier}-image-upload-widget-preview-image', 'upload-widget-preview')
        self.image_upload_info_icon = Icon(page,f'{identifier}-image-upload-widget-info-icon', 'upload-widget-info')
        self.image_upload_info_title = Text(page,f'{identifier}-image-upload-widget-info-title-text', 'upload-widget-info-title')
        self.image_upload_info_description = Text(page,f'{identifier}-image-upload-widget-info-description-text', 'upload-widget-info-description')


        # self.upload_button = page.get_by_test_id(f'{identifier}-image-upload-widget-upload-button')
        # self.remove_button = page.get_by_test_id(f'{identifier}-image-upload-widget-remove-button')
        # self.upload_input = page.get_by_test_id(f'{identifier}-image-upload-widget-input')
        self.upload_button = Button(page,f'{identifier}-image-upload-widget-upload-button', 'upload-widget-upload')
        self.remove_button = Button(page,f'{identifier}-image-upload-widget-remove-button', 'upload-widget-remove')
        self.upload_input = FileInput(page,f'{identifier}-image-upload-widget-input', 'upload-widget-input')




    # Проверяет отображение виджета в зависимости от наличия загруженного изображения
    def check_visible(self, is_image_uploaded: bool = False):
        # expect(self.image_upload_info_icon).to_be_visible()
        #
        # expect(self.image_upload_info_title).to_be_visible()
        # expect(self.image_upload_info_title).to_have_text(
        #     'Tap on "Upload image" button to select file'
        # )
        #
        # expect(self.image_upload_info_description).to_be_visible()
        # expect(self.image_upload_info_description).to_have_text('Recommended file size 540X300')
        #
        # expect(self.upload_button).to_be_visible()
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(
            'Tap on "Upload image" button to select file'
        )

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.upload_button.check_visible()



        # if is_image_uploaded:
        #     # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
        #     expect(self.remove_button).to_be_visible()
        #     expect(self.preview_image).to_be_visible()
        #
        # if not is_image_uploaded:
        #     # Если картинка не загружена, проверяем наличие компонента EmptyViewComponent
        #     self.preview_empty_view.check_visible(
        #         title='No image selected',
        #         description='Preview of selected image will be displayed here'
        #     )
        #

        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            self.remove_button.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            # Если картинка не загружена, проверяем наличие компонента EmptyViewComponent
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )


    def click_remove_image_button(self):
        # self.remove_button.click()
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)
