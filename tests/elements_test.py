import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            time.sleep(5)
            assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_tesult()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            selected_label = radio_button_page.get_selected_radio_box_label()
            print(selected_label)
            assert selected_label == 'Yes'
            radio_button_page.click_on_the_radio_button('impressive')
            selected_label = radio_button_page.get_selected_radio_box_label()
            print(selected_label)
            assert selected_label == 'Impressive'
            time.sleep(2)
