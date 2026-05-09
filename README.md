# Hybrid Image Processing & Computer Vision Toolkit

Computer vision and image processing toolkit built with Python and NumPy featuring custom image filtering, color space transformations, convolution pipelines, and hybrid image synthesis.

This project focuses on foundational computer vision algorithms, image manipulation systems, and low-level visual processing techniques commonly used in modern imaging and machine learning pipelines.

---

## Features

- Custom 2D convolution filtering system
- Edge detection using Sobel and Laplacian filters
- Gaussian blur and low-pass filtering
- Hybrid image generation using frequency-domain techniques
- RGB, grayscale, LAB, and HSV image processing
- Image transformations and intensity analysis
- Multi-scale image visualization
- Matrix-based image manipulation using NumPy

---

## Technical Highlights

### Custom Image Filtering Pipeline
Implemented convolution-based filtering systems using:
- Gaussian blur filters
- Sobel edge detection
- Laplacian sharpening
- low-pass and high-pass image filtering

to process and transform image data at the pixel level.

### Color Space Transformations
Built RGB-to-HSV and grayscale conversion pipelines from scratch using:
- vectorized NumPy operations
- channel-wise image processing
- manual hue, saturation, and value computations

without relying on high-level computer vision conversion utilities.

### Hybrid Image Synthesis
Developed hybrid image generation systems by:
- extracting low-frequency image features
- isolating high-frequency edge details
- combining filtered visual information across multiple scales

to create images that appear differently depending on viewing distance.

---

## Technologies

- Python
- NumPy
- Matplotlib
- Computer Vision
- Image Processing
- Convolution Filtering

---

## Algorithms Implemented

- 2D Convolution
- Gaussian Filtering
- Sobel Edge Detection
- Laplacian Filtering
- RGB to HSV Conversion
- Grayscale Conversion
- Hybrid Image Synthesis

---

## Running the Project

### Requirements
- Python 3.11+
- NumPy
- Matplotlib
- SciPy

### Run
```bash
python main.py
