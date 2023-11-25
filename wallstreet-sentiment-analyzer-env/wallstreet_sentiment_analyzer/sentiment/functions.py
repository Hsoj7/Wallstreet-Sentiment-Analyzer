import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

def extract_comments(comment):
    # Recursive function to extract comments and replies
    comments = [comment.body]
    for reply in comment.replies:
        comments.extend(extract_comments(reply))
    return comments

def get_reddit_comments():
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

    # Process and return the comments
    return [comment.body for comment in submission.comments.list() if not isinstance(comment, praw.models.MoreComments)]

if __name__ == "__main__":
    # Call your function here
    reddit_comments = get_reddit_comments()

    # Example: Print the retrieved comments
    for comment in reddit_comments:
        print(comment)
