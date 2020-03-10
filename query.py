import pickle
import sys
import json
with open("data_file.pickle","rb") as file:
	postings_list = pickle.load(file)

def query_and(word1_postings_list, word2_postings_list):
        result_list_boolean_and = list(set(word1_postings_list) & set(word2_postings_list))		
	for i in result_list_boolean_and:
		print(i)
def query_or(word1_postings_list, word2_postings_list): 
	result_list_boolean_or = list(set(word1_postings_list) | set(word2_postings_list)) 
	for i in result_list_boolean_or:
		print(i)
while(True):
	input_value = raw_input("Single/Boolean Query(Enter S for Single and B for Boolean(AND/OR)[For exit press E]:")
	if(input_value.lower() == "s"):
		query_single = raw_input("Enter the movie genre")
		query_single = query_single.lower()
		if(query_single in postings_list.keys()):
			postings_single = postings_list[query_single]
			for i in postings_single:
				print(i)
		else:
			print("Invalid movie genre entered")
	elif(input_value.lower() == "b"):
		query = raw_input("Enter the query to search for(Movie genre Boolean(AND/OR) Movie genre)[For exit E]")
		word = query.split()
		if(len(word) == 3):
			word1 = word[0].lower()
			boolean = word[1].lower()
			word2 = word[2].lower()
			if(query.lower() == "e"):
				print("EXIT.........................")
				break
			if(word1 in postings_list.keys() and word2 in postings_list.keys()):
				word1_postings_list = postings_list[word1]
				word2_postings_list = postings_list[word2]
				if boolean.lower() == "and":
					query_and(word1_postings_list, word2_postings_list)
				elif boolean.lower() == "or":
					query_or(word1_postings_list, word2_postings_list)
				else:
					print("Invalid boolean type entered")
			else:
				print("Invalid movie genre entered")
		else:
			print("Please enter a valid query")
	elif(input_value.lower()=="e"):
		print("EXIT........................")
		break
	else:
		print("Inavlid entry")
