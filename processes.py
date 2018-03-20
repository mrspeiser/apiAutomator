import api
import datetime
import requests
import sys

all_Processes = [];

class Processes(api.Api):
	"""docstring for Birthdays"""
	num_of_Processes = 0
	postedToday = False;

	def __init__(self, name, url='https://', appID='null', appSecret='null', appToken='null', appTokenLT='null', userToken='null'):
		super(Processes, self).__init__(name, url, appID, appSecret, appToken, appTokenLT, userToken);
		self.data = [];
		Processes.num_of_Processes+=1

	def postHB(self):
		return "Happy Birthday!"

	def makeGetReq(self):
		#make request and save to variable

		#check to see if data is parsed correctly

		#return data as variable
		pass

	def makePostReq(self, data):
		# Try Catch to make post request to url

		pass

	def passData(self):
		pass



#return String
def postHB():
	return "Happy Birthday!"

# Create Single Birthday Object and append to total
def createProcess(name, url="https://"):
	single = Processes(str(name), url);
	all_Processes.append(single);
	return single;
	

# Create n Number of processes
def createProcesses(n, url="https://"):
	defaultProcesses=[createProcess(str(n), url) for n in range(n)];
	all_Processes.append(defaultBirthdays);
	return defaultProcesses;

def createBirthdaysFromEndpointList(urlEndpoints):
	for link in urlEndpoints:
		return Processes(link, link)
		all_Processes.append