with open('recipe.txt', 'r') as file:
    cook_book = {}
    for line in file:
        dish_name = file.readline()
        number_ingrid = file.readline()
        ingrid_list = []
        for k in range(int(number_ingrid)):
            ingridient = file.readline().strip().split(' | ')
            product_info = {}
            product_info['ingredient_name'] = ingridient[0]
            product_info['quantity'] = int(ingridient[1])
            product_info['measure'] = ingridient[2]
            ingrid_list.append(product_info)
        cook_book[dish_name.strip()] = ingrid_list
    print(cook_book)
    
def get_shop_list_by_dishes(dishes, person_count):
    product_dict = {}
    for dish in dishes:
        for product_info in cook_book[dish]:
            ingredient_name = list(product_info.values())[0]
            if ingredient_name in product_dict.keys():
                product_dict[ingredient_name]['quantity'] += product_info['quantity'] * person_count
            else:
                product_info['quantity']  *= person_count
                prod_inf = {}
                product_dict[ingredient_name] = prod_inf
                prod_inf['measure'] = product_info['measure']
                prod_inf['quantity'] = product_info['quantity']
    print(product_dict)        
    
get_shop_list_by_dishes(['Омлет','Фахитос'], 10)

