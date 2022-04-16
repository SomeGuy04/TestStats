class test:
    def __init__(self,start=1,end=2,step=1):
        self.navigator=0
        self.start=start
        self.end=end+1  #for making the last question availale in test
        self.step=step
        self.qpos=start
        self.qmap=range(start,end+1,step)
        self.testlen=len(self.qmap)
        self.rlist=self.testlen*[0]
        self.ulist=self.testlen*[0]
        self.comments=self.testlen*['']
    def getNavPos(self):
        return self.navigator
    def resetNav(self): #reset navigator
        self.qpos=self.start
        self.navigator=0
    def islast(self):                           #check if navigator is in last possible position
        return self.navigator==self.testlen-1  
    def isFirst(self):                          #check if navigator is in first possible position
        return self.navigator==0 
    def nextPos(self):  #goto next pos . return value true means changed position and return value false means unable to change position
        if not self.islast():
            self.navigator+=1
            self.qpos+=self.step
            return True
        return False
    def prevPos(self):  #goto previous pos . return value true means changed position and return value false means unable to change position
        if not self.isFirst():
            self.navigator-=1
            self.qpos-=self.step
            return True
        return False
    def gotoQ(self,Qnumber):                            #goto the question,navigator dependent for ease of coding
        if Qnumber>=0 and Qnumber<self.testlen:
            self.navigator=Qnumber
            self.qpos=self.getNavQPos()
            return True
        return False
    def getQPosNav(self,n=None):                        #return navigator value of a question with a specified Qpos value(may have buggy behavior)
        if n==None:
            n=self.qpos
        return (n-self.start)//self.step    
    def getNavQPos(self,n=None):                        #inverse function of the above.will return qpos instead
        if n==None:
            n=self.navigator
        return(self.start + n*self.step)    
    def setRAns(self,val):  #set the right answer for question 
        self.rlist[self.navigator]=val
    def setUAns(self,val):  #set users answer for question 
        self.ulist[self.navigator]=val
    def getRAns(self,n=None):             #get the right answer for question 
        if n==None:
            n=navigator
        return self.rlist[n]   
    def getUAns(self,n=None):          #get users answer for question 
        if n==None:
            n=navigator
        return self.ulist[n]  
    def getQPos(self):return self.qpos      #return accual number of the current question
    def getTestLen(self):return self.testlen   #return length of test
    def getQstat(self,position):     #return current question stats. c for correct , w for wrong , u for unanswered , s for skipped  and e for error
        if(self.ulist[position]!='' and self.rlist[position]!=''):
            if (self.ulist[position]=='0'):
                return 'u'
            elif self.ulist[position]=='s':
                return 's'
            elif self.ulist[position]==self.rlist[position]:
                return 'c'
            else:
                return 'w'
        else:
            return 'e'
    def getSpecificNumber(self,x):  #function will be used in next functions
        rval=0
        for i in range(self.testlen):
            if(self.getQstat(i)==x):
                rval+=1
        return rval
    def getCorrectNumber(self):return self.getSpecificNumber('c') #returns number of test with correct answers
    def getWrongNumber(self):return self.getSpecificNumber('w')   #return total number of wrongly answered questions
    def getUnansweredNumber(self):return self.getSpecificNumber('u')  #return total number of unaswered questions
    def getSkippedNumber(self):return self.getSpecificNumber('s')     #return total number of skipped questions
    def getSpecificNumbers(self,x):                             #will return the number of wanted questions as a list
        rval=0*[0]
        pos=0
        for i in self.qmap:
            if(self.getQstat(pos)==x):
                rval+=[i]
            pos+=1
        return rval
    def showSpecificQNumbers(self,x): #function will be used in next functions
        pos=0
        for i in self.qmap:
            if(self.getQstat(pos)==x):
                print(i)
            pos+=1
    def showCorrectQNumbers(self):  #print correctly answered question numbers
        self.showSpecificQNumbers('c')
    def showWrongQNumbers(self):    #print wrongly answered question numbers
        self.showSpecificQNumbers('w')
    def showUnansweredQNumbers(self):   #print unanswered question numbers
        self.showSpecificQNumbers('u')
    def showSkippedQNumbers(self):  #print skipped question numbers
        self.showSpecificQNumbers('s')
    def setComment(self,cmnt,n=None) :     #used for setting comments on a question(current question by default)
        if n==None:
            n=self.navigator
        self.comments[n]=cmnt
    def getComment(self,n=None):           #return the user's comment
        if n==None:
            n=self.navigator
        return self.comments[n]
    def getCommentedQuestionsMap(self):
        rlist=0*[0]
        for i in range(self.testlen):
            if self.comments[i]!='':
                rlist+=[i]
        return rlist