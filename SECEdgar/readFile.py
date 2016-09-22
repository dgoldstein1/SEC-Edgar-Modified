""" 
Created 9/22/2016
This program takes in a list of companies and their respective cik number
and pulls their public 10Q,10K,8K,and 13F through a specific date
written for: satvikakumar@gmail.com
"""
import time
from SECEdgar.crawler import SecCrawler

def readIn(file):
	'''this function reads in a list of companies and enters their respective
	SEC name and number into a dictionary which we will use to recurse through '''
	file = open(file, 'r').read() #open file
	companies = {} #create dictionary mapping name:number

	#import file into dictionary
	companyName = ""
	companyCode = ""
	for char in file:
		if char == "\n":
			companies[companyName] = companyCode
			companyName = ""
			companyCode = ""

		elif char.isalpha() and char!= " ": #is letter and not space
			companyName += char
		
		else:
			try: #is number
				int(char)
				companyCode += char		
			
			except ValueError:
				pass

	return companies

def pullData(companies):
	'''pulls data using web crawler'''
	t1 = time.time()

	# create object
	seccrawler = SecCrawler()

	for company in companies:
		companyCode = company 
		cik = companies[company]      # cik code for apple
		date = '20010101'       # date from which filings should be downloaded
		count = '10'            # no of filings

		seccrawler.filing_10Q(str(companyCode), str(cik), str(date), str(count))
		seccrawler.filing_10K(str(companyCode), str(cik), str(date), str(count))
		seccrawler.filing_8K(str(companyCode), str(cik), str(date), str(count))
		seccrawler.filing_13F(str(companyCode), str(cik), str(date), str(count))

	t2 = time.time()
	print ("Total Time taken: "),
	print (t2-t1)


def processData(names):
	'''processes and interprets data '''
	#TODO: Recurse through file folders

	#TODO: Process actual data
	
	pass

if __name__ == "__main__": #run from console
	companies = readIn("companylist.txt")
	pullData(companies)

