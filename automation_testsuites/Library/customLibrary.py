from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from datetime import date
import re
import os
import random
from operator import contains
from itertools import imap, repeat
import calendar
import csv
import math
import decimal
import xlrd
from robot.libraries.OperatingSystem import OperatingSystem

class customLibrary:
    
    def __init__(self):
        pass

    def get_space_free_string(self, string):
        """Returns The string after replacing blanck spaces with empty string' """
        return string.replace(" ","")

    def string_should_contain(self,string,substring):
        """Returns True if The string contains substring else False' """
        ind=string.lower().find(substring.lower())
        if ind>=0:
            return True
        return False
    def StringContainSubstring(self,string,substring):
        """Returns True if The string contains substring else False' """
        ind=string.lower().find(substring.lower())
        if ind>=0:
            return True
        return False

    def validate_two_list_values_by_reverse_index(self,list1,list2):
        """Verify the sorting order of list values with another list in reverse order"""
        keywordStatus=True
        errormsg=''
        if not(len(list1)==len(list2)):
            raise AssertionError('The two list lengths are not same:'+str(len(list1))+'!='+str(len(list2)))
        for index in range(0,len(list1)):
            val1=list1[index].lower()
            val2=list2[len(list2)-int(index)-1].lower()
            if val1!=val2:
                try:
                    keywordStatus=False
                    raise AssertionError('The two list values are not same:'+str(val1)+'!='+str(val2))
                except:
                    errormsg=errormsg+('List 1 Index '+str(index)+' Value and  List 2 Index  '+str(len(list2)-int(index)-1)+' Value '+str(val1)+' != '+str(val2)+'\n')
        if keywordStatus==False:
            raise AssertionError('Lists are not in reverse order :'+'\n'+errormsg)
