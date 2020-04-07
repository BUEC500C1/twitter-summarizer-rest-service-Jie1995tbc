import tweepy
import os
import re
from PIL import Image, ImageDraw, ImageFont
import configparser
import json



def tweets_get(key_input):
    '''Get the text from twitter using tweepy and convert text into image'''
    config = configparser.ConfigParser()
    file = 'keys'
    if os.path.exists(file) :
        config.read(file)
        auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
        auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_token_secret').strip())
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        public_tweets = api.user_timeline(key_input)
        with open("data.json","w") as f:

            json.dump(public_tweets,f)
    else :
        with open('data.json', 'r') as f: #convert json string to dict
            public_tweets = json.load(f)

    #setFont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
    setFont = ImageFont.truetype('Arial.ttf', 50)
    count = 0;
    color = "#000000"
    header_y = 500


    image = Image.open('image/start.jpg')
    width, height = image.size
    draw = ImageDraw.Draw(image)

    tweets_contain = []

    for tweets in public_tweets:
        gap = '\n'
        for key, value in tweets.items():
            if key == 'text':
                list_contain_tweets = list(value)
        #list_contain_tweets = list(tweets.text)

        for n in range(len(list_contain_tweets)):
            if (n % 60 == 0):
                list_contain_tweets.insert(n, gap)

        tweets_text = ''.join(list_contain_tweets)
        tweets_text = re.sub("#", r'\#', tweets_text)
        tweets_text = re.sub("@", r'\@', tweets_text)
        tweets_text = re.sub('\n', '', tweets_text)

        # tweets.text = tweets.text + '\n'
        tweets_contain.append(tweets_text)

        print(tweets_text)


    for num, content in enumerate(tweets_contain):
        num += 1
        draw.text((100,height - header_y),u'%s. %s' %(num, content),color,setFont)
        header_y -= 50
    image.save('image/' + key_input + '.jpg')
    #image.save('image/' + key_input + '.jpg')
    print('-------END-------')


if __name__ == '__main__':
    tweets_get('Tesla')
