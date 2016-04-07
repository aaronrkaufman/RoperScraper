# Version 9/25/2014

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import itertools
import csv
import sys

year = sys.argv[1]

start = "1/1/%s" % (year)
stop = "12/31/%s" % (year)

driver = webdriver.Chrome(executable_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("http://www.ropercenter.uconn.edu/CFIDE/cf/action/ipoll/")

#credentials
driver.find_element_by_xpath('''//*[@id="username"]''').send_keys(YOURNAMEHERE)
driver.find_element_by_xpath('''//*[@id="password"]''').send_keys(YOURPASS)
driver.find_element_by_xpath('''//*[@id="signin"]''').click() 

#search
driver.find_element_by_xpath('''//*[@id="fromDate2"]''').send_keys('%s' % (start))
driver.find_element_by_xpath('''//*[@id="toDate2"]''').send_keys('%s'% (stop)) 
driver.find_element_by_xpath('''//*[@id="submit"]''').click()
numpages = driver.find_element_by_xpath('''//div[1]/div/span''')
n = numpages.text
nn = int(n.split(" ")[0])
np = round(nn/20)
# There are 19831 pages when I look for everything from 1994 to 2014
q = []
s = []

print(np)



#for i in range(1,3):
for i in range(0,np):
	qs = driver.find_elements_by_xpath('''//div[1]/label''')
	qs = qs[:20]
	qs2 = [x.text for x in qs]
	source = driver.find_elements_by_xpath('''//*[@class="searchResultOut"]/div[2]''') #this isnt finding it precisely enough
	source = source[:20]
	source2 = [x.text for x in source]
	#print(qs2)
	#print(source2)
	#print(len(source2))
	q.append(qs2)
	s.append(source2)
	try:
		driver.find_element_by_xpath('''//*[@id="bd"]/div[7]/div[2]/span[15]''').click()
	except:
		break
	time.sleep(0.5)

q = sum(q,[])
s = sum(s,[])
with open('roper_%s.csv' % (year), 'w', newline='') as f:
    writer = csv.writer(f, delimiter = ',')
    for i in range(0, len(q)):
    	try:
    		print(";".join([q[i], s[i]]))
    		writer.writerow([" ; ".join([q[i], s[i]])])
    	except:
    		continue

   #I'm really close. Basically there.