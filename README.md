# Dic-scraper
---

最简单的linux查词命令。

```
$> dic hello world
你好世界

```

```
$> dic hack
n. 砍，劈；出租马车
vt. 砍；出租
vi. 砍
n. (Hack)人名；(英、西、芬、阿拉伯、毛里求)哈克；(法)阿克
```

#Setup

- pip install requests BeautifulSoup4
- chmod a+x dic.py
- cp dic.py /usr/local/bin/dic


#Change Log
#0.1
- 实现有道词典英文单词(词组)翻译简单抓取


#关于我
- [我的博客](http://www.futantan.com)
- Email: [luckytantanfu@gmail.com](luckytantanfu@gmail.com)

#License
```
Copyright 2015 futantan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```