from typing import Any

from typing_extensions import Literal, TypeAlias, TypedDict

from .webelement import WebElement

LogType: TypeAlias = Literal["browser", "driver", "client", "server"]

LogLevel: TypeAlias = Literal["WARNING", "ERROR", "SEVERE"]

class LogEntry(TypedDict):
    message: str
    level: LogLevel

class WebDriver:
    def get(self, url: str) -> None: ...

    def maximize_window(self) -> None: ...

    def get_screenshot_as_png(self) -> bytes: ...

    def execute_script(self, script: str, *args: Any) -> Any: ...

    def get_log(self, log_type: LogType) -> list[LogEntry]: ...

    def set_window_size(self, width: int, height: int) -> None: ...

    def quit(self) -> None: ...

    def implicitly_wait(self, time_to_wait: int) -> None: ...

    def find_element_by_id(self, id: str) -> WebElement: ...
    def find_elements_by_id(self, id: str) -> list[WebElement]: ...
    def find_element_by_xpath(self, xpath: str) -> WebElement: ...
    def find_elements_by_xpath(self, xpath: str) -> list[WebElement]: ...
    def find_element_by_link_text(self, link_text: str) -> WebElement: ...
    def find_elements_by_link_text(self, link_text: str) -> list[WebElement]: ...
    def find_element_by_partial_link_text(self, link_text: str) -> WebElement: ...
    def find_elements_by_partial_link_text(self, link_text: str) -> list[WebElement]: ...
    def find_element_by_name(self, name: str) -> WebElement: ...
    def find_elements_by_name(self, name: str) -> list[WebElement]: ...
    def find_element_by_tag_name(self, name: str) -> WebElement: ...
    def find_elements_by_tag_name(self, name: str) -> list[WebElement]: ...
    def find_element_by_class_name(self, name: str) -> WebElement: ...
    def find_elements_by_class_name(self, name: str) -> list[WebElement]: ...
    def find_element_by_css_selector(self, css_selector: str) -> WebElement: ...
    def find_elements_by_css_selector(self, css_selector: str) -> list[WebElement]: ...
    #def find_element(self, by=By.ID, value=None):
    #def find_elements(self, by=By.ID, value=None):