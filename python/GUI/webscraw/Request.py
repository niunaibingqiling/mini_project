import requests
import os
if __name__ == '__main__':
    # 指定要爬的url
    url = 'https://wz.sun0769.com/political/index/politicsNewest'
    # 发起请求
    response = requests.get(url=url)

    # 获取响应数据
    print(dir(response))
    print(f'{response.text = }')
    print(f'{response.status_code = }')

    # 写入文件
    with open('./sogou.html','w') as f:
        f.write(response.text)
    