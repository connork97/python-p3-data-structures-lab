spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spiciest_list = []
    for food in spicy_foods:
        if (food["heat_level"] > 5):
            spiciest_list.append(dict(food))
    return spiciest_list

get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        food_name = food["name"]
        food_cuisine = food["cuisine"]
        food_heat_level = "🌶" * food["heat_level"]
        print(f"{food_name} ({food_cuisine}) | Heat Level: {food_heat_level}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if (food["cuisine"] == cuisine):
            print(dict(food))
            return dict(food)
    print("Cuisine not found")

get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if (food["heat_level"] > 5):
            food_name = food["name"]
            food_cuisine = food["cuisine"]
            food_heat_level = "🌶" * food["heat_level"]
            print(f"{food_name} ({food_cuisine}) | Heat Level: {food_heat_level}")

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    i = 0
    average_heat_level = 0
    for food in spicy_foods:
        average_heat_level += food["heat_level"]
        i += 1
    return average_heat_level / i

get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

create_spicy_food(spicy_foods, {"name": "test", "cuisine": "test", "heat_level": "test"})