import string
import re
import xml.etree.ElementTree as ET
from urllib import urlopen
from bs4 import BeautifulSoup

xmlfile = urlopen('burlg.xml').read()

soup = BeautifulSoup(xmlfile)
enbez = soup.findAll("enbez")

for y in enbez:
    norm = y.find_parent("norm")
    jurabk = soup.find("jurabk")
    enbezprint = y.text
    jurabkprint = " "+jurabk.text
    p = norm.findAll("p")
    
    for i in p:
        regex2 = re.compile(r'\. \w')
        sentences = regex2.split(i.text)

        if len(sentences) == 1:
            regex = re.compile('\(\d\)')
            result = regex.match(i.string)
            if result:
            # Remove the brackets
                resultstring = result.group()
                resultstring1 = resultstring.replace("(","")
                resultstring2 = resultstring1.replace(")","")
                resultstring3 = " " + resultstring2
                paraprint = " Abs."+resultstring3    
                
                appendix1 = "["+enbezprint+paraprint+jurabkprint+"]"
                i.append(appendix1)
                
            else:
                appendix2 = "["+enbezprint+jurabkprint+"]"
                i.append(appendix2)
                

        

        if len(sentences) > 1:
            regex = re.compile('\(\d\)')
            result = regex.match(i.string)

            if result:
            # Remove the brackets
                
                resultstring = result.group()
                resultstring1 = resultstring.replace("(","")
                resultstring2 = resultstring1.replace(")","")
                resultstring3 = " " + resultstring2
                paraprint = " Abs."+resultstring3    
                appendix3 = "["+enbezprint
                appendix4 = jurabkprint+"] "

                isentences = ('%s%s%s S. %d%s' % (s, appendix3,paraprint,i,appendix4) for i, s in enumerate(sentences, 1))
                i.string.replace_with(' '.join(isentences))
                
             
            else:
                appendix3 = "["+enbezprint
                appendix4 = jurabkprint+"] "
                isentences = ('%s%s S. %d%s' % (s, appendix3, i, appendix4) for i, s in enumerate(sentences, 1))
                i.string.replace_with(' '.join(isentences))
    
f = open("test.xml", "w")
hans = str(soup)
f.write(hans)
f.close()
           
             

             


