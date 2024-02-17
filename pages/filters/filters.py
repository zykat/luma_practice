from base.seleniumbase import BasePage
from locators.filters_locators import FiltersLocators
from locators.sort_items_locators import SortItemsLocators


class FiltersCheck(BasePage):
    def select_size(self):
        return self.is_clickable(FiltersLocators.SELECT_SIZE)

    def select_price(self):
        return self.is_clickable(FiltersLocators.SELECT_PRICE)

    def select_material(self):
        return self.is_clickable(FiltersLocators.SELECT_MATERIAL)

    def size_m(self):
        return self.is_clickable(FiltersLocators.SIZE_M)

    def price_20_30(self):
        return self.is_clickable(FiltersLocators.PRICE_20_30)

    def material_polyester(self):
        return self.is_clickable(FiltersLocators.MATERIAL_POLYESTER)

    def paging_button_next(self):
        return self.is_clickable(SortItemsLocators.PAGING_BUTTON_NEXT)

    def paging_button_next_visible(self):
        return bool(self.item_count(SortItemsLocators.PAGING_BUTTON_NEXT))

    def price_items(self):
        return self.is_visible_all_elements(SortItemsLocators.PRICE_ITEMS)

    def size_items(self):
        return self.is_visible_all_elements(FiltersLocators.SIZE)

    def items_with_filter(self):
        return self.is_visible_all_elements(FiltersLocators.ITEMS_MEN_TOPS_WITH_FILTER)

    def select_performance_fabric(self):
        return self.is_clickable(FiltersLocators.SELECT_PERFORMANCE_FABRIC)

    def performance_fabric_yes(self):
        return self.is_clickable(FiltersLocators.SELECT_PERFORMANCE_FABRIC_YES)

    def select_climate(self):
        return self.is_clickable(FiltersLocators.SELECT_CLIMATE)

    def select_climate_rainy(self):
        return self.is_clickable(FiltersLocators.SELECT_CLIMATE_RAINY)

    def name_items(self):
        return self.is_visible_all_elements(SortItemsLocators.NAME_ITEMS)


class FilterItemPage(BasePage):
    def tab_more_information(self):
        return self.is_clickable(FiltersLocators.TAB_MORE_INFORMATION)

    def material_polyester_more_information(self):
        return self.is_visible(FiltersLocators.MATERIAL_POLYESTER_MORE_INFORMATION)

    def climate_more_information(self):
        return self.is_visible(FiltersLocators.CLIMATE_MORE_INFORMATION)


class FilterPerformancePage(BasePage):
    URL = "https://magento.softwaretestingboard.com/collections/performance-fabrics.html"

    def get_items(self):
        names = []
        while self.paging_button_next_visible():
            for item in self.name_items():
                names.append(item.text)
            self.paging_button_next().click()
        for item in self.name_items():
            names.append(item.text)
        return names

    def paging_button_next_visible(self):
        return bool(self.item_count(SortItemsLocators.PAGING_BUTTON_NEXT))

    def name_items(self):
        return self.is_visible_all_elements(SortItemsLocators.NAME_ITEMS)

    def paging_button_next(self):
        return self.is_clickable(SortItemsLocators.PAGING_BUTTON_NEXT)

