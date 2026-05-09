import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import color, io

class Prob4():
    def __init__(self):
        """Load input color image indoor.png and outdoor.png here as class variables."""

        self.indoor = None
        self.outdoor = None
        ###### START CODE HERE ######
        self.indoor = io.imread(r"C:\Users\julia\OneDrive\Documentos\College\Fall 2025\Intro Comp Vision\PS1\PS1-release\indoor.png")
        self.outdoor = io.imread(r"C:\Users\julia\OneDrive\Documentos\College\Fall 2025\Intro Comp Vision\PS1\PS1-release\outdoor.png")
        ###### EnD CODE HERE ######

    
    def prob_4_1(self):
        """Plot R,G,B channels separately and also their corresponding LAB space channels separately for both the indoor and outdoor image.
           Use the "gray" colormap options for plotting each channel."""
        
        ###### START CODE HERE ######
        images = {"Indoor": self.indoor, "Outdoor": self.outdoor}
        figure, axes = plt.subplots(2, 6, figsize = (18, 6))

        for row, (name, img) in enumerate(images.items()):
            if img.shape[2] > 3:
                img = img[:, :, :3]

            r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
            l_img = color.rgb2lab(img)
            L, A, B = l_img[:, :, 0], l_img[:, :, 1], l_img[:, :, 2]

            axes[row, 0].imshow(r, cmap = "gray")
            axes[row, 0].set_title(f"{name} -> Red")
            axes[row, 0].axis("off")

            axes[row, 1].imshow(g, cmap = "gray")
            axes[row, 1].set_title(f"{name} -> Green")
            axes[row, 1].axis("off")

            axes[row, 2].imshow(b, cmap = "gray")
            axes[row, 2].set_title(f"{name} -> Blue")
            axes[row, 2].axis("off")

            axes[row, 3].imshow(L, cmap = "gray")
            axes[row, 3].set_title(f"{name} -> L")
            axes[row, 3].axis("off")

            axes[row, 4].imshow(A, cmap = "gray")
            axes[row, 4].set_title(f"{name} -> A")
            axes[row, 4].axis("off")

            axes[row, 5].imshow(B, cmap = "gray")
            axes[row, 5].set_title(f"{name} -> B")
            axes[row, 5].axis("off")

        plt.tight_layout()
        plt.show()

        ###### EnD CODE HERE ######
        return

    def prob_4_2(self):
        """
        Convert the loaded RGB image to HSV and return HSV matrix without using inbuilt functions. Return the HSV image as HSV. Plot the HSV image.
        Make sure to use a 3 channeled RGB image with floating point values lying between 0 - 1 for the conversion to HSV.

        Returns:
            HSV image (3 channeled image of size H x W x 3 with floating point values lying between 0 - 1 in each channel)
        """
        
        HSV = None
        ###### START CODE HERE ######
        img = io.imread("inputPS1Q4.jpg")
        img = img.astype(float) / 255.0
        height, width, _ = img.shape
        HSV = np.zeros_like(img, dtype = float)

        for i in range(height):
            for j in range(width):
                R, G, B = img[i, j]

                V = max(R, G, B)
                m = min(R, G, B)
                C = V - m

                if V == 0:
                    S = 0
                else:
                    S = C/V

                if C == 0:
                    H = 0
                elif V == R:
                    H = ((G - B)/C) % 6
                elif V == G:
                    H = ((B - R)/C) + 2
                else:
                    H = ((R - G)/C) + 4
            
                H = H/6
                HSV[i, j] = [H, S, V]

        plt.imshow(HSV)
        plt.title("RGB to HSV")
        plt.axis("off")
        plt.show()
        ###### EnD CODE HERE ######
        return HSV

        
if __name__ == '__main__':
    
    p4 = Prob4()
    p4.prob_4_1()
    HSV = p4.prob_4_2()





