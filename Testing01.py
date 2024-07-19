import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("7.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Take a variety of photographs of people and calculate the xy chromaticity values for
# each pixel.

# calculating RG chromaticity using equations
image_R = image_rgb[:,:,0]*1.0/image_rgb.sum(axis =2)
image_G = image_rgb[:,:,1]*1.0/image_rgb.sum(axis =2)



#Crop the photos or otherwise indicate with a painting tool which pixels are likely to be
# skin (e.g. face and arms)
patch = image_rgb[175:210, 150:170]



# Calculate a color (chromaticity) distribution for these pixels. You can use something as
# simple as a mean and covariance measure or as complicated as a mean-shift 
# segmentation algorithm (see Section 5.3.2). You can optionally use non-skin pixels to 
# model the background distribution.

# getting RG chroaticity for patch
patch_R = patch[:,:,0]*1.0/patch.sum(axis =2)
patch_G = patch[:,:,1]*1.0/patch.sum(axis= 2)

# mean and covariance measure OR mean_shift_segmentation 
std_patch_R = np.std(patch_R.flatten())
mean_patch_R = np.mean(patch_R.flatten())

std_patch_G = np.std(patch_G.flatten())
mean_patch_G = np.mean(patch_G.flatten())

cov_matrix = np.cov(patch_R.flatten(), patch_G.flatten())

# estimate bandwidth for mean shift clustering
# flat_patch = np.column_stack((patch_R.flatten(),patch_G.flatten()) )
# bandwidth = estimate_bandwidth(flat_patch, quantile=0.06, n_samples=3000)
# ms = MeanShift(bandwidth = bandwidth, bin_seeding=True)
# ms.fit(flat_patch)
# ??????????????????????????????????????????


# parametric segmentation: fit gaussian probability distribution using mask

def gaussian(p, mean, std):
    return np.exp(-(p-mean)**2/(2*std**2))*(1/(std*((2*np.pi)**0.5)))

x = np.linspace(0,1)
y = gaussian(x, mean_patch_R, std_patch_R)
# plt.plot(x,y)

prob_R = gaussian(image_R, mean_patch_R, std_patch_R)

prob_G = gaussian(image_G, mean_patch_G, std_patch_G)

prob = prob_R * prob_G

threshold = 3


# /////////////////////////
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)

plt.subplot(2, 2, 2)
plt.scatter(image_R.flatten(), image_G.flatten())
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title("Original Image chromaticity ")

plt.subplot(2, 2, 3)
plt.title("Skin Patch cropped")
plt.imshow(patch)

plt.subplot(2, 2, 4)
plt.scatter(patch_R.flatten(), patch_G.flatten())
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title("distribution of choromaticity in patch")

plt.figure(figsize=(20, 8))
plt.subplot(1, 5, 1)
plt.title("Original Image")
plt.axis("off")
plt.imshow(image_rgb)

plt.subplot(1, 5, 2)
plt.title("Prob_R")
plt.axis("off")
plt.imshow(prob_R)

plt.subplot(1, 5, 3)
plt.title("Prob_G")
plt.axis("off")
plt.imshow(prob_G)

plt.subplot(1, 5, 4)
plt.title("Prob_R*Prob_G")
plt.axis("off")
plt.imshow(prob)

plt.subplot(1, 5, 5)
plt.title("Prob threshold")
plt.axis("off")
plt.imshow(prob>threshold, "gray")


plt.show()
