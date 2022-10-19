## Histogram equalisation

>ORIGINAL IMAGE

![ORIGINAL IMAGE](https://github.com/arkapg211002/CSE_3RD_SEM_IT_LAB_PYTHON/blob/main/histogram_equalisation/image.jpg)

```python
'''
Question 1
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
inputimg='image.jpg'
grayimg=cv2.imread(inputimg,cv2.IMREAD_GRAYSCALE)
cv2.imshow('Gray',grayimg)
hist,bins=np.histogram(grayimg,256,[0,256])
plt.hist(grayimg.ravel(),256,[0,256])
plt.title('Gray')
plt.show()
while True:
    k=cv2.waitKey(0) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
```

>Histogram

![ORIGINAL HISTOGRAM](https://github.com/arkapg211002/CSE_3RD_SEM_IT_LAB_PYTHON/blob/main/histogram_equalisation/2022-10-19%20(3).png)

```python
'''Question 2'''
import cv2
import numpy
from matplotlib import pyplot as plt
inputImg = 'image.jpg'
img = cv2.imread(inputImg)
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, 
cv2.COLOR_YUV2BGR)
outputImg = 'result.jpg'
cv2.imwrite(outputImg, hist_equalization_result)
outputimg=cv2.imread(outputImg)
cv2.imshow('Gray',outputimg)
hist,bins=numpy.histogram(outputimg,256,[0,256])
plt.hist(outputimg.ravel(),256,[0,256])
plt.title('Enhanced')
plt.show()
while True:
    k=cv2.waitKey(0) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
```

>Enhanced Image

![Enhaned Image](https://github.com/arkapg211002/CSE_3RD_SEM_IT_LAB_PYTHON/blob/main/histogram_equalisation/result.jpg)

>New Histogram

![New Histogram](https://github.com/arkapg211002/CSE_3RD_SEM_IT_LAB_PYTHON/blob/main/histogram_equalisation/2022-10-19%20(5).png)
