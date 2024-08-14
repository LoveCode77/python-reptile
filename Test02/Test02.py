# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入json模块
import json
# TODO 记得更改你要的url和你自己的cookie
url = 'https://www.bilibili.com/video/BV12E411A7ZQ/'
cookie = "i-wanna-go-back=-1; FEED_LIVE_VERSION=V8; buvid4=2EA18AE5-40BF-AFB6-4A95-5896BC7BC0DB08931-023062523-E6mdP7iVh21l5uM1h7Ta9Q%3D%3D; DedeUserID=201491267; DedeUserID__ckMd5=7c675d8f7bfcca20; rpdid=|(JYlmJY)RmR0J'uY)~~uklJm; CURRENT_FNVAL=16; is-2022-channel=1; LIVE_BUVID=AUTO4216930552081916; header_theme_version=CLOSE; enable_web_push=DISABLE; hit-dyn-v2=1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; PVID=1; CURRENT_QUALITY=0; buvid3=99F5835C-A516-25A6-965A-BDAB1170D87C03387infoc; b_nut=1719244703; _uuid=8B82DE10A-CA55-E7A6-5B5C-CA34237F1078F04181infoc; fingerprint=f3390ac900a6679d9b640ae96d757423; buvid_fp=f4d505333f9df3806992117a893e8340; home_feed_column=5; browser_resolution=1862-901; bp_t_offset_201491267=956167519473762304; b_lsid=21D6ECC10_190D112DD69; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE3NTM4MDIsImlhdCI6MTcyMTQ5NDU0MiwicGx0IjotMX0.WqF2rCEKScNVMk3YGz8V6CYJZzPIH9AAVVK88X8aJCI; bili_ticket_expires=1721753742; SESSDATA=f005abfb%2C1737047371%2C2748d%2A72CjBDM4LTBt7In2JP1XRX3pL5QOa_14-DhTsg3hJaaxW_mJv06CoCYoHTeSc-M3M5JoMSVlZMLTNBT2VTTXRhTC16c0ZJZDZ3dUR1TlN4V2xJaUR2aW1zSjZqU3djMmtZZGRIRUlWX25pTWRFRXFfY3JTR0FQbFVoLWhnbnZsMkdGYlotdEJvdUNRIIEC; bili_jct=5793dc255168d221bfbbca95d7bf48e5; sid=738x15ko"
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
with open( title + '.mp4', mode='wb') as v:
    v.write(video_content)
with open( title + '.mp3', mode='wb') as a:
    a.write(audio_content)
