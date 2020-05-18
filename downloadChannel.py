import pafy
import urllib
import requests
import json
from os import path
import os

# Get api key from .env
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser("./")  # adjust as appropriate
load_dotenv(os.path.join(project_folder, ".env"))
api_key = os.getenv("api_key5")

# Api key test
def getUrlTest(channel_id):
    if not channel_id.startswith("UC"):
        u_url = "https://www.googleapis.com/youtube/v3/channels?key={}&forUsername={}&part=id".format(
            api_key, channel_id
        )

        inp = requests.get(u_url)
        resp = inp.json()
        channel_id = resp["items"][0]["id"]

    base_video_url = "https://www.youtube.com/watch?v="
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"

    first_url = (
        base_search_url
        + "key={}&channelId={}&part=snippet&maxResults=5&order=viewCount&regionCode=US".format(
            api_key, channel_id
        )
    )
    print(first_url)


# Retrieve list of all videos in channel
def get_all_video_in_channel(channel_id):
    base_video_url = "https://www.youtube.com/watch?v="
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"
    first_url = (
        base_search_url
        + "key={}&channelId={}&part=snippet&order=viewCount&maxResults=50&regionCode=US".format(
            api_key, channel_id
        )
    )

    video_links = []
    video_id = []
    url = first_url
    pages = 0
    print(url)

    while True:
        inp = requests.get(url)
        resp = inp.json()
        vids = []
        if pages > 1:
            break
        pages += 1
        try:
            for i in resp["items"]:
                if i["id"]["kind"] == "youtube#video":
                    video_links.append(
                        i["snippet"]["title"]
                        + " ,  https://www.youtube.com/watch?v="
                        + i["id"]["videoId"]
                        + " , "
                        + i["snippet"]["thumbnails"]["medium"]["url"]
                    )
                    video_id.append(
                        i["id"]["videoId"] + "," + i["snippet"]["publishedAt"]
                    )
                    vids.append(i["id"]["videoId"])

            mid = vids[int(len(vids) / 2)]
            last = vids[-1]

            try:
                next_page_token = resp["nextPageToken"]
                url = first_url + "&pageToken={}".format(next_page_token)
            except:
                break

        except Exception as e:
            print("API KEY ERRORRRR: ", e)
            break

    return channel_id, video_links, video_id


# Use pafy to get video info
def getVideoInfo(video, videoDate):
    try:
        videoPaf = pafy.new(video)
        return videoPaf
    except Exception as e:
        print("ERROR ===== ", e)
        return "Error"
    # videoPaf.title, rating, duration, likes,dislikes,length,author


def checkAvailable(videoId):
    r = requests.get("https://img.youtube.com/vi/" + videoId + "/0.jpg")
    if r.status_code > 400:
        return False
    return True


# done = zefrank1, zach king, billwurtz, cgpgrey,
def main():
    # channels = ["billwurtz","UC3Liv5-jdU2Qk53lTtYDG2w","zefrank1", "ZachKingVine","CorridorDigital","Airforceproud95","CaptainDisillusion","coldfustion","Computerphile","CinemaSins","UCdC0An4ZPNr_YiFiYoVbwaw","UCmh5gdwCx6lN7gEC20leNVA","corycotton","ErasableNinja","UCR1D15p_vdP3HkrH8wgjQRw","jacksfilms","UCYLS9TSah19IsB8yyUpiDzg","UCsXVk37bltHxD1rDPwtNM8Q","UCm9K6rby98W8JigLoZOh6FQ","UCfb2YpWR9FWTJMjzvAlP0_Q","UCY1kMZp36IQSyNx_9h4mpCg","UCBJycsmduvYEL83R_U4JriQ","UCY3TJECrA90t9YTrxhdjcVw","UCtHaxi4GTYDpJgMSGy7AeSw","UCX6OQ3DkcsbYNE6H8uQQuVA","UCxsQFG_8Dbt1sZhLReL2mUw","UCJkMlOu7faDgqh4PfzbpLdg","UCSAUGyc_xA8uYzaIVG6MESQ","UCNIuvl7V8zACPpTmmNIqP2A","UCeE3lj6pLX_gCd0Yvns517Q","UC7yF9tV4xWEMZkel7q8La_w","UC6MFZAOHXlKK1FI7V0XQVeA","Airforceproud95","UCAL3JXZSzSm8AlZyD3nQdBA","TheInfographicsShow","UCdN4aXTrHAtfgbVG9HjBmxQ","UCY3TJECrA90t9YTrxhdjcVw","UCfoK9LI9vmQQ36zqsFZtNJQ","UCvQECJukTDE2i6aCoMnS-Vg","UCq6aw03lNILzV96UvEAASfQ","UCEOXxzW2vU0P-0THehuIIeg","UC2C_jShtL725hvbm1arSV9w","UCYUQQgogVeQY8cMQamhHJcg","UC4QZ_LsYcvcq7qOsOhpAX4A","UC9-y-6csu5WGm29I7JiwpnA","UCsn6cjffsvyOZCZxvGoJxGg","UCn1XB-jvmd9fXMzhiA6IR0w","UCgrpA6pVkSU3WfCjL1NN7Ig","UCPcFg7aBbaVzXoIKSNqwaww","UCY1kMZp36IQSyNx_9h4mpCg","UCq6VFHwMzcMXbuKyG7SQYIg","UCmheCYT4HlbFi943lpH009Q","UC7OIF66iuk4yWXNOGluqEXA","UCfdNM3NAhaBOXCafH7krzrA","UCRcgy6GzDeccI7dkbbBna3Q","UCq8DICunczvLuJJq414110A","UCVpankR4HtoAVtYnFDUieYA"]

    # channels = ["KQEDDeepLook","DNewsChannel","UCUhFaUpnq31m6TNX2VKVSVA","UC04KsGq3npibMCE9Td3mVDg","lincolnmarkham","TheViralFeverVideos","UCLOwKVD0bYHxaDZxXkK4piw","UCRS07TwUdb9hTnnX0r5CuxA","twosetviolin"]

    channels = ["nigahiga", "UCP5tjEmvPItGyLhmjdwP7Ww"]

    for channel in channels:
        channelName = channel

        if not channel.startswith("UC"):
            u_url = "https://www.googleapis.com/youtube/v3/channels?key={}&forUsername={}&part=id".format(
                api_key, channel
            )

            inp = requests.get(u_url)
            resp = inp.json()
            channel = resp["items"][0]["id"]

        raw_file_name = "./data/" + channel + ".csv"
        raw_file_name = raw_file_name.replace("_", "----")

        if path.exists(raw_file_name):
            continue

        output_file = open(raw_file_name, "a")
        output_data = ""

        channel_id, video_lists, video_id = get_all_video_in_channel(channel)

        for video in video_id:
            try:
                video = video.split(",")
                urls = "https://www.youtube.com/watch?v={}".format(video[0])

                videoPaf = getVideoInfo(urls, video[1])

                if videoPaf.viewcount < 100000:
                    break

                if not videoPaf == "Error":
                    videoMeta = [
                        str(channel_id),
                        str(video[0]),
                        videoPaf.title.replace(",", "---"),
                        str(videoPaf.author),
                        str(videoPaf.duration),
                        str(videoPaf.likes),
                        str(videoPaf.dislikes),
                        str(videoPaf.viewcount),
                        str(videoPaf.thumb),
                        video[1],
                    ]

                    videoStr = ",".join(videoMeta)
                    videoStr = videoStr + "\n"
                    output_file.write(videoStr)

                    output_data += videoStr
                    print(videoStr)
            except:
                continue

        output_file.close()


if __name__ == "__main__":
    main()
