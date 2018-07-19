from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import datetime
import os
import pandas as pd
from pandas import ExcelWriter
import urllib
pd.set_option('display.max_columns', 10)

#df = pd.DataFrame(columns=['Result_ID', 'Date', 'Time', 'Ping', 'Download_Speed', 'Upload_Speed', 'Server_Name', 'Server_Place', 'Result_URL'])
df = pd.read_excel('jio_speed_test.xls')
print df

browser = webdriver.Firefox()


while True:
	try:
		browser.set_page_load_timeout(200)
		browser.get("http://www.speedtest.net/")

	except TimeoutException as ex:
		print("Exception has been thrown. " + str(ex))
		continue
	

	goClick = None
	while not goClick:
		try:
			goClick = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[1]/a/span[3]')
		except NoSuchElementException:
			time.sleep(2)

	time.sleep(2)
	goClick.click()

	j=0
	resultID = None
	while not resultID:
		if j>= 250:
			break
		try:
			resultID = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[1]/div/div[2]/div[2]/a')
			
		except NoSuchElementException:
			time.sleep(1)
			j = j + 1
	if j>= 250:
		continue 

	time.sleep(2)

	resultID = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[1]/div/div[2]/div[2]/a')
	print resultID.text

	downspeed = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/span').text
	print downspeed

	upspeed = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div[3]/div/div[2]/span').text
	print upspeed

	pingg = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div[1]/div/div[2]/span').text
	print pingg

	server_name = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[4]/div/div[3]/div/div/div[2]/a').text
	print server_name

	server_place = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[4]/div/div[3]/div/div/div[3]/span').text
	print server_place

	ts = time.time()
	stamp_date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
	stamp_time = datetime.datetime.fromtimestamp(ts).strftime('%H-%M')

	urllib.urlretrieve("http://www.speedtest.net/result/"+resultID.text+".png", "jio_speedtest_ResultID-"+resultID.text+"_"+stamp_date+"_"+stamp_time+".png")

	#df = pd.DataFrame(columns=['Result_ID', 'Date', 'Time', 'Ping', 'Download_Speed', 'Upload_Speed', 'Server_Name', 'Server_Place'])
	df = df.append({'Result_ID':resultID.text, 'Date':stamp_date, 'Time':stamp_time, 
					'Ping': pingg, 'Download_Speed': downspeed, 'Upload_Speed': upspeed, 
					'Server_Name': server_name, 'Server_Place': server_place, 
					'Result_URL': "http://www.speedtest.net/result/"+resultID.text+".png"}, ignore_index=True)
	print df

	writer = ExcelWriter('jio_speed_test.xls')
	df.to_excel(writer, 'Sheet1')
	writer.save()

	time.sleep(120)

	#browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[1]/a/span[3]").click()


