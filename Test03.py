# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入json模块
import json
# TODO 记得更改你要的url和你自己的cookie
url = 'https://console.nuoyun.tv/Watch/156057834'
cookie = "_bl_uid=t1lnkydLrIec337d08Fk876ykzmj; NYSSID=7egofcqpt6ipjnmbb6s2m4f415; appid=156057834; unstable=off; WSTOKEN=7egofcqpt6ipjnmbb6s2m4f415; sign_need_login=no; is_master="
headers = {
        # Referer 防盗链 告诉服务器你请求链接是从哪里跳转过来的
        # "Referer": "https://www.bilibili.com/video/BV1454y187Er/",
        "Referer": url,
        # User-Agent 用户代理, 表示浏览器/设备基本身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
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


# video_content = requests.get(url=video_url, headers=headers).content
# # 获取音频内容
# audio_content = requests.get(url=audio_url, headers=headers).content
# # 保存数据
# with open( title + '.mp4', mode='wb') as v:
#     v.write(video_content)
# with open( title + '.mp3', mode='wb') as a:
#     a.write(audio_content)
