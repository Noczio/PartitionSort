# -*- coding: utf-8 -*-
#region Imports
import json 
#endregion Imports

#region General Methods
def Swap_Data(first_value,second_value): 
    first_value,second_value=second_value,first_value
    return first_value, second_value
#endregion General Methods

#region Class Quick_Sort
class Quick_Sort():
#region Sorting methods
    def Sort_Method(self, lst:list, lowest: int, highest: int):
        if lowest < highest:            
            pivot_indx = self.Partition_Method(lst,lowest,highest)              
            self.Sort_Method(lst, lowest, pivot_indx-1) 
            self.Sort_Method(lst, pivot_indx+1, highest)
        return lst

    def Get_Pivot(self, lst:list, lowest: int, highest: int):        
        middle=(highest+lowest)//2
        pivot=highest
        if(lst[lowest][1]<lst[middle][1]):
            if(lst[middle][1]<lst[highest][1]):
                pivot=middle
        elif(lst[lowest][1]<lst[highest][1]):
            pivot=lowest
        return pivot
    
    def Partition_Method(self, lst:list, lowest: int, highest: int):
        pivot_indx=self.Get_Pivot(lst,lowest,highest)
        pivot_data=lst[pivot_indx][1]    
        #swap datas
        lst[pivot_indx],lst[lowest]=Swap_Data(lst[pivot_indx],lst[lowest])

        border=lowest # left border indx
        for i in range(lowest,highest+1):
            if(lst[i][1]<pivot_data):
                border+=1
                #swap datas
                lst[i],lst[border]=Swap_Data(lst[i],lst[border])
        #swap datas once the for statement is over
        lst[lowest],lst[border]=Swap_Data(lst[lowest],lst[border])
        # return pivot indx
        pivot_indx=border        
        return pivot_indx 
#endregion Sorting methods
   
    # constructor
    def __init__(self,lst:list):     
        self.data = lst    
    # getting the list 
    @property   
    def data(self):        
        return self._data          
    # sorting the list 
    @data.setter
    def data(self, lst:list):     
        self._data=self.Sort_Method(lst,0,len(lst)-1)                           
    # deleting the list
    @data.deleter
    def data(self):        
        del self._data                           
#endregion Class Quick_Sort  