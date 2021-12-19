import pyinputplus as pyip
import yaml
item_list ={'bread':['wheat:10','white:10','soudough:5']
,'protein':["chicken:10",'turkey:15','ham:10','tofu:8'],
'cheese(optional)':['cheddar:3', 'Swiss:5','mozzarella:2']
,'sides':['mayo, mustard, lettuce, tomato:5']}
cheese=''

flag_sides = False
sides = ''
bread_list = [10,10,5]
protein_list = [10,15,10,8]
cheese_list=[3,5,2]
Total_price = 0

#Printing Menu
print()
print('\t\t\tMenu')
print()
print(yaml.dump(item_list, default_flow_style=False,sort_keys=False))

#Taking inputs
print('Choice of bread:')
bread = pyip.inputMenu(['wheat','white','sourdough']).lower()
print()
print('Choice of protein:')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham','tofu']).lower()
print()
print("Cheese (y/n)?:")
reply = pyip.inputYesNo().lower()
if reply=='yes' or reply=='y':
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella']).lower()
    
print()
print('Sides (mayo, mustard, lettuce, tomato) (y/n)?')
reply2 = pyip.inputYesNo().lower()
if reply2 =='yes' or reply=='y':
      flag_sides = True     
      sides = 'sides'    

#Calculating output
# for bread
if bread == 'wheat':
    Total_price+=bread_list[0]
elif bread == 'white':
    Total_price+=bread_list[1]
elif bread=='sourdough':
    Total_price+=bread_list[2]

#for protein
if protein  == 'chicken':
    Total_price += protein_list[0]
elif protein  == 'turkey':
    Total_price += protein_list[1]
elif protein == 'ham':
    Total_price += protein_list[2]
elif protein == 'tofu':
    Total_price += protein_list[3]

#for cheese
if cheese == 'cheddar':
    Total_price+=cheese_list[0]
elif cheese == 'swiss':
    Total_price+=cheese_list[1]
elif cheese == 'mozzarella':
    Total_price+=cheese_list[2]
else:
    Total_price+=0

#for sides
if flag_sides:
    Total_price+=5

print()
print('Final Order: ',bread,protein,cheese,sides)
print('Cost of one sandwich: ',Total_price)
print()
n = pyip.inputInt("No. of sandwiches required: ",min = 1)
final_price = Total_price * n

print("Final cost : ",final_price)