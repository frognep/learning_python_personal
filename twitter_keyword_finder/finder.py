import tweepy
import key
import os

# referencing the stored keys in separate file
consumer_key= key.consumer_key
consumer_secret= key.consumer_secret
access_token= key.access_token
access_token_secret= key.access_token_secret

client = tweepy.Client(
   consumer_key= consumer_key, 
   consumer_secret= consumer_secret, 
   access_token= access_token, 
   access_token_secret= access_token_secret
   )

def key_grabber(screen_name, target_word):
   # fetching user's data
   user_ID_Grab = client.get_user(username=screen_name, user_auth= True)

   # grabs the user's ID
   user_TwitID = (user_ID_Grab.data.id)

   # empty list to store all tweets to compare
   stored_tweets = []

   switch = True
   while switch == True:
      print('searching.. ')
      
      # pulls recent 5 tweets (API minimum) from target user's timeline
      target_timeline = client.get_users_tweets(user_TwitID, exclude= ['replies', 'retweets'], max_results= 5, user_auth= True)
      
      for target_tweets in target_timeline.data:
         if target_word in target_tweets.text:
            os.system('clear')
            print('FOUND!! \n \n')
            for tweets in target_timeline.data:
               stored_tweets.append(tweets.text.lower())
            switch = False
      # compares the keyword (target_word) to every word in the list of tweets
      for word in stored_tweets:
         if target_word in word:
            print(word.upper() + '\n \n')

# test: Lover26Matcha
run_again = True
while run_again == True:

   reconfirm_handle = ''
   while reconfirm_handle != 'y':
      user_handle = input('enter target user: ').lower()
      reconfirm_handle = input(f'press y if {user_handle} is correct, or press n to re-enter user: ').lower()

   print('\n')

   reconfirm_keyword = ''
   while reconfirm_keyword != 'y':
      user_keyword = input('enter keyword: ').lower()
      reconfirm_keyword = input(f'press y if {user_keyword} is correct, or press n to re-enter user: ').lower()

   os.system('clear')
   print(f'target user: {user_handle}')
   print(f'keyword: {user_keyword}')
   
   key_grabber(user_handle, user_keyword)
   user_choice = input('press y to rerun. press any key to exit: ').lower()
   if user_choice == 'y':
      os.system('clear')
   else:
      run_again = False
      exit()