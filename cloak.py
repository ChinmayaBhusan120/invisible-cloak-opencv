import cv2
import numpy as np
import time

# Open webcam
cap = cv2.VideoCapture(0)
time.sleep(2)  # let camera warm up

# Capture the background (without you in the frame)
print("[i] Capturing background... please move out of frame.")
for i in range(60):
    ret, background = cap.read()
    if not ret:
        continue
background = np.flip(background, axis=1)

print("[i] Background captured. Hold your BLUE towel in front of you!")

# Define HSV range for blue colour
lower_blue = np.array([90, 120, 70])
upper_blue = np.array([130, 255, 255])

# Morphology kernel
kernel = np.ones((3, 3), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)   # flip frame horizontally
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask to detect blue colour
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Clean the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask_inv = cv2.bitwise_not(mask)

    # Segment out the blue towel from the frame
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    rest_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine cloak area with rest of frame
    final_output = cv2.addWeighted(cloak_area, 1, rest_area, 1, 0)

    # Add instructions on screen
    cv2.putText(final_output, "Press Q/ESC = Quit | Press C = Re-Capture BG",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Invisible Cloak", final_output)

    # Check key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:   # quit with q or ESC
        print("[i] Exiting program...")
        break
    elif key == ord('c'):  # re-capture background
        print("[i] Re-capturing background... move out of frame.")
        time.sleep(2)
        for i in range(60):
            ret, background = cap.read()
            if ret:
                background = np.flip(background, axis=1)
        print("[i] Background updated!")

# Release everything
cap.release()
cv2.destroyAllWindows()
