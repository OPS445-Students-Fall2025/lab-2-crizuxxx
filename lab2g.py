#!/usr/bin/env python3 
#Author: Oji Onyedikachi Christopher
#Author ID: 133383224
#Date Created: 2025/09/25

import sys

timer = 3

if len(sys.argv) > 1:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print('blast off!')