import requests
import os

path = f'{os.getcwd()}/data'

if not os.path.exists(path):
    os.makedirs(path)

name=input('이름>')

url =f'https://www.google.com/search?sca_esv=5d812c3a7137edf1&udm=2&fbs=AIIjpHyDg0Pef0CibV20xjIa-FRejxCuOmkq074km2sZXr7uq1p1X9bxXgjHLQK32SkzhUQ4QccZJzUGp6HJd5RiCMO4jDTfs_-W3JbTmf4FOSk_x-Z_-2AgoBIU_TZi7PJ3nFu_FpTJPcuJaxeemUemuJje05ZbjollhdcMxu0JkclO0hJjk-S0ZJRp5YtlVPbdLED0AuWZrqPneRit01TR2WDIfLfUuIAzLHxWOu9dHD4WWes2jlE&q={name}&sa=X&ved=2ahUKEwi14_2067iPAxXks1YBHbCdPMUQtKgLegQIEhAB&biw=1536&bih=730&dpr=1.25'
res = requests.get(url)


file_name = f'data/{name}.html'
with open(file_name, 'w', encoding='utf-8')as file:
    file.write(res.text)