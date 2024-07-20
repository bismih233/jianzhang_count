import requests

base_url = "https://workers.vrp.moe/api/bilibili/live-guards/1660392980"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# 创建或清空文件
with open("1.txt", "w", encoding="utf-8") as file:
    file.write("")

# 请求每一页并保存响应内容
for page in range(1, 335):
    url = f"{base_url}?p={page}"
    try:
        response = requests.get(url, headers=headers, timeout=60)  # 1分钟超时设置
        response.raise_for_status()  # 检查请求是否成功

        # 追加响应内容到文件
        with open("1.txt", "a", encoding="utf-8") as file:
            file.write(response.text + "\n\n")

        print(f"页面 {page} 的内容已保存")

    except requests.Timeout:
        print(f"请求页面 {page} 超时")
    except requests.RequestException as e:
        print(f"请求页面 {page} 发生错误: {e}")
