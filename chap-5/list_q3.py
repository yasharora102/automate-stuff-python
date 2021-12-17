def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i not in inventory:
           inventory[i]=0
        inventory[i]+=1  
    return inventory

def displayInventory(data):
    key_value_list = data.keys()
    values_list = data.values()
    print('Inventory:')
    for i,j in zip(values_list,key_value_list):
        print(i,j)
    print('Total number of items: ',sum(values_list))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)