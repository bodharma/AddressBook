from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class EditAddressesLocators:
    # locator_new_address_link = (By.LINK_TEXT, "New Address")
    locator_list_link = (By.LINK_TEXT, "List")
    locator_show_address_link = (By.LINK_TEXT, "Show")
    # locator_edit_address_link = (By.LINK_TEXT, "Edit")
    # locator_destroy_address_link = (By.LINK_TEXT, "Destroy")
    locator_first_name_field = (By.NAME, "address[first_name]")
    locator_last_name_field = (By.NAME, "address[last_name]")
    locator_address1_field = (By.NAME, "address[address1]")
    locator_address2_field = (By.NAME, "address[address2]")
    locator_city = (By.NAME, "address[city]")
    locator_state = (By.NAME, "address[state]")
    locator_zip_code = (By.NAME, "address[zip_code]")
    locator_address_country_us = (By.ID, "address_country_us")
    locator_address_country_canada = (By.ID, "address_country_canada")
    locator_address_state = (By.XPATH, '/*[@id="new_address"]/div[8]')
    locator_birthday = (By.NAME, "address[birthday]")
    locator_color = (By.NAME, "address[color]")
    locator_age = (By.NAME, "address[age]")
    locator_website = (By.NAME, "address[website]")
    locator_picture = (By.ID, 'address_picture')
    locator_phone = (By.NAME, "address[phone]")
    locator_climbing = (By.ID, "address_interest_climb")
    locator_dancing = (By.ID, "address_interest_dance")
    locator_reading = (By.ID, "address_interest_read")
    locator_note = (By.ID, "address_note")
    locator_update_address_btn = (By.NAME, "commit")
    # locator_result_container = (By.CLASS_NAME, "container")
    # locator_container_options = (By.XPATH, "//p")
    # locator_destroyed_message = (By.XPATH, "/html/body/div/div")
    locator_required_fields_error = (By.XPATH, ".//div[@id = 'error_explanation']")


class EditAddressPage(BasePage):
    def click_on_element_if_yes(self, locator, option):
        element = self.find_element(locator)
        if option == 'Yes':
            return element.click()
        elif option == 'No':
            element.get_attribute("checked")
            if element.get_attribute("checked"):
                element.click()
            else:
                pass
        else:
            raise Exception("Provide 'Yes' or 'No'")

    def set_data_to_field(self, field_locator, data):
        return self.find_element(
            field_locator, time=2)\
            .send_keys(data)

    def select_dropdown_option(self, dropdown_locator, value):
        dropdown = Select(self.find_element(
            dropdown_locator, time=2))
        return dropdown.select_by_value(value)

    def select_element_by_locator(self, locator):
        element = Select(self.find_element(locator))
        return element

    def select_state(self, state):
        if state == "us":
            self.click_on_element(EditAddressesLocators.locator_address_country_us)
        elif state == "canada":
            self.click_on_element(EditAddressesLocators.locator_address_country_canada)
        else:
            pass

    def clean_field(self, locator):
        return self.find_element(locator).clear()

    def click_update_address_btn(self):
        self.wait_until_element_clickable(
            (By.NAME, "commit")
        )

        update_address_btn = self.driver.find_element(
            By.NAME, "commit"
        )

        update_address_btn.click()

        self.find_element(
            (By.CLASS_NAME, "container")
        )


# class Converters:
#     def hex_to_rgb(self, value):
#         value = value.lstrip('#')
#         lv = len(value)
#         return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
#
#     def rgb_to_hex(self, rgb_str):
#         rgb_tuple = self.str_to_tuple(rgb_str)
#         return '#%02x%02x%02x' % rgb_tuple
#
#     def date_converter(self, date):
#         mm, dd, yyyy = date.split('/')
#         return f'{dd}/{mm}/{yyyy}'
#
#     def str_to_tuple(self, data):
#         list_int_numbers = []
#         list_str_numbers = data[1:-1].split(", ")
#         for number in list_str_numbers:
#             list_int_numbers.append(int(number))
#         tuple_numbers = tuple(list_int_numbers)
#         return tuple_numbers
