import pafy
import urllib
import requests
import json
import os

# Get api key from .env
import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('./')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
api_key = os.getenv('api_key3')

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
        'key={}&channelId={}&part=snippet&order=viewCount&maxResults=5&regionCode=US'.format(
            api_key, channel_id)

    video_links = []
    video_id = []
    url = first_url
    pages=0
    print(url)

    while True:
        inp = requests.get(url)
        resp = inp.json()
        vids = []
        if(pages>0):
            break
        pages=pages+1
        try:
            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(i['snippet']['title'] +
                                       " ,  https://www.youtube.com/watch?v="+i['id']['videoId']+" , "+i['snippet']['thumbnails']['medium']['url'])
                    video_id.append(i['id']['videoId']+","+i['snippet']['publishedAt'])
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
        except Exception as e:
            print("API KEY ERRORRRR: ",e)
            break
    return video_links, video_id

# Use pafy to get video info
def getVideoInfo(video,videoDate):
    try:
        videoPaf = pafy.new(urls)
        print(videoPaf.title,videoPaf.duration,videoPaf.likes,videoPaf.dislikes,videoPaf.viewcount,videoPaf.thumb,videoDate)
        return videoPaf
    except Exception as e:
        print("ERROR ===== ",e)
        return("Error")
    # videoPaf.title, rating, duration, likes,dislikes,length,author

def checkAvailable(videoId):
    r = requests.get("https://img.youtube.com/vi/"+videoId+"/0.jpg")
    # print(r.status_code)
    if(r.status_code>400):
        return False
    return True



# lists = get_all_video_in_channel("UC-lHJZR3Gqxm24_Vd_AJ5Yw")
# video_lists, video_id = get_all_video_in_channel("CGPGrey")
# print(video_lists)
# print(video_id)
# video_id = ['iHzzSao6ypE', 'rNu8XDBSn10', '7Pq-S557XQU', 'qMkYlIA7mgw', 'kF8I_r9XT7A', 'jNgP6d9HraI', 'rStL7niR7gs', 'uqH_Y1TupoQ', 'ASSOQDQvVLU', 'eE_IUPInEuc', 'O37yJBFRrfg', 'sYzfKiIWN4g', 'wfYbgdo8e-8', 'YxgsxaFWWHQ', 'SCzXZfNIu3A', 'OPHRIjI3hXs', 'wOmjnioNulo', 'rE3j_RHkqJc', 'O2hO4_UEe-4', 'JEYh5WACqEk', '3uBcq1x7P34', 'oAHbLRjF0vo', 'OTVE5iPMKLg', 'y5UT04p5f7U', 'BUY6HGqYweQ', '4AivEQmfPpk', 'WKU0qDpu3AM', 'cZYNADOHhVY', 'KIbkoop4AYE', '84aWtseb2-4', 'LrObZ_HZZUc', 'tk862BbjWx4', 'Erp8IAUouus', 'S92fTz_-kQE', 'kcc_KAhwpa0', 'bhyYgnhhKFw', 'LO1mTELoj6o', 'C25qzDhGLx8', 'tlI022aUWQQ', 'Vui-qGCfXuA', 'piEayQ0T-qA', 's7tWHJfhiyo', 'm3_I2rfApYk', 'R9OHn5ZF4Uo', 'Z_2gbGXzFbs', 'SgZ1f4ACZBQ', 'LruaD7XhQ50', 'r9rGX91rq5I', 'F9-iSl_eg5U', '7wC42HgLA4k', 'DbKNlFcg02c', 'h3ppbbYXMxE', 'TsXMe8H6iyc', 'PM79Epw_cp8', 'ULBCuHIpNgU', 'naDCCW5TSpU', 'nQHBAdShgYI', 'xX96xng7sAE', 'l8XOZJkozfI', 'KW0eUrUiyxo', 'sHEDXzOfENI', 'z1ROpIKZe-c', 'ig_qpNfXHIU', '3Y3jE3B8HsE', 'Mky11UJb9AY', 'agZ0xISi40E', 'OUS9mM8Xbbw', 'p3HnMLq8m9U', 'J1Yv24cM2os', 'RbUVKXdu4lQ', 'VPBH1eW28mo', '7-Nl4JFDLOU', 'nU4E6SSy5Yg', 'G3wLQz-LgrM', 'Ex74x_gqTU0', '0dU4IMex4FU', 'hsWr_JWTZss', '_naDg-guomA', '_95I_1rZiIs', 'tUX-frlNBJY', 'wtt2aSV8wdw', 'utDHcbiOfKY', 'SumDHcnCRuU', 'orybDrUj4vA', 'QC-cMv0e3Dc', 'K63ZKa_tt3s', 'QT0I-sdoSXU', 'gaQwC5QbLeQ', 'WVZQapdkwLo', 'tlsU_YT9n_g', 'DIssymQvrbU', 'kh88fVP2FWQ', 'GOiIxqcbzyM', '7vsCAM17O-M', 'zcZTTB10_Vo', '0JK2dR8ei5E', 'jlLUuX2a0Cg', 'e-ZpsxnmmbE', 'snAhsXyO3Ck', 'NVGuFdX5guE', 'wpYtLcRKuPk', 'AM1-ecnQsm4', 'f-mHLBD64HM', 'wvWpdrfoEv0', 'NVmnLaTXylc', '3e5Jn2gG8Eg', 'QMNGEY8OZqo', 'U6ViKuXd5qQ', '8qGCAE1jte8', 'aN44ETT6mUY', 'swx6VyiJ7TI', 'Ac9070OIMUg', 'VvaxkpeSg_4', 'ZmD9RkCJgDI', 'rbHQObTeLDM', 'LIS0IFmbZaI', 'l_wFE9kHSos', 'SuhGwaZiNIk', 'aHRTtA7yTZ0', '6JN4RI7nkes', 'PukSDm0RD2E', 'w5UnNpnGSNI', 'jky6UhxCzTE', 'Pyv1A8StJSs', 'S6QmhrtBTO0', 'uR2DfpjIuXo', 'ABMV4wXx6Xo', 'wRc630BSTIg', 'kUS9uvYyn3A', '8DNtsjB7L_I', 'jxTaj_EfE9g', 'UEX16lWliQc', 'AqwJXTyfNqU', 'btDMr-13d3g', '8CQ3qWgH4B0', '5hPsX3zQeX4', 'uBcGdf4OjQw', 'hvt5xjZTN1U', 'iOWC0g_1IxQ', 'ZtOdVjF_73I', 'YVJXRq7IfgQ', 'ugcV7JSXFN0', 'jIQmdKmtxC4', 'XQuo4-t0p_8', 'KRzQVD6LfCE', 'YJxKvQ4R1GQ', 'nNgzAQINDtw', 'iyoB5erM-W8']
video_id = ['iHzzSao6ypE,2016-08-31T12:36:39Z', 'rNu8XDBSn10,2011-01-30T16:19:41Z', '7Pq-S557XQU,2014-08-13T12:00:03Z', 'qMkYlIA7mgw,2013-06-05T21:35:43Z']
for video in video_id:
    video = video.split(",")
    urls = "https://www.youtube.com/watch?v={}".format(video[0])
    videoPaf = getVideoInfo(urls,video[1])
    # if(not videoPaf):
    #     print(video,videoPaf)