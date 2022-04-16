from classes import test
import os
import sys

def readlog():
    logfile=open("logfile","r")
    line=logfile.readline()
    while line!='':
        print(line,end='')
        line=logfile.readline()
    logfile.close()
totalQNumbers=0
mainPhase=True
showRightAns=False
examMode=False
#processing command line args
for i in range(1,len(sys.argv)):
    if sys.argv[i]=="--showRightAns":
        examMode=False
        showRightAns=True
    elif sys.argv[i]=="--numberOfQuestions":
        totalQNumbers=int(sys.argv[i+1])
    elif sys.argv[i]=="--showlog":
        mainPhase=False
        readlog()
    elif sys.argv[i]=="--exam-mode":
        examMode=True
        showRightAns=False
    elif sys.argv[i]=="--help":
        mainPhase=False
        print("--help : show this\n--showlog : display logged teszts\n--showRightAns : display correct answer after incorrect or unaswered question\n--numberOfQuestions : limit the number of questions")
if mainPhase:
    alreadyLogged=False
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def enterToContinue():
        x=input("press enter to continue")

    def retakeIfNull(msg=""):
        x=""
        while (x==""):
            x=input(msg)
        return x

    def printQuestionStatusMessage(CurrentQuestionResult):      #this function returns True if the input was acceptable and False if otherwise
        if CurrentQuestionResult=='c':
            print("correct")
        elif (CurrentQuestionResult=='w' or CurrentQuestionResult=='u'):
            if CurrentQuestionResult=='w':
                print("wrong,check correct answer and/or continue")
            elif CurrentQuestionResult=='u':
                print("unanswered,check correct answer and/or continue")
        elif CurrentQuestionResult=='s':
            print("skipped")
        else:
            return False
        return True
    
    def getAnsList():
        global CurrentTest
        CurrentTest.resetNav()
        conditionsMet=True
        while conditionsMet:
            print("enter THE CORRECT answer for test number ",CurrentTest.getQPos()," ( ",CurrentTest.getNavPos()+1,"/",CurrentTest.getTestLen(),") : ",end='')
            CurrentTest.setRAns(retakeIfNull())
            conditionsMet=CurrentTest.nextPos()

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
    #setting correct answers if not exam mode
    if not examMode : getAnsList()
    else : alreadGotAnsList=False
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
        clearConsole()
        CurrentTest.resetNav()
        conditionsMet=True
        while conditionsMet:
            gotoNextQ=False
            while not gotoNextQ:
                gotoNextQ=False
                print("enter YOUR answer for test number ",CurrentTest.getQPos()," ( ",CurrentTest.getNavPos()+1,"/",CurrentTest.getTestLen(),") (", CurrentTest.getTestLen()-CurrentTest.getNavPos(),"questions left ) : ",end='')
                x=retakeIfNull()                
                if(x=='fs'):
                    conditionsMet2=True
                    while conditionsMet2:
                        CurrentTest.setUAns('s')
                        conditionsMet2=CurrentTest.nextPos()
                    conditionsMet=False
                elif x=="status":
                    if not examMode:
                        print("correct : ",CurrentTest.getCorrectNumber(),"\nwrong : ",CurrentTest.getWrongNumber(),"\nunanswered : ",CurrentTest.getUnansweredNumber(),
                        "\nskipped",CurrentTest.getSkippedNumber(),
                        "\nwrite exit to exit,redo to redo the answering,showCorrect,showWrong,showUnAns,showSkipped,showUsrAns,log,showLog")
                    else :
                        print("not available during exam mode")
                elif x=="comment":
                    CurrentTest.setComment(input("the comment : "))
                elif x=="comments":
                    CurrentTest.getComment()
                elif x=="goto":
                    if not CurrentTest.gotoQ(CurrentTest.getQPosNav(int(input("the question number : ")))):
                        print("that question seems to be nonexistant")
                else:
                    gotoNextQ=True
                    if x=="end":
                        conditionsMet=False
                    else:
                        CurrentTest.setUAns(x)

                        CurrentQuestionResult=CurrentTest.getQstat(CurrentTest.getNavPos())
                        if(not examMode):
                            printQuestionStatusMessage(CurrentQuestionResult)
                        if(not CurrentQuestionResult in ['c','w','u','s']):
                            gotoNextQ=False
                            print("error occured while checking answer")
                        if (showRightAns and CurrentQuestionResult!='c'):
                                print("the right answer is : ",CurrentTest.getRAns(CurrentTest.getNavPos()))
                        if gotoNextQ and not examMode:
                            enterToContinue()
            if (conditionsMet and (not CurrentTest.nextPos())):
                print("that was the last question")
                print("you can finish the testing phase-if you wish- by entering\"end\" command")
                print("or you can use the \"goto\" command in order to return to a question")
        # exam mode : taking answers now
        if examMode and not alreadGotAnsList : 
            getAnsList()
            alreadGotAnsList=True
        # results screen
        endCmdDone=False
        while not endCmdDone:
            print("\nresults\ncorrect : ",CurrentTest.getCorrectNumber(),"\nwrong : ",CurrentTest.getWrongNumber(),"\nunanswered : ",CurrentTest.getUnansweredNumber(),
            "\nskipped",CurrentTest.getSkippedNumber(),"\nwrite exit to exit,redo to redo the answering,showCorrect,showWrong,showUnAns,showSkipped,showUsrAns,log,showLog,showComments")
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
                    #CurrentTest.showWrongQNumbers()
                    for i in CurrentTest.getSpecificNumbers('w'):
                        print(i,"\t\tcorrect answer :",CurrentTest.getRAns(CurrentTest.getQPosNav(i)),"\t\tyour answer :",CurrentTest.getUAns(CurrentTest.getQPosNav(i)))
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
                elif endCmd=="showComments":
                    for commentsNavigator in CurrentTest.getCommentedQuestionsMap():
                        print("Question N. : ",CurrentTest.getNavQPos(commentsNavigator),"\t\tThe comment : ",CurrentTest.getComment(commentsNavigator))
                elif endCmd=="log":
                    if not alreadyLogged:
                        alreadyLogged=True
                        #saving crrent test general information
                        logfile=open('logfile','a')
                        testname=input("name of this test : ") 
                        logfile.write("test name : "+ testname + "\n" + "start : "+str(start)+"\n"+"end : " + str(end) + '\n' + "step : " + str(step) + '\n\n')
                        logfile.close()
                        print("logged")
                    else :
                        print("test is already logged")
                elif endCmd=="showLog":
                    readlog()
                elif (endCmd!="") :
                    print("error : unkknown command : ",endCmd)
