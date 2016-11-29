# Yelp

import rauth
import time

def main():

	locations = ["Montgomery, Alabama", "Juneau, Alaska", "Phoenix, Arizona", "Little Rock, Arkansas", "Sacramento, California", "Denver, Colorado",
				"Hartford, Connecticut", "Dover, Delaware", "Tallahassee, Florida", "Atlanta, Georgia", "Honolulu, Hawaii", "Boise, Idaho",
				"Springfield, Illinois", "Indianapolis, Indiana", "Des Moines, Iowa", "Topeka, Kansas", "Frankfort, Kentucky", "Baton Rouge, Louisiana",
				"Augusta, Maine", "Annapolis, Maryland", "Boston, Massachusetts", "Lansing, Michigan", "Saint Paul, Minnesota", 
				"Jackson, Mississippi", "Jefferson City, Missouri", "Helena, Montana", "Lincoln, Nebraska", "Carson City, Nevada", 
				"Concord, New Hampshire", "Trenton, New Jersey", "Santa Fe, New Mexico", "Albany, New York", "Raleigh, North Carolina", 
				"Bismarck, North Dakota", "Columbus, Ohio", "Oklahoma City, Oklahoma", "Salem, Oregon", "Harrisburg, Pennsylvania", 
				"Providence, Rhode Island", "Columbia, South Carolina", "Pierre, South Dakota", "Nashville, Tennessee", "Austin, Texas", 
				"Salt Lake City, Utah", "Montpelier, Vermont", "Richmond, Virginia", "Olympia, Washington", "Charleston, West Virginia", 
				"Madison, Wisconsin", "Cheyenne, Wyoming"]

	api_calls = []
	city_data_listings = [] 
	for city in locations:
		params = get_search_parameters(city)
		api_calls.append(get_results(params))
		time.sleep(1.0)


	# Makes copy pasting into excel easier
	for index in range(len(locations)):
		print(locations[index])
	for index in range(len(locations)):
		print(api_calls[index]['total'])

	#   To fill city_data_listings, uncomment below
	# 	city_listings.append((locations[index], api_calls[index]['total']))




def get_results(params):

	#Obtain these from Yelp's manage access page
	consumer_key = "INSERT HERE"
	consumer_secret = "INSERT HERE"
	token = "INSERT HERE"
	token_secret = "INSERT HERE"
	
	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)

	request = session.get("http://api.yelp.com/v2/search",params=params)
	
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	session.close()
	
	return data

def get_search_parameters(city):

  #Different Paramters: https://www.yelp.com/developers/documentation/v2/search_api

  params = {}
  params["term"] = "restaurant"
  params["location"] = "{}".format(str(city))
  params["category_filter"] = "halal"

  return params

if __name__=="__main__":
  	main()






