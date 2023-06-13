import SnakeLadder2 as sl
#O(100) Constant
def boardp2():
    for i in range (100,0,-1):
        if sl.dict1[i] == "P2":
            sl.dict1[i] = str(i)
        elif sl.dict1[i] == "P1":
            sl.dict1[i] = "P1"
        elif sl.dict1[i] == "P1 , P2":
            sl.dict1[i] = "P1"
        elif sl.dict1[i] == "P2":
            sl.dict1[i] = "P2"
        elif sl.dict1[i] == "P1 , P2":
            sl.dict1[i] = "P2"
        elif (i == 8):
            sl.dict1[i] = str("L1S") #+ " "+str(i)
        elif (i == 59):
            sl.dict1[i] = str("L2S")#+ " "+str(i)
        elif (i == 75):
            sl.dict1[i] = str("L3S")#+ " "+str(i)
        elif (i == 91):
            sl.dict1[i] = str("S1H")#+ " "+str(i)
        elif (i == 78):
            sl.dict1[i] = str("S2H")#+ " "+str(i)
        elif (i == 36):
            sl.dict1[i] = str("S3H")#+ " "+str(i)
        elif (i == 40):
            sl.dict1[i] = str("S4H")#+ " "+str(i)
        elif (i == 32):
            sl.dict1[i] = str("L1E")
        elif ( i== 99):
            sl.dict1[i] = str("L2E")
        elif (i == 97):
            sl.dict1[i] = str("L3E")
        elif (i == 54):
            sl.dict1[i] = str("S1T")
        elif (i == 55):
            sl.dict1[i] = str("S2T")
        elif (i == 25):
            sl.dict1[i] = str("S3T")
        elif (i ==19):
            sl.dict1[i] = str("S4T")
        else:
            sl.dict1[i] = str(i)
    return("\t | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t | % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s  | %s  | %s  | %s | %s  | %s  | %s  | %s  | %s  | \n\t---------------------------------------------------\n\t " % tuple(dict1.values()))
