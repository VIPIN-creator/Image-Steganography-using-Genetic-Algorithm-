# 

<h1 align="center">Image-Steganography-using-Genetic-Algorithm 🎭</h1>

> Steganography is knowledge and art of hiding secret data into information which is largely used in information security systems. The purpose of a steganography algorithm is hiding a large amount of secret data into a meaningful host media such that the embedded secret data are concealed to prevent the attack of unauthorized persons. *The cover or host image* is referred as the original image without the embedded secret message, while the image that is obtained by embedding secret message into cover image without destroying the cover image is termed as *stego image*.

## Idea 
 The main idea of this technique is modeling the steganography problem as a search and optimization problem in which the purpose is finding the best direction and the best starting point in host image for hiding secret data such that the PSNR of the stego-image is maximized by using *Genetic Algoithm*.
Given below are some different scanning starting points in differnet directions.
 ![image](https://user-images.githubusercontent.com/59695863/169637275-13c85a99-5a73-4f25-8f00-3fae3042d27f.png)
 
 1. Chromosome Representation
 
| Gene name | Value range | Length | Description |
| ------------- | ------------- | ------------- | ------------- |
| Direction | 0–15 | 4 Bits | Direction of host image pixel scanning |
| X-offset | 0–255 | 8 Bits | X-offset of starting point |
| Y-offset | 0–255 | 8 Bits | Y-offset of starting point |
| SB-Pole | 0–1 |1 Bit | Pole of secret bits |
| SB-Dire | 0–1 |1 Bit | Direction of secret bits |

  - All the 16 different directions
  
   ![directions](https://user-images.githubusercontent.com/59695863/169637821-e6c879a0-72c7-495b-85dd-27486444a0bd.png)

  - Possible values for SB-Pole, SB-Dire and BP-Dire genes.

## Python Libraries 

```sh
OpenCv, numpy, Pillow, math, copy, random
```

## Author

👤 **Vipin Tripathi**

* LinkedIn: [@vipin-creator](https://linkedin.com/in/vipin-creator)

## Show your support

Give a ⭐️ if this project helped you!
Contributions are welcomed🤗


