from appID import appID
from appSecret import appSecret
from appToken import appToken
from appTokenLT import appTokenLT
from userToken import userToken

	
class Api(object):
	baseUrl='https://'
	num_of_objects= 0

	def __init__(self, name, url=baseUrl, appID='null', appSecret='null', appToken='null', appTokenLT='null', userToken='null'):
		self.name = name
		self.url = url
		self.appID = appID
		self.appSecret = appSecret
		self.appToken = appToken
		self.appTokenLT = appTokenLT
		self.userToken = userToken
		
		Api.num_of_objects+=1

	def printUrl(self):
		return self.url;
		# print(self.url)

	def printAppId(self):
		return self.appID;
		# print(self.appID);

	def printAppSecret(self):
		return self.appSecret;

	def printAppToken(self):
		return self.appToken
		# print(self.appToken);

	def printAppTokenLT(self):
		return self.appTokenLT;

	def __repr__(self):
		return "'{}'".format(self.name)

	def __str__(self):
		return "{}".format(self.name);

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())

