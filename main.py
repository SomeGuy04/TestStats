from classes import test
conditionsMet=False
while not conditionsMet:
    start=int(input("enter the starting question number"))
    end=int(input("enter the last question number"))
    step=int(input("enter step number"))
    if end<=start:
        print("error : incorrect numbers")
    else:
        conditionsMet=True
CurrentTest=test(start,end,step)
#setting correct answers
conditionsMet=True
while conditionsMet:
    CurrentTest.setRAns(int(input("enter THE CORRECT answer for test number ",CurrentTest.getQPos()," ( ",CurrentTest.getNavPos(),"/",CurrentTest.getTestLen(),")")))
    conditionsMet=CurrentTest.nextPos()