# 🧙‍♂️ Invisible Cloak – OpenCV (Python)

A fun computer vision project inspired by **Harry Potter’s Invisible Cloak** — implemented using **OpenCV + Python**.
This project captures the background and makes any **BLUE-colored cloth** appear invisible in real-time!

##  Demo

 Works in real time using your laptop webcam.  
 Move out of the frame → background captured  
 Come back with a BLUE cloth → your body disappears 

## 📸 How It Works

The trick is simple:
1. Capture the **background** without the person.
2. Detect BLUE color using **HSV color space**.
3. Replace the BLUE area with the background.
4. Combine both frames to create the invisibility effect.
---
##  Tech Stack

- Python
- OpenCV
- NumPy

## 📂 Project Structure

📦 invisible-cloak-opencv
 ┣ 📜 cloak.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md

## 🧪 Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt


### 2️⃣ Run the script
```bash
python cloak.py
## 🔧 Controls
| Key | Action |
|-----|--------|
| **C** | Re-capture background |
| **Q** / **ESC** | Quit program |

## 🎨 Color Detection Settings
The program detects BLUE cloth using the following HSV range:

```python
lower_blue = np.array([90, 120, 70])
upper_blue = np.array([130, 255, 255])
```

---

## 🧩 Code Used in the Project

The full code is available in `cloak.py`.  
(Uploaded as part of this repository)
## 📜 License
This project is completely free and open-source under the **MIT License**.

---

## ⭐ Show Support

If you like this project, please ⭐ the repository and share it with your friends!
