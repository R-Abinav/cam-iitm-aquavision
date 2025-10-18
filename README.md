# AUV Computer Vision Code for IITM AquaVision Competition 2025

This repository contains computer vision algorithms and implementations developed for testing camera-based functions during the IITM AquaVision Competition (2025). The code focuses on underwater object detection, gate detection, color tracking, and line detection for autonomous underwater vehicles (AUVs).

## File Descriptions

### Camera and Basic Detection
- **`cam-test.py`** - Basic camera testing script to verify camera functionality and frame capture
- **`color_second.py`** - Color detection implementation using HSV color space with CLAHE preprocessing for better underwater visibility
- **`image_main.py`** - Image-based color detection and bounding box generation for static images
- **`main.py`** - Real-time color detection and tracking using webcam feed with bounding box and centroid calculation

### Gate Detection Algorithms
- **`gate_code.py`** - Real-time gate detection using Hough line transform on live camera feed
- **`gate_code_img.py`** - Static image-based gate detection with line intersection finding
- **`gate_lmao.py`** - Simplified gate detection implementation for testing purposes
- **`new_gate_code_image.py`** - Enhanced gate detection with improved line classification and corner detection

### Line Detection and Processing
- **`hough_line.py`** - Hough line transform implementation for detecting horizontal and vertical lines
- **`extract_line_data.py`** - Line data extraction with slope, intercept, length, and midpoint calculations
- **`vertical_line_detector.py`** - Real-time vertical line detection using Hough transform
- **`vertical_line_img.py`** - Static image-based vertical line detection

### Clustering and Advanced Processing
- **`dbscan_clustering.py`** - DBSCAN clustering algorithm for grouping similar lines
- **`proper_clustering.py`** - K-means clustering for separating left/right poles and averaging horizontal lines
- **`implement.py`** - Implementation combining line extraction and clustering for gate detection

### Measurement and Analysis
- **`measure.py`** - Width measurement and comparison of detected objects using contour analysis
- **`measure_with_vid.py`** - Real-time width measurement using video feed with contour detection

### Specialized Detection
- **`Track_Curved.py`** - Curved line detection for racetrack navigation using contour analysis
- **`magnifying.py`** - Contour filtering and masking for object isolation

### Utility Functions
- **`util.py`** - Utility functions for color space conversion and HSV range calculation

## Key Features
- Real-time camera processing
- HSV color space detection with underwater optimization
- Hough line transform for gate detection
- Clustering algorithms for line grouping
- Contour-based object measurement
- CLAHE preprocessing for underwater visibility enhancement

## Dependencies
- OpenCV (cv2)
- NumPy
- scikit-learn
- PIL (Pillow)

## Usage
Each script can be run independently for testing specific computer vision functionalities. Most scripts support both static image processing and real-time camera feed processing.
