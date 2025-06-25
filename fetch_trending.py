
from googleapiclient.discovery import build
import json

def fetch_trending_shorts(api_key, max_results=10):
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        maxResults=max_results,
        order="viewCount",
        q="shorts",
        type="video",
        videoDuration="short"
    )
    response = request.execute()

    trending = []
    for item in response['items']:
        video_data = {
            "title": item['snippet']['title'],
            "videoId": item['id']['videoId'],
            "description": item['snippet']['description'],
            "channel": item['snippet']['channelTitle'],
            "url": f"https://www.youtube.com/shorts/{item['id']['videoId']}"
        }
        trending.append(video_data)

    with open("trending_shorts.json", "w") as f:
        json.dump(trending, f, indent=2)

    return trending
