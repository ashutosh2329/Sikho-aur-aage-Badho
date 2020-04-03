old_list=['a,s,d,h,y,t,g,g,h']
new_list=[]
for elements in old_list:
    if elements not in old_list:
        new_list+=old_list[elements]

print(new_list)
print(old_list)
