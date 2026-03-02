amount = int(input("Enter the money you would like to withdraw"))
note1 = amount//100
note2 = (amount%100)// 50
note3 = ((amount%100)%50)//10
print("Notes of hundred rupeese are" , note1)
print("Notes of fifty ruppeese are" , note2)
print("Notes of ten ruppeese are" , note3)
