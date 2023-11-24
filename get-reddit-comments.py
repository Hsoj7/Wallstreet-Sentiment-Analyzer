import praw
# Make sure to have a local config file
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

# Initialize PRAW
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD
)

# Specify the URL of the Reddit post
post_url = 'https://new.reddit.com/r/wallstreetbets/comments/182ay78/what_are_your_recipes_tomorrow_november_24th_2022/'

# Extract the post ID from the URL
post_id = post_url.split('/')[-3]

# Fetch the post
submission = reddit.submission(id=post_id)

# Print the post title
print(f"Post Title: {submission.title}\n")

# Download and print the body of the comments
for comment in submission.comments.list():
    print(comment.body)

