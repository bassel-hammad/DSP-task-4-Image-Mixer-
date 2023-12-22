# image_class.py

from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
from PyQt5.QtGui import QPixmap as qtg
import numpy as np
import matplotlib.pyplot as plt

class Image:
    def __init__(self, path):
        self.path = path
        self.image_data = plt.imread(self.path)
        self.image_data =self.image_data[:,:,0]
        self.original_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.processed_image = self.original_image.copy()
        self.size = self.original_image.shape[:2]  # (height, width)
        ##FFT COMPONENTS
        self.fft = np.fft.fft2(self.image_data)
        self.magnitude = np.abs(self.fft)
        self.phase = np.angle(self.fft)
        self.real = np.real(self.fft)
        self.imaginary = np.imag(self.fft)

        self.components = {
            '':'',
            'Magnitude':self.magnitude,
            'Phase':self.phase,
            'Real':self.real,
            'Imaginary': self.imaginary,
        }
    def get_tab_number(self):
        return self.tab_number

    def get_component(self, type: str, ratio: float) -> np.ndarray:
        if type == "Magnitude":
            return self.components[type] 
        elif type == "Phase":
            return  self.components[type] 
        elif type == "Real":
            return self.components[type] 
        elif type == "Imaginary":
            return  self.components[type] 
        elif type =="Uniform Magnitude" :
            return np.ones(shape=self.shape) * ratio
        elif type == "Uniform Phase":
            return np.exp(1j * np.zeros(shape=self.shape) * ratio)

    def apply_inverse_fourier_transform(self):
        # Apply inverse Fourier transform to obtain the processed image
        processed_image = np.fft.ifft2(self).real
        return processed_image
    
    def mix(*images, types, ratios, mode):
        if len(images) < 2:
            raise ValueError("At least two images are required for mixing.")

        components = [image.get_component(type_, ratio) for image, type_, ratio in zip(images, types, ratios)]

        if mode == 'mag-phase':
            construct = np.real(np.fft.ifft2(np.prod(components)))
        elif mode == 'real-imag':
            construct = np.real(np.fft.ifft2(sum(components)))
        else:
            raise ValueError("Invalid mode. Supported modes: 'mag-phase', 'real-imag'.")

        if np.max(construct) > 1.0:
            construct /= np.max(construct)

        plt.imsave('test.png', np.abs(construct))
        return qtg('test.png')

    def resize(self, desired_size):
        if self.processed_image is not None and self.processed_image.shape[0] > 0 and self.processed_image.shape[1] > 0:
            resized_image = cv2.resize(self.processed_image, (desired_size[1], desired_size[0]))
            return resized_image

    def to_image_object(self, data):
        # Create a new Image instance from the given data
        img = Image(self.path)
        img.processed_image = data
        return img
    
    def get_component_images(self, type: str,):
            component = self.get_component(type,1)
            component_image = self.to_image_object(component)
            return component_image

    
    def is_imaginary_component_of(self, other_image):   # Resize images to a common size
        target_size = (max(self.original_image.shape[0], other_image.original_image.shape[0]),
                    max(self.original_image.shape[1], other_image.original_image.shape[1]))

        resized_self = cv2.resize(self.original_image, target_size)
        resized_other = cv2.resize(other_image.original_image, target_size)

        # Apply Fourier transform to the resized images
        fft_image_self = np.fft.fft2(resized_self)
        fft_image_other = np.fft.fft2(resized_other)

        # Extract the imaginary component
        imaginary_self = np.fft.fftshift(fft_image_self).imag
        imaginary_other = np.fft.fftshift(fft_image_other).imag

        # You may want to use a suitable comparison method based on your needs
        return np.array_equal(imaginary_self, imaginary_other)
    




    def mix_and_reconstruct(mode,components_p_1,image_1,components_p_2,image_2,components_p_3,image_3,components_p_4,image_4):
        denominator_for_comp_1 =components_p_1[0]+components_p_2[0]+components_p_3[0]+components_p_4[0]
        ratio__for_comp_1=[x//denominator_for_comp_1 for x in [components_p_1[0] , components_p_2 [0], components_p_3 [0], components_p_4[0]]]
        denominator_for_comp_2 =components_p_1[1]+components_p_2[1]+components_p_3[1]+components_p_4[1]
        ratio__for_comp_2=[x//denominator_for_comp_2 for x in [components_p_1[1] , components_p_2 [1], components_p_3 [1], components_p_4[1]]]

        if(mode=="real-imag"):
            real_part=ratio__for_comp_1[0]*image_1.real + ratio__for_comp_1[1]*image_2.real  + ratio__for_comp_1[2]*image_3.real + ratio__for_comp_1[3]*image_4.real
            imag_part=ratio__for_comp_2[0]*image_1.imaginary + ratio__for_comp_2[1]*image_2.imaginary  + ratio__for_comp_2[2]*image_3.imaginary + ratio__for_comp_2[3]*image_4.imaginary
            img_fft=real_part+ 1j *(imag_part)
            img_fftshift = np.fft.fftshift(img_fft)
            img_ifftshit = np.fft.ifftshift(img_fftshift)
            reconstrucuted_image = np.fft.ifft2(img_ifftshit)
            #self.axes_component.imshow(np.abs(reconstrucuted_image), cmap="gray")
        else:
            magnitude=ratio__for_comp_1[0]*image_1.magnitude + ratio__for_comp_1[1]*image_2.magnitude  + ratio__for_comp_1[2]*image_3.magnitude + ratio__for_comp_1[3]*image_4.magnitude
            phase=ratio__for_comp_2[0]*image_1.phase + ratio__for_comp_2[1]*image_2.phase  + ratio__for_comp_2[2]*image_3.phase + ratio__for_comp_2[3]*image_4.phase
            img_fft=magnitude * np.exp(1j * phase)
            reconstrucuted_image=np.fft.ifft2(img_fft)
            #self.axes_component.imshow(np.abs(reconstrucuted_image), cmap="gray")
            



