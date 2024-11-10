def append_item(item, item_list):
    item_list.append(item)
    print(item_list)
    return item_list

item_list=[]
for i in range (1,6):
 new_item=input("enter the new item:")
 append_item(new_item, item_list)