import threading 

#Note len(dataDic) if 20, 20th element is length.
class Rearrange: 
    dataDic = {}   
    data = ""
    dataSplit = []
    dataSet = {}
    length = 0
    rearrageSplit = []

    def __init__(self, data):
        self.data = data 
        self.dataSplit = self.data.split(" ")
        self.dataSet = {key for key in self.dataSplit} 
        self.length = len(self.dataSplit) 
       #self.rearrageSplit = [0 for i in range(self.dataDic["length"])]
        self.rearrageSplit = [0 for i in range(self.length)]

    #Go through the split data, and see if it exsist, if not add key with values of its position in data. 
    def splitData(self, ): 
        for key in range(len(self.dataSplit)): 
            try:
                if(self.dataDic[self.dataSplit[key]]): 
                    self.dataDic[self.dataSplit[key]]["pos"].append(key)
            except: 
                self.dataDic[self.dataSplit[key]] = {"pos": [key]}
            # if(key == len(self.dataSplit) -1 ): 
            #     self.dataDic["length"] = len(self.dataSplit)




    #  create  a array of len of total number of time word exist 
    ## Without threading
    # def self.reArrangeSplit(): 
    #     for key in self.dataDic.keys(): 
    #         for p in self.dataDic[key]["pos"]: 
    #             self.rearrageSplit[p] = key

    ##With Thread
    def reArrangeSplitx(self, key): 
        for p in self.dataDic[key]["pos"]: 
            self.rearrageSplit[p] = key
    def reArrangeSplit(self,): 
        for key in self.dataDic.keys(): 
            threadX = threading.Thread(target=self.reArrangeSplitx, args=(key,))
            threadX.start()
        
    def reArrangeData(self,): 
        re_arrange =""
        for i in self.rearrageSplit: 
            re_arrange+=str(i) + " " 
        return re_arrange


    def checkIfExist(self, value): 
        tf = True if(value in self.dataSet) else self.dataSet.add(value)
        return True if(tf) else False; 




data = "After Thanos, an intergalactic warlord, disintegrates half of the universe, the Avengers must reunite and assemble again to re-invigorate their trounced allies and restore balance."
r = Rearrange(data); 
r.splitData()
r.reArrangeSplit()
print(r.reArrangeData())

