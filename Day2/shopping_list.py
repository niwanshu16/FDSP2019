# Accepting items in comma separated string
shopping_list1 = []
print('Enter all the items you want to purchase ')
item = input()
shopping_list1 = item.split(',')

# Exception if there is any number in a name of item
for i in range(len(shopping_list1)):
    if not shopping_list1[i].isalpha():
        print("Enter this {} item again ".format(shopping_list1[i]))
        d=input()
        shopping_list1.remove(shopping_list1[i])
        shopping_list1.insert(i,d)


# Add at specific index
print('Enter the index where you want to add item and item name comma separated')
a=input()
a,b=a.split(',')

# Exception if the index is too large
if int(a)>len(shopping_list1):
    print("Index can't be greater than length of list , Enter index again ")
    a = int(input())
shopping_list1.insert(int(a),b)


# Remove the items from a list
print('Item you want to remove')
c = input()

# Exception if item is not in list
if c not in shopping_list1:
    print('Item not in list , Enter again ')
    c = input()
shopping_list1.remove(c)



# Print the list
print(shopping_list1)

with open('mylist.txt','w') as f:
    for item in shopping_list1:
        f.write("%s\n" % item)
          
          
          
