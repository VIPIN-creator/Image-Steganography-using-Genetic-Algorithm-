import cv2
from copy import copy,deepcopy
import helper as h
import diretion_gene as d
import extraction as e
import  numpy as np
from PIL import Image
import random


# getting host image
img = cv2.imread("hostim.jpg", 0)

# getting secret image
sec_img=cv2.imread("secret2.png",0)
y_=deepcopy(img)
x_=deepcopy(sec_img)
# print(x_)
# converting to pixels
host=y_.tolist()
pix_secret=x_.tolist()
# print(pix_secret)
# converting decimal to binary
for i in range(len(pix_secret)):
    for j in range(len(pix_secret)):
        pix_secret[i][j]=bin(pix_secret[i][j]).replace("0b", "")

# converting to 8-bit pixels 
secret=[]
secret+=h.conversion_8bit(pix_secret)
# print(len(secret))

# getting the psnr of stego image
# psnr, stego = d.return_psnr(host,secret)


#initialize population
best=-100000
best_stego1 = []
best_stego2 = {}
populations = [[random.randint(0,1) for x in range(22)] for i in range(300)]
# print((populations))
parents=[]
best_population = []
# print(populations)


# fitness score calculation ............
def fitness_score():
    global populations, best, best_stego1, best_stego2, best_population
    fit_value = []
    fit_score = []
    all_stego = []
    for i in range(300):
        f, stego = d.return_psnr(host,secret, populations[i])
        fit_value.append(f)
        all_stego.append(list(stego))
        best_stego2[f] = stego
    # print(fit_value)
    fit_value, populations, all_stego = zip(*sorted(zip(fit_value, populations, all_stego) , reverse = True))
    best= fit_value[0]
    populations = list(populations)
    best_population = populations[0]
    best_stego1 = all_stego[0]


# fitness_score()
# print(len(all_stego), type(best_stego1))

# Tournmanet Selection
def tournament(population):
    candidate1 = population[random.randint(0, 299)]
    candidate2 = population[random.randint(0, 299)]
    while(candidate1 == candidate2):
        candidate2 = population[random.randint(0, 299)]

    f1, s1 = d.return_psnr(host, secret, candidate1)
    f2, s2 = d.return_psnr(host, secret, candidate2)
    if(f1>f2) : return  candidate1
    return  candidate2


def selectparent():
    global parents
    parents = []
    #global populations , parents
    for _ in range(150):
        child = tournament(populations)
        parents.append(child)
    # parents = populations[0:150]
    # print(len(parents))
# selectparent()
#
# #
def crossover():
    global parents

    cross_point = random.randint(0, 21)
    offsprings = []
    p_crossover = 0.7
    for j in range (75):
            if random.random() > p_crossover:
                offspring1 = parents[2*j]
                offspring2 = parents[2*j+1]
            else:
                offspring1 = parents[2*j][0:cross_point + 1] + parents[2*j+1][cross_point + 1:22]
                # for i in range (6):
                #     offspring1[i+16] = random.randint(0, 1)
                # print(type(offspring1))
                # parents = parents + tuple([offspring1])

                offspring2 = parents[2*j+1][0:cross_point + 1] + parents[2*j][cross_point + 1:22]
                # for i in range(6):
                #     offspring2[i + 16] = random.randint(0, 1)
            offsprings.append(offspring1)
            offsprings.append(offspring2)


    parents = parents + offsprings
    # print(len(parents), len(offsprings))

# crossover()
#
def mutation() :
    mutation_rate = 0.04
    global populations, parents

    if random.random() < mutation_rate :
        x=random.randint(0,299)
        y = random.randint(0,21)
        parents[x][y] = 1-parents[x][y]
    populations = parents
    # print(len(populations))
# mutation()
#
# # [1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0]
#
for i in range(10) :
    fitness_score()
    selectparent()
    crossover()
    mutation()
print("best score :")
print(best)
print("sequence........")
print(best_population)
# print("stego.........")
# print(best_stego1)
print(".....................")
# print(np.array(best_stego2[best]))

# if best_stego2[best] != best_stego1:
#     print(type(best_stego2[best]), type(best_stego1))

# # Extraction
new_secret = e.return_secret(best_stego2[best], best_population)
# if h.getValue(new_secret[0:8]) == h.getValue(new_secret[8*128: 8*128+8]):
#     print("YES")
# print(h.getValue(new_secret[0:8]), h.getValue(new_secret[8*128: 8*128+8]))
real_secret = np.array(h.convert_decimal(new_secret))
print(x_)
print(real_secret)
print(np.array_equal(x_,real_secret))
array = np.array(real_secret, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save("extracted_secret.png")

array = np.array(best_stego1, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save("stego.png")

# from matplotlib import pyplot as plt
# best_stego1 = np.array(best_stego1, dtype=np.uint8)
# histr = cv2.calcHist([best_stego1], [0], None, [256], [0, 256])
# #
# # # show the plotting graph of an image
# plt.plot(histr)
# plt.show()

