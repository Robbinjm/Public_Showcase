import requests
import pprint
import json
import random


top100_user_scores = []
mediocre_user_scores = []
low_user_scores = []

critic_top100_rt_score = []
common_rt_top100_score = []

critic_med_rt_score = []
common_med_score = []

critic_low_rt_score = []
common_rt_low_score = []

def GetMovie(movie_name):

    url = "https://flixster.p.rapidapi.com/search"

    querystring = {"query":{movie_name}}

    headers = {
        "X-RapidAPI-Key": "75bf1504fcmsh221e172eefbe35bp1e1880jsna424546223e7",
        "X-RapidAPI-Host": "flixster.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.text
    js_std_out = json.loads(response)
    try:
        title = js_std_out['data']['search']['movies'][0]['name']
        global rt_critic_rating
        rt_critic_rating = js_std_out['data']['search']['movies'][0]['tomatoRating']['tomatometer']
        global rt_user_rating
        rt_user_rating = js_std_out['data']['search']['movies'][0]['userRating']['dtlLikedScore']
    except:
        title = js_std_out['data']['search']['movies'][1]['name']
        rt_critic_rating = js_std_out['data']['search']['movies'][0]['tomatoRating']['tomatometer']
        rt_user_rating = js_std_out['data']['search']['movies'][0]['userRating']['dtlLikedScore']

    #print(f'Title: {title}\nCritic RT score: {rt_critic_rating}\nUser RT score: {rt_user_rating}')

def StartTop100():

    print('_____________________\nStart Top 100\n')
    cont = True
    while cont:
        ## TOP 100 MOVIES
        with open('/home/jordan/Documents/rottenTomatoProj/top100.txt', 'r') as top100file:
            top_movies_file = top100file.readlines()
            random_top100 = random.choice(top_movies_file)

            user_seen_movie_input = input(f'Have you seen the movie {random_top100}>\n').lower()

            if user_seen_movie_input == 'yes' or user_seen_movie_input == 'y':
                try:
                    GetMovie(random_top100)
                    user_scores_movie = int(input(f'On a scale from 1-100, what score would you give {random_top100}>\n'))
                    ##append scores to lists
                    top100_user_scores.append(user_scores_movie)
                    critic_top100_rt_score.append(rt_critic_rating)
                    common_rt_top100_score.append(rt_user_rating)
                    print(f'User - {top100_user_scores}\nCritics - {critic_top100_rt_score}\nCommons - {common_rt_top100_score}')
                    cont = False
                except:
                    print('Sorry!! Cant find a score for this film, lets try another..\n')
                    cont = True
            else:
                cont = True



def StartMediocre():

    print('_____________________\nStart Mediocre\n')
    cont = True
    while cont:
        ## MEDIOCRE MOVIES 1985 - Current
        with open('/home/jordan/Documents/rottenTomatoProj/mediocre_movies_1985.txt', 'r') as mediocreFile:
            mediocre_movies_file = mediocreFile.readlines()
            random_mediocre = random.choice(mediocre_movies_file)

            user_seen_movie_input = input(f'Have you seen the movie {random_mediocre}>\n').lower()

            if user_seen_movie_input == 'yes' or user_seen_movie_input == 'y':
                try:
                    GetMovie(random_mediocre)
                    user_scores_movie = int(
                        input(f'On a scale from 1-100, what score would you give {random_mediocre}>\n'))
                    ##append scores to lists
                    mediocre_user_scores.append(user_scores_movie)
                    critic_med_rt_score.append(rt_critic_rating)
                    common_med_score.append(rt_user_rating)
                    print(
                        f'User - {mediocre_user_scores}\nCritics - {critic_med_rt_score}\nCommons - {common_med_score}')
                    cont = False
                except:
                    cont = True
                    print('Sorry!! Cant find a score for this film, lets try another..\n')
            else:
                cont = True



def StartLowScore():

    print('_____________________\nStart lowest\n')
    cont = True
    while cont:
        ## Lowest 185 since 1985
        with open('/home/jordan/Documents/rottenTomatoProj/lowest_rated_since_1985.txt', 'r') as lowestFile:
            lowest_movies_file = lowestFile.readlines()
            random_lowest = random.choice(lowest_movies_file)

            user_seen_movie_input = input(f'Have you seen the movie {random_lowest}>\n').lower()

            if user_seen_movie_input == 'yes' or user_seen_movie_input == 'y':
                try:
                    GetMovie(random_lowest)
                    user_scores_movie = int(
                        input(f'On a scale from 1-100, what score would you give {random_lowest}>\n'))
                    ##append scores to lists
                    low_user_scores.append(user_scores_movie)
                    critic_low_rt_score.append(rt_critic_rating)
                    common_rt_low_score.append(rt_user_rating)
                    print(
                        f'User - {low_user_scores}\nCritics - {critic_low_rt_score}\nCommons - {common_rt_low_score}')
                    cont = False
                except:
                    cont = True
                    print('Sorry!! Cant find a score for this film, lets try another..\n')
            else:
                cont = True




StartTop100()
StartMediocre()
StartLowScore()