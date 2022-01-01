from classes import test
import sys

showRightAns=False
totalQNumbers=0
mainPhase=True
#processing command line args
for i in range(1,len(sys.argv)):
    if sys.argv[i]=="--showRightAns":
        showRightAns=True
    elif sys.argv[i]=="--numberOfQuestions":
        totalQNumbers=int(sys.argv[i+1])
    elif sys.argv[i]=="--showlog":
        mainPhase=False
        logfile=open("logfile","r")
        line=logfile.readline()
        while line!='':
            print(line,end='')
            line=logfile.readline()
if mainPhase:  
    def enterToContinue():
        x=input("enter anything to continue")

    def retakeIfNull(msg=""):
        x=""
        while (x==""):
            x=input(msg)
        return x

    conditionsMet=False
    while not conditionsMet:
        start=int(input("enter the starting question number : "))
        end=int(input("enter the last question number : "))
        if totalQNumbers==0:
            step=int(input("enter step number : "))
        if end<=start:
            print("error : incorrect numbers")
        else:
            conditionsMet=True
    if(totalQNumbers!=0):
        step=(end-start)//(totalQNumbers-1)
        print("step is ",step)
        end=start+(totalQNumbers-1)*step

    CurrentTest=test(start,end,step)
    #setting correct answers
    conditionsMet=True
    while conditionsMet:
        print("enter THE CORRECT answer for test number ",CurrentTest.getQPos()," ( ",CurrentTest.getNavPos()+1,"/",CurrentTest.getTestLen(),") : ",end='')
        CurrentTest.setRAns(retakeIfNull())
        conditionsMet=CurrentTest.nextPos()
    #making sure user is not zoned out while entering answers
    conditionsMet=False
    while not conditionsMet:
        if input("type \'begin\' to begin : ")=="begin":
            conditionsMet=True
        else:
            print("i guess you're zoned out and didnt even read this")
    #entering the testing phase
    done=False
    while not done:
        CurrentTest.resetNav()
        conditionsMet=True
        while conditionsMet:
            print("enter YOUR answer for test number ",CurrentTest.getQPos()," ( ",CurrentTest.getNavPos()+1,"/",CurrentTest.getTestLen(),") : ",end='')
            x=retakeIfNull()
            if(x=='fs'):
                conditionsMet2=True
                while conditionsMet2:
                    CurrentTest.setUAns('s')
                    conditionsMet2=CurrentTest.nextPos()
            else:
                CurrentTest.setUAns(x)

                CurrentQuestionResult=CurrentTest.getQstat(CurrentTest.getNavPos())
                if CurrentQuestionResult=='c':
                    print("correct")
                elif (CurrentQuestionResult=='w' or CurrentQuestionResult=='u'):
                    if CurrentQuestionResult=='w':
                        print("wrong,check correct answer and/or continue")
                    elif CurrentQuestionResult=='u':
                        print("unanswered,check correct answer and/or continue")
                    if (showRightAns):
                        print("the right answer is : ",CurrentTest.getRAns(CurrentTest.getNavPos()))
                elif CurrentQuestionResult=='s':
                    print("skipped")
                else:
                    print("error occured while checking answer")
                enterToContinue()

            conditionsMet=CurrentTest.nextPos() 
        # results screen
        endCmdDone=False
        while not endCmdDone:
            print("results\ncorrect : ",CurrentTest.getCorrectNumber(),"\nwrong : ",CurrentTest.getWrongNumber(),"\nunanswered : ",CurrentTest.getUnansweredNumber(),
            "\nskipped",CurrentTest.getSkippedNumber(),"\nwrite exit to exit,redo to redo the answering,showCorrect,showWrong,showUnAns,showSkipped,showUsrAns,log")
            endCmd=input()
            endCmdDone=True
            if endCmd=="exit":
                done=True
            elif endCmd=="redo":
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
                elif endCmd=="showUsrAns":
                    j=0
                    for i in range(start,end+1,step):
                        print(i,':',end='')
                        x=CurrentTest.getUAns(j)
                        if(x=='s'):
                            print("skipped")
                        elif(x=='0'):
                            print("unanswered")
                        else:
                            print(x)
                        j+=1
                elif endCmd=="log":
                    #saving crrent test general information
                    logfile=open('logfile','a')
                    testname=input("name of this test : ") 
                    logfile.write("test name : "+ testname + "\n" + "start : "+str(start)+"\n"+"end : " + str(end) + '\n')
                    logfile.close()
                    print("logged")