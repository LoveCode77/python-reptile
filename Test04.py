# TODO 视频网址
# url = 'https://www.bilibili.com/video/BV1jt421c7yN/'
url='https://console.nuoyun.tv/Watch/156057834'
headers = {
    # Referer 防盗链 告诉服务器你请求链接是从哪里跳转过来的
    # "Referer": "https://www.bilibili.com/video/BV1454y187Er/",
    "Referer": url,
    # User-Agent 用户代理, 表示浏览器/设备基本身份信息
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
import requests

# TODO 通过F12查看视频的地址
# video_url = 'https://xy183x214x144x8xy2409y8c50yda00y126yy8xy.mcdn.bilivideo.cn:4483/upgcxcode/83/23/1523062383/1523062383-1-100113.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1715968562&gen=playurlv2&os=mcdn&oi=1879749745&trid=00008c163333de3442dc929f4f62aff31adau&mid=691902317&platform=pc&upsig=a453aaa2553b8cd8f2fcca789fcd68d2&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=50002512&bvc=vod&nettype=0&orderid=0,3&buvid=2844B77E-F527-FB05-1DF5-9FDF834AE3E888277infoc&build=0&f=u_0_0&agrr=0&bw=25270&logo=A0020000'
video_url ='https://vod1.nuoyun.tv/e2e04cfdvodcq1254131505/dd57ae4b1253642701323743100/playlist.f3_0.ts'
video_response = requests.get(video_url, headers=headers)
with open('luzhi01.mp4', mode='wb') as v:
    v.write(video_response.content)

# # TODO 通过F12查看音频的地址
# # audio_url = 'https://xy183x214x144x8xy2409y8c50yda00y126yy8xy.mcdn.bilivideo.cn:4483/upgcxcode/83/23/1523062383/1523062383-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1715968562&gen=playurlv2&os=mcdn&oi=1879749745&trid=00008c163333de3442dc929f4f62aff31adau&mid=691902317&platform=pc&upsig=a9e345e9808698097e942b690872ece1&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=50002512&bvc=vod&nettype=0&orderid=0,3&buvid=2844B77E-F527-FB05-1DF5-9FDF834AE3E888277infoc&build=0&f=u_0_0&agrr=0&bw=9931&logo=A0020000'
# audio_url ='https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/62/07/167220762/167220762_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1721502677&gen=playurlv2&os=cosbv&oi=29456127&trid=25fabc0a8fc54d749800b3ae961ad486u&mid=201491267&platform=pc&og=cos&upsig=052ab9e763309118ea9ad75860f72826&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=99F5835C-A516-25A6-965A-BDAB1170D87C03387infoc&build=0&f=u_0_0&agrr=0&bw=15909&logo=80000000'
# audio_response = requests.get(audio_url, headers=headers)
# with open('yingping1.mp3', mode='wb') as v:
#     v.write(audio_response.content)
