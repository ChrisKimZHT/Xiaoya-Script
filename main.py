import requests

token = input("请输入 token: ")
headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
data = {
    "video_id": "awa",
    "played": 1000,
    "media_type": 1,
    "duration": 1000,
    "watched_duration": 1000
}

while True:
    node_id = input("请输入 node_id: ")
    resource_url = f"https://whut.ai-augmented.com/api/jx-iresource/resource/queryResource?node_id={node_id}"
    resource_resp = requests.get(url=resource_url, headers=headers).json()
    quote_id = resource_resp["data"]["quote_id"]
    url = f"https://whut.ai-augmented.com/api/jx-iresource/vod/duration/{quote_id}"
    result = requests.post(url=url, headers=headers, json=data)
    print(f"resp status: {result.status_code}\n")
