import os
from urllib import request,error
import requests
from aiohttp import ClientSession
import asyncio
import time
a = time.time()
async def run_proc(url,imagename,sp):
    async with sp:
        imagepath = os.path.join(image_dir+ os.sep + imagename)
        async with ClientSession() as session:
            async with session.get(url=url) as response:
                response = await response.read()
                with open(imagepath, 'wb') as f:
                    f.write(response)
                    print('save %s to %s sussfully'%(imagename,imagepath))
def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        print(path+' 创建成功')
        return True
    else:
        print(path+' 目录已存在')
        return False

image_dir =  os.path.join(os.getcwd()+os.sep+'images')
mkdir(image_dir)
images= []
image_names=[]
i=0
with open(r'resources.txt','r') as f:
        for path in f:
            url = path
            images.append(url)
            image_name = str(i).zfill(4)+ '.jpg'
            image_names.append(image_name)
            i=i+1
    
print(i)#总共多少个任务
async def run():
    # 多核并行 16
    semaphore = asyncio.Semaphore(16)
    to_get = [run_proc(images[index],image_names[index],semaphore) for index in range(0,i)] 
    await asyncio.wait(to_get)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    b = time.time()
    print(b-a)