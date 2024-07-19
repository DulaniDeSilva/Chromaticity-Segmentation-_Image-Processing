# Chromaticity-Segmentation-_Image-Processing

Chromaticity segmentation: process of extracting objects from images using the chromaticity space of the RG channels. (Extracting objects from images by analyzing the color properties of the image, specially focusing on red and green channels). This method disregards the intensity/ brightness of the colors and only considers their proportions.
![image](https://github.com/user-attachments/assets/e2b2b074-5392-463e-b4dd-e3e0f9f4cf13)
Steps
1.	Compute RG chromaticity of the given image using the above equations
2.	Compute for the 2D histogram of the color values in the original image: it can be noticed what color or group of colors comprises the image: 
a.	Scatter plot shows which hues in the chromaticity space occur in the image.
b.	Bright values indicates that these are dominant hues in the image.
3.	Select a reference image patch: generate patch from the object of interest. 
4.	Compute for the RG chromaticity of the patch: 
5.	Compute 2D historgram of the color values/ patch -- upto now we have  got the chromaticity value of the concerned images. 
6.	Parametric segmentation: rely on assumption of a specific data distribution. Perform effectively when the data aligns with the assumed distribution and when prior knowledge about the objects to be segmented is available. They are computationally efficient and offer consice representations of the segmented regions.
    a.	Requires to fit a Gaussian distribution which will determine the pixels that belong to the color of interest.
    b.	Requires
      i.	Mean 
      ii.	Standard deviation calculated from the object of interest / reference patch
    c.	Then fed to the Gaussian distribution function.
     i.	Gaussian distribution in red channel 
    ii.	Gaussian distribution in green channel
    iii.	Multiply those tow get the actual segmentation based on the reference patch.
    iv.	It may appear that the red channel on its own appear to provide better segmentation but multiplication gives better results,
Using Gaussian distribution function, obtain the probability of color being part of image through both the R and G coordinates.
Use thresholding value to segment 


