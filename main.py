product_dict = {"apple": ["25", "300"],
                "orange": ["47", "560"],
                "tomato": ["34", "710"],
                "berries": ["61", "240"],
                "cucumber": ["18", "830"]
                }
for k, v in product_dict.items():
    print(k, "-", "цена", product_dict[k][0], "-", "количество", product_dict[k][1])

    a = input("Введите название товара:")
    b = int(input("Введите количетво товара:"))
    if a in product_dict and b <= int(product_dict[k][1]):
        print(int(product_dict[k][0])*b, int(product_dict[k][1])-b)
