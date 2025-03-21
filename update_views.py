#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# 读取文件
with open('navi/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换所有的 u"字符串" 为 "字符串"
content = re.sub(r'u"([^"]*)"', r'"\1"', content)

# 写回文件
with open('navi/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Views.py updated successfully!')
