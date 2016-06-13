[Function]
This script which is programmed by python2.7 is used to parse xml format contents
in any XML file. There are three modules can be used to parse XML syntax, which are
DOM, SAX and ELEMENTTREE all are in xml package. ElementTree module is used in this 
tool to deal with it. At same time, all kinds of exceptions can be dealed with in 
processing XML file.

[Example]
This tool can be used in command line with xml file as parsing object, like this:

# python ./pylibxml.py demo.xml 

When you do not specific any xml file, it will display prompt information to console
and exit program.
If the spcific file you do does not exist in currenty directory, a prompt information 
also can be display in console, which will be leaded to exit normally.