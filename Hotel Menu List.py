MENU={1:"POROTTA", 2:"MEALS", 3:"BIRIYANI", 4:"JUICE"} #menu list
print(MENU)

choice=int(input("Enter your choice"))  #selecing required item

if choice<=0 or choice>=4:
    print("Your Choise is wrong")
else:
    print("Your selected item:",MENU[choice] )  #selecting the item if selected between1-4
