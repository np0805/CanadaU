import praw

# Create our Reddit client (lets us communicate with Reddit)
reddit = praw.Reddit(client_id='X8SOj2XwYw0RwA',
                     client_secret='WajadMY0iH0lRPe7wVBK_0lFkOg',
                     user_agent='web:CanadaU:1.0 (by /u/savvymanager)')

# # Go through the first 10 hot posts in the uwaterloo subreddit
# for submission in reddit.subreddit('uwaterloo').hot(limit=10):
#     print(submission.title)

"""
- - - SUBREDDIT OPERATIONS - - -
"""
subreddit = reddit.subreddit("anime")

print("Subscriber Count: %d" % subreddit.subscribers)

print("Hot")
hot_submissions = subreddit.hot(limit=10)
i = 1
for submission in hot_submissions:
    print(i,"\t %s" % submission.title)
    i = i + 1

i = 1
print("Top of All Time")
top_submissions = subreddit.top('all', limit=10)
for submission in top_submissions:
    print(i,"\t %s" % submission.title)
    i = i + 1

# For more examples, see:
# https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html



"""
- - - SUBMISSION AND COMMENT OPERATIONS - - -
"""
i = 1
print("Comments on Top Submission")
top_submissions = subreddit.top('all', limit=10)
top_submission = next(top_submissions)
comments = top_submission.comments
for comment in comments:
    try:
        print(i,"\t %s" % comment.body)
        i = i + 1
    except AttributeError:
        pass

# For more examples, see:
# https://praw.readthedocs.io/en/latest/code_overview/other/commentforest.html