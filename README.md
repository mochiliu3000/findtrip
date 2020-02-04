# Findtrip Help Doc

## Fork from 
https://github.com/fankcoder/findtrip.git

## Setup
```
npm install phantomjs@2.1.1 --registry=http://registry.npm.taobao.org/ --disturl=https://npm.taobao.org/dist

export PATH=${PATH}:<path-to-phantomjs>/phantomjs/bin

which phantomjs

pip install scrapy==1.0 requests==2.4.3 selenium==2.52.0 lxml==3.4.2 --index https://pypi.douban.com/simple/ --index https://pypi.tuna.tsinghua.edu.cn/simple
```
## Config
Edit line 10 in findtrip/spiders/alone/Ctrip.py: <br>
http://flights.ctrip.com/international/search/oneway-bjs-puq?depdate=2020-02-05

## Run
```
scrapy crawl Ctrip
scrapy crawl Qua
```
