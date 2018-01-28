
from googleapiclient.discovery import build

Developer_Key = "your key"
Service_name = "youtube"
version = "v3"

def youtube_search(q, max_results=50, order="relevance", token=None, location=None, location_radius=None):

    youtube = build(Service_name, version, developerKey=Developer_Key)

    search_response = youtube.search().list(
        q=q,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=max_results,
        location=location,
        locationRadius=location_radius).execute()

    searched_videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            searched_videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return nexttok, searched_videos

    except Exception as e:
        nexttok = "last_page"
        return nexttok, searched_videos


def video_data_mining(video_id):

    youtube = build(Service_name, version,developerKey=Developer_Key)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'
    ).execute()

    return video_response
