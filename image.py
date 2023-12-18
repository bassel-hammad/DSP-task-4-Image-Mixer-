# image_class.py

from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
class Image:
    def __init__(self, path):
        self.path = path
        self.original_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.processed_image = self.original_image.copy()
        self.size = self.original_image.shape[:2]  # (height, width)

        #compute image fft (mag,phase,reaal,img)
        self.image_fft=self.apply_fourier_transform()
        self.fft_magnitude=self.get_magnitude(self.image_fft)
        self.fft_phase=self.get_magnitude(self.image_fft)
        self.fft_real=self.get_real_component(self.image_fft)
        self.fft_img=self.get_imaginary_component(self.image_fft)

        #CANVAS  FOR  PLOTTING SELECTED COMPONENT OF FFT
        self.fig = Figure(figsize=(3, 3), dpi=100)
        self.canvas_component = FigureCanvas(self.fig)
        fig = Figure(figsize=(3, 3), dpi=100)
        self.axes_component = fig.add_subplot(111)

    def apply_fourier_transform(self):
        # Apply Fourier transform to the image
        fft_image = np.fft.fft2(self.processed_image)
        return fft_image

    def get_magnitude(self, fft_image):
        # Compute the magnitude spectrum
        magnitude_spectrum = np.abs(fft_image)
        return magnitude_spectrum

    def get_phase(self, fft_image):
        # Compute the phase spectrum
        phase_spectrum = np.angle(fft_image)
        return phase_spectrum

    def get_real_component(self, fft_image):
        # Compute the real component of the Fourier transform
        real_component = fft_image.real
        return real_component

    def get_imaginary_component(self, fft_image):
        # Compute the imaginary component of the Fourier transform
        imaginary_component = fft_image.imag
        return imaginary_component

    def apply_inverse_fourier_transform(self, fft_image):
        # Apply inverse Fourier transform to obtain the processed image
        processed_image = np.fft.ifft2(fft_image).real
        return processed_image
    
    #pass the canvas for plotting the  selected component to image class
    def set_component_viewer(self,axes_component,canvas_component):
        self.axes_component=axes_component
        self.canvas_component=canvas_component
        self.canvas_component.draw()

    def select_plotted_component(self , component=""):
        if(component=="Magnitude"):
            # Shift the zero-frequency component to the center of the spectrum
            fourier_shift = np.fft.fftshift(self.image_fft)
            # calculate the magnitude of the Fourier Transform
            magnitude_spectrum = 20 * np.log(np.abs(fourier_shift))
            self.axes_component.imshow(magnitude_spectrum, cmap='gray')
            self.axes_component.title('Magnitude Spectrum')
            self.axes_component.axis('off')
            self.axes_component.show()



