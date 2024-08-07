import json
from datetime import datetime, timedelta

# 读取 total.json 文件
with open('total.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 获取当前时间并加上8个小时
current_time = (datetime.now() + timedelta(hours=8)).strftime('%H:00')
current_date= (datetime.now() + timedelta(hours=8)).strftime(' %b %d, %Y')

# 格式化数据
formatted_text = f"<b>头条一小时 {current_time}</b>{current_date}\n\n"
for item in data:
    title = item.get('title', '').replace('[', '\\[').replace(']', '\\]').replace('_', '\\_')
    url = item.get('url', '')
    hot = item.get('hot', 'null')
    source = item.get('source', '未知来源')
    formatted_text += f"•【{source}】<a href=\"{url}\">{title}</a> 🔥<i>{hot}</i>\n"

# 输出格式化后的文本
print(formatted_text)
