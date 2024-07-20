import Data
import pytest
from bs4 import BeautifulSoup
from typing import List


class Kitchenware:
    def __init__(self, name: str):
        self.name = name


class FoodLabel:
    def __init__(self, name: str):
        self.name = name


class Beverage:
    def __init__(self, name: str, price: float, labels: List[FoodLabel], way: str):
        self.name = name
        self.price = price
        self.labels = labels
        self.way = way


class FoodIngredients:
    def __init__(self, name: str, labels: List[FoodLabel]):
        """
        :param name:
        :param labels:
        """
        self.name = name
        self.labels = labels


class Dish:
    def __init__(self, name: str, source: str, kitchenware: Kitchenware, price: float,
                 food_ingredients: List[FoodIngredients], positive_characteristics: List[FoodLabel],
                     negative_characteristics: List[FoodLabel], cooking_time: float, level: int, cooking_method: str):
        """
        :param name: 菜品名称
        :param source:  菜品来源
        :param kitchenware:  烹饪的工具
        :param price: 价钱
        :param food_ingredients: 食材
        :param positive_characteristics: 正面特性
        :param negative_characteristics: 负面特称
        :param cooking_time: 烹饪时间
        :param level: 烹饪等级
        :param cooking_method: 获得方式
        """
        self.name = name
        self.source = source
        self.kitchenware = kitchenware
        self.price = price
        self.food_ingredients = food_ingredients
        self.positive_characteristics = positive_characteristics
        self.negative_characteristics = negative_characteristics
        self.cooking_time = cooking_time
        self.level = level
        self.cooking_method = cooking_method


def test_data():
    print(Data.getData())


def test_get_tag_data():
    data = Data.getData();
    soup = BeautifulSoup(data, 'html.parser')
    rows = soup.find_all('tr')
    sixth_column_data = []
    for row in rows:
        # 找到当前行的所有列<td>或<th>元素
        columns = row.find_all(['td', 'th'])
        # 如果当前行有至少六列，就获取第六列的数据
        if len(columns) >= 6:
            sixth_column_data.append(columns[5].text.strip())  # 保存第六列的文本内容
    print(sixth_column_data)
    total_data = []
    for str in sixth_column_data:
        split_list = str.split('、')
        total_data += split_list

from bs4 import BeautifulSoup
import json

def test_get_dish_data():
    data = Data.getData()
    soup = BeautifulSoup(data, 'lxml')
    # 找到所有的<tr>标签
    rows = soup.find_all('tr')

    # 初始化一个列表来存储所有的菜品数据
    recipes = []

    # 遍历每一行数据

    # 遍历所有的<tr>标签
    for row in rows:
        # 找到当前行的所有<td>标签
        cols = row.find_all('td')

        # 由于第一个<td>是菜品名称，我们从第二个<td>开始提取数据
        data = [tag.text.strip() for tag in cols[1:]]

        # 将时间转换为整数数组
        # 看data[6]是否可以转为整数，如果可以讲data[6]转为整数，不可以则返回空列表
        cooking_time = []
        try:
            cooking_time = list(map(int, [data[6],data[7]]));
        except:
            pass

        # 将食材和特性转换为列表
        food_ingredients = data[3].split('、')
        positive_characteristics = data[4].split('、')
        negative_characteristics = data[5].split('、') if data[5] else []

        if cols[0].text.strip() == '樱落雪' or cols[0].text.strip() == '松子糕':
            continue
        # 构建菜品字典
        recipe = {
            "name": cols[0].text.strip(),
            "source": data[0],
            "kitchenware": data[1],
            "price": int(data[2]),
            "food_ingredients": food_ingredients,
            "positive_characteristics": positive_characteristics,
            "negative_characteristics": negative_characteristics,
            "cooking_time": cooking_time,
            "level": int(data[8]),
            "cooking_method": data[9]
        }

        # 将菜品字典添加到列表中
        recipes.append(recipe)
    # 将列表转换为JSON格式
    json_data = json.dumps(recipes, ensure_ascii=False, indent=2)

    print(json_data)
    # 保存json文件
    with open('DishBook.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

def testdata():
    print("hello world")
