import praw
from datetime import datetime
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD


def get_reddit_data():
    # Initialize PRAW
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=USERNAME,
        password=PASSWORD
    )

    # Specify the subreddit
    subreddit = reddit.subreddit('wallstreetbets')

    # Get the most recent 50 posts
    recent_items = subreddit.new(limit=50)
    # Get the most recent 50 comments
    # recent_items = subreddit.comments(limit=50)

    # Process and return relevant information from the items
    data_info = []

    for item in recent_items:
        if isinstance(item, praw.models.Submission):
            # For posts
            data_info.append({'type': 'post',
                              'timestamp': datetime.utcfromtimestamp(item.created_utc),
                              'title': item.title,
                              'url': item.url})
        elif isinstance(item, praw.models.Comment):
            # For comments
            data_info.append({'type': 'comment',
                              'timestamp': datetime.utcfromtimestamp(item.created_utc),
                              'body': item.body})

    return data_info


if __name__ == "__main__":
    # Call your function here
    reddit_data = get_reddit_data()

    # Example: Print the retrieved data
    for data_item in reddit_data:
        print(data_item)
