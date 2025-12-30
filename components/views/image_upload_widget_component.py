from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # Используем компонент EmptyViewComponent
        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = page.get_by_test_id(f'{identifier}-image-upload-widget-preview-image')

        self.image_upload_info_icon = page.get_by_test_id(f'{identifier}-image-upload-widget-info-icon')
        self.image_upload_info_title = page.get_by_test_id(f'{identifier}-image-upload-widget-info-title-text')
        self.image_upload_info_description = page.get_by_test_id(
            f'{identifier}-image-upload-widget-info-description-text'
        )

        self.upload_button = page.get_by_test_id(f'{identifier}-image-upload-widget-upload-button')
        self.remove_button = page.get_by_test_id(f'{identifier}-image-upload-widget-remove-button')
        self.upload_input = page.get_by_test_id(f'{identifier}-image-upload-widget-input')