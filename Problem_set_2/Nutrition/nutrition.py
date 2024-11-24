fruits = {"apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60,
          "Grapes": 90, 'honeydew melon': 50, 'kiwifruit': 90, 'lemon': 15, "lime": 20,
          'nectarine': 60, 'orange': 80, 'peach': 60, 'pear': 100, 'pineapple': 50,
          'plums': 70, 'strawberries': 50, 'sweet cherries': 100, 'Tangerine': 50, 'watermelon': 80
          }

def main():
    # takes user input
    chosen_fruit = input("Item: ")
    # finds the calorie of the input
    for key,value in fruits.items():
        if key == chosen_fruit.lower():
            print(f'calories: {value}')


if __name__ == "__main__":
    main()
