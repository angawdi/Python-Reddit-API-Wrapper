import praw
import random

CLIENT_ID = 'oEiQ8VCRHmmvaQ'
CLIENT_SECRET = 'z7lijM88X_GT7wU2uKESHx90vXY'
BOT_NAME = 'redditcreate9989'
BOT_PASSWORD = 'NOifw-239/faw'
USER_AGENT = 'script:oEiQ8VCRHmmvaQ:0.0.1(by /u/coolandy)'
quote_choices = ['What\'s Up?',
    'Howdy',
    'Hey, do you like cats?',
    'How much does a polar bear weigh?',
    'What do you call a cow with no legs?',
    'What happened when the wheel was invented?']

def pick_quote_index():
    return random.randint(0, len(quote_choices) - 1)

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT,
                     username=BOT_NAME,
                     password=BOT_PASSWORD)

# assume you have a Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit('test')
print(subreddit.display_name, subreddit.title)  # Output: test

count = 1

# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.hot():
    print(count, submission.title, submission.score, 'votes')  # Output: the submission's score
    if submission.score <= 1:
        submission.reply('A lonely post!\n\n☆☆☆\n\n' + quote_choices[pick_quote_index()])
    count += 1