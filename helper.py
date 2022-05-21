def conversion_8bit(pix):
    temp = []
    for i in range(128):
        for j in range(128):

            while (len(str((pix[i][j]))) != 8):
                pix[i][j] = "0" + str(pix[i][j])
            temp += pix[i][j]
    # print(len(temp))
    return temp

def getValue(arr) :
    res = int("".join(str(x) for x in arr), 2)
    return res


def convert_decimal(arr):
    temp = [[0]*128 for _ in range(128)]
    k = 0
    for i in range(128):
        for j in range(128):
            temp[i][j] = getValue(arr[k:k+8])
            k += 8
            # print(temp[i][j])
    # print(temp)
    # array = np.array(temp, dtype=np.uint8)
    # new_image = Image.fromarray(array)
    # new_image.save("rs.png")
    return  temp
