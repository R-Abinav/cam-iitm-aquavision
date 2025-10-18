import cv2
import numpy as np

def detect_curved_lines_in_image(image_path, min_distance_threshold=150, min_contour_length=100):
    """
    Detect curved lines in an image and highlight them.
    
    Args:
        image_path (str): Path to the input image.
        min_distance_threshold (int): Minimum distance between detected lines.
        min_contour_length (int): Minimum length of contours to be considered.
    
    Returns:
        result_frame (np.ndarray): The image with detected lines highlighted.
        detected_contours (list): List of detected contours.
    """
    # Load the image
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Error: Unable to read image from {image_path}")
        return None, None
    
    # Resize the image for consistent processing (optional)
    frame = cv2.resize(frame, (800, 600))
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours by length
    filtered_contours = []
    for c in contours:
        contour_length = cv2.arcLength(c, True)
        if contour_length > min_contour_length:
            filtered_contours.append(c)

    # Sort contours by area and select the top 2 largest
    filtered_contours = sorted(filtered_contours, key=cv2.contourArea, reverse=True)[:2]
    
    # Further filter based on distance between contours
    final_contours = []
    for c in filtered_contours:
        if len(final_contours) == 0:
            final_contours.append(c)
        else:
            dist_ok = True
            for prev_contour in final_contours:
                prev_rect = cv2.boundingRect(prev_contour)
                curr_rect = cv2.boundingRect(c)
                
                prev_center = (prev_rect[0] + prev_rect[2] // 2, prev_rect[1] + prev_rect[3] // 2)
                curr_center = (curr_rect[0] + curr_rect[2] // 2, curr_rect[1] + curr_rect[3] // 2)
                
                distance = np.sqrt((prev_center[0] - curr_center[0])**2 + (prev_center[1] - curr_center[1])**2)
                if distance < min_distance_threshold:
                    dist_ok = False
                    break
            
            if dist_ok:
                final_contours.append(c)

    # Draw the filtered contours on the original image
    result_frame = np.zeros_like(frame)  # Blank black frame
    for contour in final_contours:
        cv2.drawContours(result_frame, [contour], -1, (0, 0, 255), 3)  # Red color (BGR)

    return result_frame, final_contours

# Path to the image (replace with your racetrack image path)
image_path = "/home/invictus/Desktop/CV/Curved-Detec/test1.jpg"

# Detect curved lines
result_frame, detected_contours = detect_curved_lines_in_image(image_path)

# Display the results
if result_frame is not None:
    cv2.imshow('Detected Curved Lines', result_frame)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()