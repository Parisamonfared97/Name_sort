#برنامه ای که تا وقتی کاربر exit وارد نکرده اسم دریافت کند
#در یک لیست قرار دهد

#اسامی بیش از 5 حرف
#اسامی کمتر از 5 حرف

name_list=[]

while True:
    name=input("Please enter your name:")
    if name.lower()=="exit":
        break
    else:
        name_list.append(name)

name_list.sort(key=lambda x:len(x))
less_than_5=list(filter(lambda x:len(x)<5,name_list))
greater_or_equal_5=list(filter(lambda x:len(x)>=5,name_list))

print("Less Than 5: ")
print(less_than_5)
print("Greater Or Equal: ")
print(greater_or_equal_5)
