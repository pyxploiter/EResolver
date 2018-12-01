import requests
from bs4 import BeautifulSoup
import re, json
from googleapiclient.discovery import build

def parseContent(content):
	newContent = str()
	for item in content:
		newContent += str(item)
	return newContent

def getAnswerVote(answer):
	voteDiv = answer.find("span", {"class": "vote-count-post"})
	return voteDiv.text

def getAnswerText(answer):
	textDiv = answer.find("div", {"class": "post-text"})
	return parseContent(textDiv.contents)
	#return textDiv.text

def getAnswerDate(answer):
	dateDiv = answer.find("span", {"class": "relativetime"})
	return dateDiv.text

def checkAcceptedAnswer(answer):
	return "accepted-answer" in answer['class'] 

def getQuestion(qPage):
	question = []
	questionDiv = qPage.find("div", {"class": "question"})
	
	questionText = questionDiv.find("div", {"class": "post-text"})
	question.append(parseContent(questionText.contents))

	questionVote = questionDiv.find("span", {"class": "vote-count-post"})
	question.append(questionVote.text)

	questionDate = questionDiv.find("span", {"class": "relativetime"})
	question.append(questionDate.text)

	return question

def getAnswers(qPage):
	return qPage.find_all("div", {"class": "answer"})

def parseAnswers(answers, topAnswers=5):
	newAnswersList = []
	answerCount = 0
	for ans in answers:
		newAnswersList.append([getAnswerText(ans), getAnswerVote(ans), getAnswerDate(ans), checkAcceptedAnswer(ans)])
		answerCount += 1
		if answerCount >= topAnswers:
			break
	return newAnswersList

def printAnswers(answers):
	for x in range(len(answers)):
		print "-----------------------------------------------------"
		print "Answer-"+str(x+1)+": (Votes: "+str(answers[x][1])+")"
		print answers[x][0]
		print "Date:"+str(answers[x][2])

def getStackURLs(query, topURLs=2):
	my_api_key = "XXXX" #google custom search api key
	my_cse_id = "XXXX" #google custom search cse id

	service = build("customsearch", "v1",
	        developerKey=my_api_key)

	res = service.cse().list(
	  q=query,
	  cx=my_cse_id,
	).execute()
	
	items = res['items']
	stackItems = list()
	urlCounter = 0
	for item in items:
		if (re.findall('https://stackoverflow.com/', item['link'])):
			stackItems.append(item['link']) 
			urlCounter += 1
			if urlCounter >= topURLs:
				break
	return stackItems

def resolver(query):
	answersss = list()

	urls = getStackURLs(query)
	response = dict()
	response['query'] = query
	response['answers'] = list()
	for url in urls:
		page = requests.get(url)
		queryPage = BeautifulSoup(page.content, "html.parser")
		question = getQuestion(queryPage)
		answers = parseAnswers(getAnswers(queryPage), topAnswers=5)
		questItem = dict()
		questItem['stack_question_content'] = question[0]
		questItem['stack_question_vote'] = question[1]
		questItem['stack_question_time'] = question[2]
		questItem['stack_answers'] = list()

		for ans in answers:
			ansItem = dict()
			ansItem['answer_content'] = ans[0] 
			ansItem['answer_vote'] = ans[1]
			ansItem['answer_date'] = ans[2]
			ansItem['answer_accepted'] = ans[3]
			questItem['stack_answers'].append(ansItem)
			
			answersss.append(ans[0])
		response['answers'].append(questItem)
	return response
	#return answersss