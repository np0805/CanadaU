import os
from collections import Counter

import spacy
import praw
import prawcore
from flask import Flask

# Create our Reddit client to communicate with Reddit
# NOTE: Remember to fill in the '<>'!
reddit = praw.Reddit(client_id='X8SOj2XwYw0RwA',
                     client_secret='WajadMY0iH0lRPe7wVBK_0lFkOg',
                     user_agent='web:CanadaU:1.0 (by /u/reddit savvymanager)')

# Create our Flask application
app = Flask(__name__)

# Add an endpoint to our Flask application
@app.route('/subreddit/<subreddit_id>')
# This function has a new parameter subreddit_id!
def subreddit(subreddit_id):
    return reddit.subreddit(subreddit_id).description_html

# - - - WE WILL ADD NEW ENDPOINTS HERE - - -
# Endpoints to get the subscriber count
@app.route('/subreddit/<subreddit_id>/subscribers')
def subreddit_count_subscribers(subreddit_id):
    try:
        return ({ 'subscribers': reddit.subreddit(subreddit_id).subscribers }, 200)
    except prawcore.exceptions.Redirect:
        return ("Couldn't find subreddit.", 404)

# Endpoint to get the banner img of a subreddit
@app.route('/subreddit/<subreddit_id>/banner')
def subreddit_banner_img(subreddit_id):
    try:
        banner_img = reddit.subreddit(subreddit_id).banner_img
        return ("<img src=%s>" % banner_img, 200)
    except prawcore.exceptions.Redirect:
        return ("Couldn't find subreddit.", 404)

# Endpoint to titles of top 10 posts of a subreddit
@app.route('/subreddit/<subreddit_id>/top')
def subreddit_top_posts(subreddit_id):
    # Check if the user specified the number of posts to get
    # E.g., /subreddit/uwaterloo/top?limit=100
    # NOTE: anything after the '?' in a URL is called a QUERY PARAMETER!
    limit = request.args.get('limit')
    # If not specified, or invalid, default to 10.
    try:
        limit = int(limit)
    except:
        limit = 10
    limit = min(100, limit)

    subreddit = reddit.subreddit(subreddit_id)
    # Get top posts of all time
    top_posts = subreddit.top('all', limit=limit)
    # Get title of each post
    top_posts_titles = [ post.title for post in top_posts ]
    # Return dictionary with response
    return ({ 'top_posts': list(top_posts_titles) }, 200)

# Endpoint to get the most common words from the top 100 posts of a subreddit
nlp = spacy.load("en_core_web_sm")
@app.route('/subreddit/<subreddit_id>/topWords')
def subreddit_common_words(subreddit_id):
    subreddit = reddit.subreddit(subreddit_id)
    # Get top 10 posts of all time
    top_posts = subreddit.top('month', limit=500)
    # Get title of each post
    top_posts_titles = [ post.title for post in top_posts ]
    top_posts_titles_text = " ".join(top_posts_titles)
    # Filter out irrelevant tokens
    doc = nlp(top_posts_titles_text)
    tokens = [
        token.text.lower() for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.is_digit
    ]
    word_count = Counter(tokens)
    # Use only words mentioned at least twice
    filtered_word_count = [count for count in word_count.items() if count[1] > 1]
    # Sort words by count
    sorted_word_count = sorted(filtered_word_count, key=lambda item: item[1], reverse=True)
    # Return dictionary with response
    return ({ 'word_count': sorted_word_count }, 200)

if __name__ == "__main__":
    app.run()