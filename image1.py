import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PIL import ImageEnhance
from PIL import Image as PilImage
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



class ImageViewer:
    def __init__(self,imagelabel1, imagelabel2,path):
        self.path = path

        # Initialize variables
        self.image = None
        self.adjustedimage = None

        self.image_label = imagelabel1
        self.ft_label = imagelabel2
        self.load_image()
        f_transform = np.fft.fft2(self.image)
        f_transform_shifted = np.fft.fftshift(f_transform)
        # Display the selected FT component
        self.magnitude = np.abs(f_transform_shifted)
        magnitude_normalized = cv2.normalize(self.magnitude, None, 0, 255, cv2.NORM_MINMAX)

        self.phase = np.angle(f_transform_shifted)
        phase_normalized = cv2.normalize(self.phase, None, 0, 255, cv2.NORM_MINMAX)

        self.real_part = np.real(f_transform_shifted)
        real_normalized = cv2.normalize(self.real_part, None, 0, 255, cv2.NORM_MINMAX)

        self.imaginary_part = np.imag(f_transform_shifted)
        imaginary_normalized = cv2.normalize(self.imaginary_part, None, 0, 255, cv2.NORM_MINMAX)
        

        self.ft_components = ["Magnitude", "FT Phase", "FT Real", "FT Imaginary"]
        self.orgcomponents = {
            '':'',
            'Magnitude':self.magnitude,
            'Phase':self.phase,
            'Real':self.real_part,
            'Imaginary':self.imaginary_part,
        }
        self.components = {
            '':'',
            'Magnitude':magnitude_normalized,
            'Phase':phase_normalized,
            'Real':real_normalized,
            'Imaginary':imaginary_normalized,
        }
        self.show_image()
        self.show_ft_component("Magnitude")
        self.recover_image("ri")
        
        
    def getorgcomponents(self,text):
        return self.orgcomponents[text]
        
    def load_image(self):
        
        if self.path:
            # Read the image using OpenCV
            original_image = cv2.imread(self.path)
            self.image =original_image
            if original_image is not None:
                # Convert to grayscale
                gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

                # Resize to the smallest size
                min_size = min(original_image.shape[:2])
                resized_image = cv2.resize(gray_image, (271, 221))

                # Update the image and display it
                self.image = resized_image
                self.adjustedimage = resized_image
                
                

    def show_image(self):
        desired_size = (271, 221)

        
        resized_image = cv2.resize(self.adjustedimage, (desired_size[1], desired_size[0]))

        # Resize the image to the desired size
        

        qt_image = QtGui.QImage(resized_image.data, resized_image.shape[1], resized_image.shape[0], resized_image.shape[1], QtGui.QImage.Format_Grayscale8)

        # Create a QPixmap with the desired size
        pixmap = QtGui.QPixmap.fromImage(qt_image)
        
        



        # Set the QPixmap on the QLabel
        self.image_label.setPixmap(pixmap)




        # Convert the resized image to a QImage
    
    def show_ft_component(self,text):
        if self.image is not None:
            
            component = self.components[text]
            desired_size = (271, 200)
            # Display the FT component in the label
            recovered_image = (component - np.min(component)) / (np.max(component) - np.min(component))
            img_pil = (recovered_image * 255).astype(np.uint8)
            img = np.array(img_pil)
            resized_image = cv2.resize(img, (desired_size[1], desired_size[0]))
            qt_image = QtGui.QImage(resized_image.data, resized_image.shape[1], resized_image.shape[0], resized_image.shape[1], QtGui.QImage.Format_Grayscale8)
            
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            self.ft_label.setPixmap(pixmap)


    def recover_image(self,mode):
        if self.image is not None:
            
            # Assuming self.recovered_image is a NumPy array
            if mode == "ri":
                complex_array =  0*self.real_part + 1j * self.imaginary_part
            else:
                complex_array = self.magnitude * np.exp(1j * self.phase)

            # Perform inverse 2D Fourier Transform
            f_transform_inverse = np.fft.ifft2(np.fft.ifftshift(complex_array))

            # Take the real part to get the recovered image
            self.recovered_image = np.real(f_transform_inverse)
            recovered_image = self.recovered_image

            # Display the recovered image
            plt.imshow(recovered_image, cmap='gray')  # Use 'gray' colormap for grayscale images
            plt.title('Recovered Image')
            plt.colorbar()  # Add a colorbar for intensity scale
            plt.show()
    def numpy_array_to_qpixmap(self,numpy_array):
        # Convert the NumPy array to a QImage
        height, width = numpy_array.shape
        bytes_per_line = width
        image_format = QImage.Format_Grayscale8  # Adjust the format as needed
        qt_image = QImage(numpy_array.data.tobytes(), width, height, bytes_per_line, image_format)

        # Convert the QImage to a QPixmap
        pixmap = QPixmap.fromImage(qt_image)

        return pixmap

    def adjust_brightness_contrast(self, x, y):
        # Normalize x and y values
        x_normalized = (x + 60) / 60
        y_normalized = (y + 60) / 60

        # Convert the image to PIL format
        pil_image = PilImage.fromarray(self.image)

        # Apply contrast adjustment using ImageEnhance.Contrast
        contrast_enhancer = ImageEnhance.Contrast(pil_image)
        pil_image_contrasted = contrast_enhancer.enhance(x_normalized)

        # Apply brightness adjustment using ImageEnhance.Brightness
        brightness_enhancer = ImageEnhance.Brightness(pil_image_contrasted)
        pil_image_adjusted = brightness_enhancer.enhance(y_normalized)

        # Convert the adjusted PIL image back to NumPy array
        self.adjustedimage = np.array(pil_image_adjusted)

        self.show_image()  


    def getorgcomponents(self,text,rows_percentage,col_percentage,type="inner"):
        component=self.orgcomponents[text]
        number_of_rows=rows_percentage*component.shape[0]/100
        number_of_col=col_percentage*component.shape[1]/100
        # // => floor division
        starting_row=(component.shape[0]//2)-(number_of_rows//2)
        ending_row=starting_row+(number_of_rows)

        starting_col=(component.shape[1]//2)-(number_of_col//2)
        ending_col=starting_col+(number_of_col)
        if type=="inner":
            bounding_arr=np.zeros(component.shape)
            bounding_arr[starting_row:ending_row, starting_col:ending_col] = 1
        else:
            bounding_arr=np.ones(component.shape)
            bounding_arr[starting_row:ending_row, starting_col:ending_col] = 0
        
        return np.multiply(component,bounding_arr)
    
        #https://www.educative.io/answers/how-to-use-the-npmultiply-function-for-a-2d-array-in-python
        #https://stackoverflow.com/questions/60325518/make-everything-zeros-in-a-numpy-2d-array-outside-of-bounding-box

