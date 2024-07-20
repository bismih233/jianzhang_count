import requests
from openpyxl import Workbook

# 目标 URL 的基础部分
base_url = "https://workers.vrp.moe/api/bilibili/user-info/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

# 创建 Excel 工作簿和工作表
wb = Workbook()
ws = wb.active
ws.title = "User Info"

# 写入标题行

input_file = 'output.txt'

# 逐行读取输入文件
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        uid = line.strip()  # 去掉行末的换行符
        url = f'{base_url}{uid}'
        
        try:
            response = requests.get(url, headers=headers, timeout=60)  # 1分钟超时设置
            response.raise_for_status()  # 检查请求是否成功

            # 解析 JSON 响应
            data = response.json()
            
            # 提取 mid 和 current_level 信息
            mid = data.get("card", {}).get("mid", "N/A")
            current_level = data.get("card", {}).get("level_info", {}).get("current_level", "N/A")
            print(mid)
            print(current_level)
            # 写入数据行
            ws.append([mid, current_level])

        except requests.Timeout:
            print(f"请求超时，uid={uid}")
        except requests.RequestException as e:
            print(f"请求发生错误，uid={uid}: {e}")
        except ValueError:
            print(f"解析 JSON 响应时发生错误，uid={uid}")

# 保存 Excel 文件
wb.save("user_info.xlsx")
print("数据已写入 user_info.xlsx")
