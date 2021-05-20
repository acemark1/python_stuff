import threading 
import time

#Note len(dataDic) if 20, 20th element is length.
dataDic = {

}   
data = "After Thanos, an intergalactic warlord, disintegrates half of the universe, the Avengers must reunite and assemble again to reinvigorate their trounced allies and restore balance."
dataSplit = data.split(" ")
dataSet = {key for key in dataSplit}
length = len(dataSplit)
# rearrageSplit = [0 for i in range(dataDic["length"])]
rearrageSplit = [0 for i in range(length)]

#Go through the split data, and see if it exsist, if not add key with values of its position in data. 
def splitData(): 
    for key in range(len(dataSplit)): 
        try:
            if(dataDic[dataSplit[key]]): 
                dataDic[dataSplit[key]]["pos"].append(key)
        except: 
            dataDic[dataSplit[key]] = {"pos": [key]}
        # if(key == len(dataSplit) -1 ): 
        #     dataDic["length"] = len(dataSplit)




#  create  a array of len of total number of time word exist 
## Without threading
# def reArrangeSplit(): 
#     for key in dataDic.keys(): 
#         for p in dataDic[key]["pos"]: 
#             rearrageSplit[p] = key

##With Thread
def reArrangeSplitx(key): 
    for p in dataDic[key]["pos"]: 
        rearrageSplit[p] = key
def reArrangeSplit(): 
    for key in dataDic.keys(): 
        threadX = threading.Thread(target=reArrangeSplitx, args=(key,))
        threadX.start()
    
def reArrangeData(): 
    re_arrange =""
    for i in rearrageSplit: 
        re_arrange+=str(i) + " " 
    return re_arrange


def checkIfExist(value): 
    tf = True if(value in dataSet) else dataSet.add(value)
    return True if(tf) else False; 



splitData()
reArrangeSplit()
print(reArrangeData())