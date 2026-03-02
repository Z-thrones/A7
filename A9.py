maths = int(input("How much marks did you get in the maths exam or test"))
science = int(input("How much marks did you get in the science exam or test"))
english = int(input("How much marks did you get in the english exam or test"))
history = int(input("How much marks did you get in the history exam or test"))
firstsum = maths+science+english+history
secondsum = firstsum // 400
overallpercentage = secondsum * 100
print("Your overall percentage in all the subjects is " , overallpercentage)