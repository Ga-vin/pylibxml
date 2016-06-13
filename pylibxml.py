# -*- coding: gb18030 -*-
## ------------------------------------------------------------------------------
## File name : pylibxml.py
## Function  : Parse all contents of xml file
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

try:
    from xml.etree import ElementTree as ET
except ImportError, e:
    print 'Do not find module xml.etree: %s' % e

try:
    import xmlerror
except ImportError, e:
    print 'Can not find module xmlerror in current directory: %s' % e
## ------------------------------------------------------------------------------

## ------------------------------------------------------------------------------
## Class ParseXml    
class ParseXml(object):
    '''
    The class type can parse all files which is composed with xml format.
    '''

    def __init__(self, file_name):
        '''
        Constructor function
        @file_name : the specific file to be dealing with
        '''
        self.__file_name  = file_name
        self.__root_tag   = ""
        self.__valid_flag = False
        self.__xml_obj    = None

        try:
            ## Specific file does not exists in current directory
            if not os.path.exists(os.getcwd() + "\\" + self.getFileName()):
                raise xmlerror.XFileNotExistError(self.getFileName())

            ## Create XML object
            self.__xml_obj    = ET.parse(self.getFileName())
            self.__valid_flag = True;
        except xmlerror.XFileNotExistError, e:
            print e.toErrorString()
        except ET.ParseError, e:
            print "Parse XML file error: %s" % e

    def isValid(self):
        '''
        Check whether the xml file is valid with proper format.
        @True  -- it is valid.
        @False -- it is invalid.
        '''
        if self.__xml_obj and self.__valid_flag:
            return True
        else:
            return False

    def getFileName(self):
        '''
        Get the name of file to be parsing
        @Specific xml file name
        '''
        return self.__file_name

    def getRootTag(self):
        '''
        Get the root tag of the specific xml file.
        '''
        if self.isValid():
            self.__root_tag = str(self.__xml_obj.getroot().tag)

            return self.__root_tag
        else:
            return ""

    def getDepth(self):
        '''
        Get the depth of whole xml file exclude root node.
        @-1    -- xml object is invalid
        @Depth
        '''
        pass
        ## Makesure the xml object is valid
        if self.isValid():
            pass
        else:
            return -1

    def isNUL(self):
        '''
        Check whether the contents of xml file is empty.
        '''
        return (not self.__valid_flag)

    def getAttributes(self, tag):
        '''
        Get all attributes of specific tag.
        @tag : specific tag to find its attributes
        '''
        pass
## ------------------------------------------------------------------------------    
        
## ------------------------------------------------------------------------------
## Unit test for the Class Type
def main():
    if len(sys.argv) < 2:
        print "Usage: %s xml_type_file RET" % sys.argv[0]
        sys.exit(127)

    xml_oo = ParseXml(sys.argv[1])
    root_tag = xml_oo.getRootTag()
    if root_tag:
        print 'Root Tag: %s' % root_tag
## ------------------------------------------------------------------------------

## ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
