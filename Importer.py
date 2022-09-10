import csv
from itertools import count
class parser:

    def __init__(self,htmlDataArray):
        self.htmlDataArray = htmlDataArray
        self.DimmList = []
        self.DimmHeaderList = []
        self.DimmNameList = []
        self.dimmData = []
        self.VideoAdapterList = []
        self.VideoAdapterNameList = []
        self.MonitorList = []
        self.MonitorNameList = []
        self.DiscList = []
        self.DiscNameList = []
        


    def findUserNameData(self):
        for i in range(len(self.htmlDataArray)):
            if i < 500:
                if self.htmlDataArray[i] == "UserName":  
                    return self.htmlDataArray[i]
    def findUserNameNameData(self):
        for i in range(len(self.htmlDataArray)):
            if i < 500:
                if self.htmlDataArray[i] == "UserName":  
                    return self.htmlDataArray[i+1]
    
    def findMotherboardData(self):
        for i in range(len(self.htmlDataArray)):            
            if i < 500:       
                if self.htmlDataArray[i] == "MotherboardName":
                    return self.htmlDataArray[i]
    def findMotherboardNameData(self):
        for i in range(len(self.htmlDataArray)):            
            if i < 500:       
                if self.htmlDataArray[i] == "MotherboardName":
                    return self.htmlDataArray[i+1]

    def findCPUTypeData(self):                
        for i in range(len(self.htmlDataArray)):
            if i< 500:
                if self.htmlDataArray[i] == "CPUType":
                    return self.htmlDataArray[i] 
    def findCPUNameData(self):                
        for i in range(len(self.htmlDataArray)):
            if i< 500:
                if self.htmlDataArray[i] == "CPUType":
                    return self.htmlDataArray[i+1] 

    def findCurrentPowerSourceData(self):
        for i in range(len(self.htmlDataArray)):             
            if i<5000:
                if self.htmlDataArray[i] == "CurrentPowerSource":
                    return self.htmlDataArray[i]
    def findCurrentPowerSourceName(self):
        for i in range(len(self.htmlDataArray)):             
            if i<5000:
                if self.htmlDataArray[i] == "CurrentPowerSource":
                    return self.htmlDataArray[i+1]

    def findSystemMemoryData(self): 
        for i in range(len(self.htmlDataArray)):                
            if i<600: 
                if self.htmlDataArray[i] =="SystemMemory":
                    return self.htmlDataArray[i]
    def findSystemMemoryCount(self): 
        for i in range(len(self.htmlDataArray)):                
            if i<600: 
                if self.htmlDataArray[i] =="SystemMemory":
                    return self.htmlDataArray[i+1]

    def findDIMMData(self):
        for i in range(len(self.htmlDataArray)):
            if i > 320 and i < 600:
               if "DIMM" in self.htmlDataArray[i]:
                        dataSrt = self.htmlDataArray[i]
                        dataAr = dataSrt.split(":")
                        self.DimmList.append(dataAr)

    def findDIMMNameData(self):
        for i in range(len(self.htmlDataArray)):
            if i > 320 and i < 600:
               if "DIMM" in self.htmlDataArray[i]:
                    self.DimmNameList.append(self.htmlDataArray[i + 1])

    def findVideoAdapterData(self):  
        for i in range(len(self.htmlDataArray)):
            if i<600:
                if self.htmlDataArray[i] =="VideoAdapter":
                    self.VideoAdapterList.append(self.htmlDataArray[i])
            
    def findVideoAdapterNameData(self): 
        VideoAdapterList = []          
        for i in range(len(self.htmlDataArray)):
            if i<600:
                if self.htmlDataArray[i] =="VideoAdapter":
                    self.VideoAdapterNameList.append(self.htmlDataArray[i+1])

    def findDiskDriveData(self):             
        for i in range(len(self.htmlDataArray)):
            if i<600:
                if self.htmlDataArray[i] =="DiskDrive":
                    self.DiscList.append(self.htmlDataArray[i])

    def findDiskDriveNameData(self):             
        for i in range(len(self.htmlDataArray)):
            if i<600:
                if self.htmlDataArray[i] =="DiskDrive":
                    self.DiscNameList.append(self.htmlDataArray[i+1]) 
                     

    def findMonitorData(self):             
        for i in range(len(self.htmlDataArray)):
            if i>200 and i<600:
                if self.htmlDataArray[i] =="Monitor":
                   self.MonitorList.append(self.htmlDataArray[i])

    def findMonitorNameData(self):             
        for i in range(len(self.htmlDataArray)):
            if i>200 and i<600:
                if self.htmlDataArray[i] =="Monitor":
                   self.MonitorNameList.append(self.htmlDataArray[i+1])
    
