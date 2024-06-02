from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
from model.config import *

class NutritionScraper:
    def __get_query(self, dish):
        return f'calories of {dish} tarla dalal'

    def __format_into_dict(
        self, calories, nutrient_name,
        nutrient_value_per_serving, nutrient_daily_value
    ):
        all_nutritions_dict = {}
        all_nutritions_dict['Calories'] = calories
        for idx, nutrient in enumerate(nutrient_name):
            all_nutritions_dict[nutrient] = {}
            all_nutritions_dict[nutrient]['Value Per Serving'] = nutrient_value_per_serving[idx]
            all_nutritions_dict[nutrient]['% Daily Values'] = nutrient_daily_value[idx]
        return all_nutritions_dict

    def __parse_page(self, page):
        calories = re.search(r"\d+ calories", page).group(0)
        soup = BeautifulSoup(page, 'html.parser')
        nutrition_table = soup.find_all('table', {'id': 'rcpnutrients'})
        if nutrition_table and len(nutrition_table) > 0:
            self.__search = False
            rows = nutrition_table[0].find_all('tr')[1:]
            nutrient_name = []
            nutrient_value_per_serving = []
            nutrient_daily_value = []
            for row in rows:
                cols = row.find_all('td')
                if len(cols) != 3:
                    continue
                nutrient_name.append(cols[0].text)
                nutrient_value_per_serving.append(cols[1].text)
                nutrient_daily_value.append(cols[2].text)

        return self.__format_into_dict(
            calories,
            nutrient_name,
            nutrient_value_per_serving,
            nutrient_daily_value
        )

    def get_nutrition(self, dish=None):
        self.__search = True
        if dish:
            query = self.__get_query(dish)
            print('Query build:', query)
            for url in search(query, tld="co.in", stop=LINKS_TO_VISIT, pause=DELAY):
                try:
                    print('Scraping url:', url)
                    page = requests.get(url).text
                    all_nutritions_dict = self.__parse_page(page)
                    if not self.__search:
                        return all_nutritions_dict
                except:
                    print('Some error occured in', url, "continuing search")
                    continue