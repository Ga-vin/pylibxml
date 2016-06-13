# -*- coding: gb18030 -*-
## ------------------------------------------------------------------------------
## File name : xmlerror.py
## Function  : Define all kinds of exceptions which could be dealing in parsing
##             XML file.
## Author    : Gavin.Bai gavin_8724@163.com
## Time      : 2016.06.13
## Version   : (C)V1.0
## Modified  :
## License   : GPL
## ------------------------------------------------------------------------------

## ------------------------------------------------------------------------------
## Essential packages & modules
import os
import sys
import time

## ------------------------------------------------------------------------------
## Exceptions for this module
class XFileNotExistError(Exception):
    '''
    The file that is specified does not exist in specific directory.
    '''
    Err_Counter = 0

    def __init__(self, file_name):
        '''
        Constructor function
        '''
        super(XFileNotExistError, self).__init__()
        self.__file_name = file_name
        self.resetErrorCounter()
        self.increaseOneError()
        self.__prompt_information = "<XFileNotExistError> : %s not exist." % self.getFileName()

    def increaseOneError(self):
        '''
        Increase one error to the counter of error
        '''
        XFileNotExistError.Err_Counter += 1

    def getErrorCounter(self):
        '''
        Get current counter of error
        '''
        return XFileNotExistError.Err_Counter

    def getFileName(self):
        '''
        Get the file name which does not exist.
        '''
        return self.__file_name

    def resetErrorCounter(self):
        '''
        Reset the error counter to zero.
        '''
        XFileNotExistError.Err_Counter = 0

    def toErrorString(self):
        '''
        Get error string stored in the class object.
        '''
        return self.__prompt_information
## ------------------------------------------------------------------------------    
