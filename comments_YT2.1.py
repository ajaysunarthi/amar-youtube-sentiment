from gdata.youtube import service
from urllib import urlopen, unquote; 
from urlparse import parse_qs, urlparse; 
import sys;
import codecs;


if len(sys.argv)!= 2:
	sys.exit("must provide the URL")
	
youtube_watchurl=sys.argv[1]; 
VIDEO_ID= parse_qs(urlparse(youtube_watchurl).query)['v'][0]; 	

USERNAME = 'xyz@gmail.com'
PASSWORD = 'gmail_passwd'
"""VIDEO_ID = 'pdcwbQa7S5E'"""

def comments_generator(client, video_id):
    comment_feed = client.GetYouTubeVideoCommentFeed(video_id=video_id)
    while comment_feed is not None:
        for comment in comment_feed.entry:
             yield comment
        next_link = comment_feed.GetNextLink()
        if next_link is None:
             comment_feed = None
        else:
             comment_feed = client.GetYouTubeVideoCommentFeed(next_link.href)

client = service.YouTubeService()
client.ClientLogin(USERNAME, PASSWORD)

for comment in comments_generator(client, VIDEO_ID):
	author_name = comment.author[0].name.text
	text = comment.content.text
	print("{}: {}".format(author_name, text))
	