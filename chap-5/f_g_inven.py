data ={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(data):
    key_value_list = data.keys()
    values_list = data.values()
    print('Inventory:')
    for i,j in zip(values_list,key_value_list):
        print(i,j)
    print('Total number of items: ',sum(values_list))
displayInventory(data)