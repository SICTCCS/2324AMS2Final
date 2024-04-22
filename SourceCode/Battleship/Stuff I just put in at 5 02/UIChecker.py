'''def printShipList(shiplist):
    out = ""
    for i in shiplist:
        if i == shiplist[len(shiplist)-1]:
            out += i
        else:
            out += (i+",")
    return out

shipsList1 =   ['P','D','S','B','C' ]
shipChoiceP1 = input("Player 1 - What ship do you want {}: ".format(printShipList(shipsList1))).upper()
'''

class UIchecker:
    status=False
    @staticmethod
    def checkInput(goodList,answer):
        #list of answers that are ok
        appropriateAnswers=goodList
        #the answer from the user
        ui=answer
        if (ui in appropriateAnswers):
            return True
