import pafy
import urllib
import requests
import json
import os

# Get api key from .env
api_key = os.getenv('api_key')

# Api key test
def getUrlTest(channel_id):
    if not channel_id.startswith("UC"):
        u_url = "https://www.googleapis.com/youtube/v3/channels?key={}&forUsername={}&part=id".format(
            api_key, channel_id)

        inp = requests.get(u_url)
        resp = inp.json()
        channel_id = (resp["items"][0]["id"])

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + \
        'key={}&channelId={}&part=snippet&maxResults=50&order=viewCount&regionCode=US'.format(
            api_key, channel_id)
    print(first_url)

# Retrieve list of all videos in channel
def get_all_video_in_channel(channel_id):
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    if not channel_id.startswith("UC"):
        u_url = "https://www.googleapis.com/youtube/v3/channels?key={}&forUsername={}&part=id".format(
            api_key, channel_id)

        inp = requests.get(u_url)
        resp = inp.json()
        channel_id = (resp["items"][0]["id"])

    first_url = base_search_url + \
        'key={}&channelId={}&part=snippet&order=viewCount&maxResults=100&regionCode=US'.format(
            api_key, channel_id)

    video_links = []
    video_id = []
    url = first_url
    print(url)

    while True:
        inp = requests.get(url)
        resp = inp.json()
        vids = []
        try:
            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(i['snippet']['title'] +
                                       " ,  https://www.youtube.com/watch?v="+i['id']['videoId']+" , "+i['snippet']['thumbnails']['medium']['url'])
                    video_id.append(i['id']['videoId'])
                    vids.append(i['id']['videoId'])

            mid = vids[int(len(vids)/2)]
            last = vids[-1]
            # print(mid, last)

            # vid_url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id={}&regionCode=US&key={}".format(
            #     last, api_key)
            # inp = requests.get(vid_url).json()
            # print(inp["items"][0]["statistics"]["viewCount"])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
        except:
            print("API KEY ERRORRRR")
            break
    return video_links, video_id

# Use pafy to get video info
def getVideoInfo(video):
    # lists = get_all_video_in_channel2("UC-lHJZR3Gqxm24_Vd_AJ5Yw")
    video_lists, video_id = get_all_video_in_channel("CypherX01")
    print(video_id)
    for video in video_id:
        urls = "https://www.youtube.com/watch?v={}".format(video)
        videoPaf = pafy.new(urls)
        print(video+" , "+str(videoPaf.viewcount))
    # videoPaf.title, rating, duration, likes,dislikes,length,author


