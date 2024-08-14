# 正常的爬虫

# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入json模块
import json
# TODO 记得更改你要的url和你自己的cookie
url = 'https://www.bilibili.com/video/BV1uZ4y1k76V'
cookie = "i-wanna-go-back=-1; FEED_LIVE_VERSION=V8; buvid4=2EA18AE5-40BF-AFB6-4A95-5896BC7BC0DB08931-023062523-E6mdP7iVh21l5uM1h7Ta9Q%3D%3D; DedeUserID=201491267; DedeUserID__ckMd5=7c675d8f7bfcca20; rpdid=|(JYlmJY)RmR0J'uY)~~uklJm; CURRENT_FNVAL=16; is-2022-channel=1; LIVE_BUVID=AUTO4216930552081916; header_theme_version=CLOSE; enable_web_push=DISABLE; hit-dyn-v2=1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; PVID=1; CURRENT_QUALITY=0; buvid3=99F5835C-A516-25A6-965A-BDAB1170D87C03387infoc; b_nut=1719244703; _uuid=8B82DE10A-CA55-E7A6-5B5C-CA34237F1078F04181infoc; fingerprint=f3390ac900a6679d9b640ae96d757423; home_feed_column=5; browser_resolution=1862-901; buvid_fp=f3390ac900a6679d9b640ae96d757423; SESSDATA=d41cc351%2C1737391149%2Cefb94%2A72CjCUx3OXuf1rOu9RvkR7xf0IoCG62IMVWd2QTaJdo4bzDWuss4cP_u1QZGzwwZJ6yvESVnlHaDZrQ2FFQnJoQUV2bXJnT2N3NUNndUdwUHcxTnlJQnFXcDdiRHpLTUFBNzF3QXNxRDNaa2tWME9BUHBJUUh1Z1FZd0VpdnhCR21QVlh3dl8zd0JRIIEC; bili_jct=54ad5a0946f75ca5c3b86acf2ad4908e; sid=4j2e1f2f; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjIwOTgzNTcsImlhdCI6MTcyMTgzOTA5NywicGx0IjotMX0.LCb2FlVkFdh1iXrTQWIqed5zA5QdhKO7pHrPT8H5aJs; bili_ticket_expires=1722098297; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; bsource=search_bing; b_lsid=D4B10224A_190EA08DCB7; bp_t_offset_201491267=958102243326820352"
headers = {
        # Referer 防盗链 告诉服务器你请求链接是从哪里跳转过来的
        # "Referer": "https://www.bilibili.com/video/BV1454y187Er/",
        "Referer": url,
        # User-Agent 用户代理, 表示浏览器/设备基本身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Cookie": cookie
}
# 发送请求
response = requests.get(url=url, headers=headers)
html = response.text
print(html)
# 解析数据: 提取视频标题
title = re.findall('title="(.*?)"', html)[0]
print(title)
title='这世界那么多人'
# 提取视频信息
info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
# info -> json字符串转成json字典
json_data = json.loads(info)
# 提取视频链接
video_url = json_data['data']['dash']['video'][0]['baseUrl']
print(video_url)
# 提取音频链接
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
print(audio_url)
video_content = requests.get(url=video_url, headers=headers).content
# 获取音频内容
audio_content = requests.get(url=audio_url, headers=headers).content
# 保存数据
with open('file/'+title+'.mp4', mode='wb') as v:
    v.write(video_content)
with open('file/'+title+'.mp3', mode='wb') as a:
    a.write(audio_content)
