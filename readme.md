# 📚 Software Re-Engineering – Library Management System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-orange.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite3-green.svg)

## 📌 Project Overview
This project is part of the **Software Re-Engineering** assignment course. The target was to choose an existing open-source software baseline, analyze its architecture, fix legacy dependency bugs, and introduce functional/design improvements.

* **Original Base Repository:** [Prakarsha/Library-Management-System](https://github.com/Prakarsha/Library-Management-System)
* **Re-Engineered Repository:** [Usman-ali31/Software-ReEngineering-Library-System](https://github.com/Usman-ali31/Software-ReEngineering-Library-System)

---

## 🚀 Re-Engineering Modifications Made

### 1. Legacy Library & UI Crash Fixes (Refactoring)
* **Pillow Migration:** Upgraded deprecated `Image.ANTIALIAS` calls to modern `Image.Resampling.LANCZOS` standard to prevent execution crashes on modern Python environments.
* **Canvas Fallback Handler:** Implemented an exception-handling fallback design that renders custom colored UI banners when local PNG background images are missing, preventing blank screen rendering.

### 2. Live Dashboard Real-Time Counter (New Feature)
* Added a centered dynamic dashboard header panel on the main menu.
* Real-time querying against the SQLite database (`test.db`) to compute total available book copies and active issued books count.

### 3. Dynamic Overdue Fine Calculation Module (Functional Improvement)
* Modified the book return logic (`returnbook`).
* Automatically compares the expected return date against the system date.
* Calculates a penalty fine rate (Rs. 10/day) for overdue items and alerts the administrator via detailed popup dialogs.

---

## 🛠️ Tech Stack & Requirements
* **Language:** Python 3.x
* **GUI Framework:** Tkinter
* **Database:** SQLite3
* **Image Processing:** Pillow (`PIL`)

---

## 🏃 How to Run the Application

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Usman-ali31/Software-ReEngineering-Library-System.git](https://github.com/Usman-ali31/Software-ReEngineering-Library-System.git)
   cd Software-ReEngineering-Library-System