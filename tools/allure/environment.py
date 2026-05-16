from config import settings


def create_allure_environment_file():
    """
    Generates an `environment.properties` file in the Allure results directory.
    
    The file contains all current settings as key-value pairs, which Allure 
    uses to display the test environment information in the HTML report.
    """
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)