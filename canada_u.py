import praw

# Create our Reddit client (lets us communicate with Reddit)
reddit = praw.Reddit(client_id='X8SOj2XwYw0RwA',
                     client_secret='WajadMY0iH0lRPe7wVBK_0lFkOg',
                     user_agent='my user agent')

# Go through the first 10 hot posts in the uwaterloo subreddit
for submission in reddit.subreddit('uwaterloo').hot(limit=10):
    print(submission.title)