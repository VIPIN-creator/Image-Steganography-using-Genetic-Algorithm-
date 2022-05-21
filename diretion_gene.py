import math
import numpy as np
import copy
from PIL import Image

def zero(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while total != 0:
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        y_offset += 1
        if y_offset == 256:
            x_offset -= 1
            if x_offset == -1 and y_offset == 256:
                x_offset = 255
            y_offset = 0
        l += 2
        total -= 1
    return host, mse

def one(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        x_offset += 1
        if x_offset == 256:
            y_offset -= 1
            if y_offset == -1 and x_offset == 256:
                y_offset = 255
            x_offset = 0
        l += 2
        total -= 1
    return host, mse

def two(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)

        y_offset -= 1
        if y_offset == -1:
            x_offset +=1
            if x_offset == 256 and y_offset == -1:
                x_offset = 0
            y_offset = 255
        l += 2
        total -= 1
    return host, mse

def three(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        x_offset -= 1
        if x_offset == -1:
            y_offset += 1
            if y_offset == 256 and x_offset == -1:
                y_offset = 0
            x_offset = 255
        l += 2
        total -= 1
    return host, mse

def four(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        y_offset += 1
        if y_offset == 256:
            x_offset += 1
            if y_offset == 256 and x_offset == 256:
                x_offset = 0
            y_offset = 0
        l += 2
        total -= 1
    return host, mse

def five(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        x_offset += 1
        if x_offset == 256:
            y_offset += 1
            if y_offset == 256 and x_offset == 256:
                y_offset = 0
            x_offset = 0
        l += 2
        total -= 1
    return host, mse

def six(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        y_offset -= 1
        if y_offset == -1:
            x_offset -= 1
            if y_offset == -1 and x_offset == -1:
                x_offset = 255
            y_offset = 255
        l += 2
        total -= 1
    return host, mse

def seven(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        x_offset -= 1
        if x_offset == -1:
            y_offset -= 1
            if y_offset == -1 and x_offset == -1:
                y_offset = 255
            x_offset = 255
        l += 2
        total -= 1
    return host, mse

def eight(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        if x_offset % 2 == 0:
            y_offset += 1
            if y_offset == 256:
                x_offset += 1
                y_offset = 255
        else:
            y_offset -= 1
            if y_offset == -1:
                x_offset += 1
                if x_offset == 256:
                    x_offset = 0
                y_offset = 0
        l += 2
        total -= 1
    return host, mse

def nine(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        if y_offset % 2 == 0:
            x_offset += 1
            if x_offset == 256:
                y_offset -= 1
                if y_offset == -1:
                   y_offset = 255
                x_offset=255
        else:
            x_offset -= 1
            if x_offset == -1:
                y_offset -= 1
                x_offset = 0
        l += 2
        total -= 1
    return host, mse

def ten(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        # print(mse)
        if x_offset % 2 == 0:
            y_offset -= 1
            if y_offset == -1:
                y_offset = 0
                x_offset -= 1
                if x_offset == -1:
                    x_offset = 255
        else:
            y_offset += 1
            if y_offset == 256:
                y_offset = 255
                x_offset -= 1
        l += 2
        total -= 1
    return host, mse

def eleven(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        # print(mse)
        if y_offset%2 == 0:
            x_offset-=1
            if x_offset == -1:
                x_offset = 0
                y_offset += 1
        else:
            x_offset+=1
            if x_offset == 256:
                x_offset = 255
                y_offset += 1
                if y_offset == 256:
                    y_offset = 0
        l += 2
        total -= 1
    return host, mse

def twelve(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        # print(mse)
        if y_offset % 2 == 0:
            x_offset -= 1
            if x_offset == -1:
                x_offset = 0
                y_offset -= 1
                if y_offset == -1:
                    y_offset = 255
        else:
            x_offset += 1
            if x_offset == 256:
                x_offset = 255
                y_offset -= 1
        l += 2
        total -= 1
    return host, mse

def thirteen(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        # print(mse)
        if x_offset % 2 == 0:
            y_offset += 1
            if y_offset == 256:
                y_offset = 255
                x_offset -= 1
                if x_offset == -1:
                    x_offset = 255
        else:
            y_offset -= 1
            if y_offset == -1:
                y_offset = 0
                x_offset -= 1

        l += 2
        total -= 1
    return host, mse

def fourteen(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        if y_offset % 2 == 0:
            x_offset += 1
            if x_offset == 256:
                x_offset = 255
                y_offset += 1
        else:
            x_offset -= 1
            if x_offset == -1:
                x_offset =  0
                y_offset += 1
                if y_offset == 256:
                    y_offset = 0
        l += 2
        total -= 1
    return host, mse

def fifteen(x_offset, y_offset, host, secret):
    mse = 0
    val = 0
    l = 0
    prev = 0
    total = 256 * 256
    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = host[x_offset][y_offset]
        host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        mse += ((prev - host[x_offset][y_offset]) ** 2)
        if x_offset%2 == 0:
            y_offset-=1
            if y_offset == -1:
                y_offset = 0
                x_offset+=1
        else:
            y_offset+=1
            if y_offset == 256:
                y_offset = 255
                x_offset+=1
                if x_offset == 256:
                    x_offset = 0
        l += 2
        total -= 1
    return host, mse

switcher = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve,
        13: thirteen,
        14: fourteen,
        15: fifteen
    }

def raster_order(dir_input, x_offset, y_offset, host, secret):
    func = switcher[dir_input](x_offset, y_offset, host, secret)
    return func

def getValue(arr) :
    res = int("".join(str(x) for x in arr), 2)
    return res

def return_psnr(pix, secret, population):
    temp_pix = copy.deepcopy(pix)
    temp_secret = copy.deepcopy(secret)
    x_offset = getValue(population[14:22])
    y_offset = getValue(population[6:14])
    direction = getValue(population[2:6])
    sb_pole = getValue(population[1:2])
    sb_dir = getValue(population[0:1])

    if(sb_pole):
        for i in range(len(temp_secret)):
            if temp_secret[i] == '0':
                temp_secret[i] = '1'
            else:
                temp_secret[i] = '0'


    if(sb_dir):
        temp_secret.reverse()

    # calculating psnr
    stego, mse = raster_order(direction, x_offset, y_offset, temp_pix, temp_secret)
    # print(mse)
    mse = mse / (256 * 256)
    psnr = 10 * math.log10((255 * 255) / mse)
    return  psnr, stego
