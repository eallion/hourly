import requests
import json
import os

APIs = [
    "https://api.hourly.top/36kr?limit=1&cache=true",
    "https://api.hourly.top/acfun?limit=1&cache=true",
    "https://api.hourly.top/baidu?limit=1&cache=true",
    "https://api.hourly.top/bilibili?limit=1&cache=true",
    "https://api.hourly.top/douyin?limit=1&cache=true",
    "https://api.hourly.top/hellogithub?limit=1&cache=true",
    "https://api.hourly.top/hupu?limit=1&cache=true",
    "https://api.hourly.top/huxiu?limit=1&cache=true",
    "https://api.hourly.top/ifanr?limit=1&cache=true",
    "https://api.hourly.top/ithome?limit=1&cache=true",
    "https://api.hourly.top/netease-news?limit=1&cache=true",
    "https://api.hourly.top/ngabbs?limit=1&cache=true",
    "https://api.hourly.top/qq-news?limit=1&cache=true",
    "https://api.hourly.top/sina?limit=1&cache=true",
    "https://api.hourly.top/sina-news?limit=1&cache=true",
    "https://api.hourly.top/sspai?limit=1&cache=true",
    "https://api.hourly.top/thepaper?limit=1&cache=true",
    "https://api.hourly.top/tieba?limit=1&cache=true",
    "https://api.hourly.top/toutiao?limit=1&cache=true",
    "https://api.hourly.top/v2ex?limit=1&cache=true",
    "https://api.hourly.top/weibo?limit=1&cache=true",
    "https://api.hourly.top/weread?limit=1&cache=true",
    "https://api.hourly.top/zhihu?limit=1&cache=true",
    "https://api.hourly.top/zhihu-daily?limit=1&cache=true"
]

def fetch_data(api):
    try:
        response = requests.get(api)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def process_data(data, source):
    if data and 'data' in data and 'title' in data:
        for item in data['data']:
            item['source'] = data['title']
            if 'hot' not in item:
                item['hot'] = null
        return data['data']
    return []

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    all_data = []
    for api in APIs:
        data = fetch_data(api)
        if data:
            source = api.split('/')[-1].split('?')[0]
            processed_data = process_data(data, source)
            save_data(data, f"{source}.json")
            all_data.extend(processed_data)

    # 处理没有 'hot' 字段的情况
    all_data.sort(key=lambda x: (x['hot'] is not None, x['hot']), reverse=True)
    save_data(all_data, 'total.json')

if __name__ == "__main__":
    main()
