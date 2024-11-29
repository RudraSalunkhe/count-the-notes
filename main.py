amount = int(input("please enter the amount : "))
note_1=(amount//100)
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("note of rupees 100",note_1)
print("note of rupees 50",note_2)
print("notr of rupees 10",note_3)
