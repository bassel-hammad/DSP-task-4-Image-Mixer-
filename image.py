# image_class.py

from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import numpy as np

class Image:
    def __init__(self, path):
        self.path = path
        self.original_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.processed_image = self.original_image.copy()
        self.size = self.original_image.shape[:2]  # (height, width)

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
