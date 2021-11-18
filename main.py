from classes import test

def enterToContinue():
    x=input("enter anything to continue")

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
    print("enter THE CORRECT answer for test number ",CurrentTest.getQPos()," ( ",CurrentTest.getNavPos()+1,"/",CurrentTest.getTestLen(),") : ")
    CurrentTest.setRAns(input())
    conditionsMet=CurrentTest.nextPos()
#entering the testing phase
done=False
while not done:
    CurrentTest.resetNav()
    print(CurrentTest.rlist)
    conditionsMet=True
    while conditionsMet:
        print("enter YOUR answer for test number ",CurrentTest.getQPos()," ( ",CurrentTest.getNavPos()+1,"/",CurrentTest.getTestLen(),") : ")
        CurrentTest.setUAns(input())

        CurrentQuestionResult=CurrentTest.getQstat(CurrentTest.getNavPos())
        print(CurrentQuestionResult)
        if CurrentQuestionResult=='c':
            print("correct")
        elif CurrentQuestionResult=='w':
            print("wrong,check correct answer and/or continue")
        elif CurrentQuestionResult=='u':
            print("unanswered,check correct answer and/or continue")
        elif CurrentQuestionResult=='s':
            print("skipped")
        else:
            print("error occured while checking answered")
        enterToContinue()
        conditionsMet=CurrentTest.nextPos()
    # results screen
    endCmdDone=False
    while not endCmdDone:
        print("results\ncorrect : ",CurrentTest.getCorrectNumber(),"\nwrong : ",CurrentTest.getWrongNumber(),"\nunanswered : ",CurrentTest.getUnansweredNumber(),
        "\nskipped",CurrentTest.getSkippedNumber(),"\nwrite exit to exit,redo to redo the answering,showCorrect,showWrong,showUnAns,showSkipped")
        endCmd=input()
        if endCmd=="exit":
            done=True
            endCmdDone=True
        elif endCmd=="redo":
            endCmdDone=True
            done=False
        else:
            endCmdDone=False
            if endCmd=="showCorrect":
                CurrentTest.showCorrectQNumbers()
            elif endCmd=="showWrong":
                CurrentTest.showWrongQNumbers()
            elif endCmd=="showUnAns":
                CurrentTest.showUnansweredQNumbers()
            elif endCmd=="showSkipped":
                CurrentTest.showSkippedQNumbers()