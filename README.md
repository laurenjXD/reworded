# Re:Worded

> A Permutation Playground for Words. An interactive tool to visualize combinatorial concepts.

![Project Screenshot]([LINK TO YOUR SCREENSHOT HERE])
*A preview of the Re:Worded interface.*

---

## 📥 Download & Run (No Coding Required)

**For the easiest experience, download the standalone executable:**

1.  Go to the **[Releases](../../releases)** section on the right sidebar.
2.  Download the file named **`ReWorded.exe`**.
3.  Double-click to run.
    * *Note: If Windows Defender shows a warning, click "More Info" > "Run Anyway". This appears because this is a custom student application and is not digitally signed.*

---

## 🧐 About the Project

**Re:Worded** is an interactive application designed to visualize and explore the combinatorial concept of **Permutations**.

Developed as a final requirement for **S-CSPC212 (Discrete Structures 1)**, this tool transforms abstract counting principles into tangible results. While calculating $n!$ (n-factorial) on paper is standard, visualizing the actual resulting set helps students better grasp the magnitude and structure of combinatorial growth.

### 🧮 Mathematical Foundation
The application serves as a "playground" to demonstrate:
* **Permutations ($P(n, n)$):** Calculating the number of ways to arrange a set of objects where order matters.
* **Factorial Growth:** Visualizing how the sample space explodes ($n!$) as the input length increases.
* **Systematic Listing:** Generating outcomes in a readable format to verify manual calculations.

### 🚀 Key Features
* **Real-Time Computation:** Instantly calculates the total count of possible arrangements.
* **Scrollable Output:** Displays the generated list of words in a clean, scrollable view.
* **Modern UI:** Built with **CustomTkinter** for a professional, dark-mode interface.
* **Error Handling:** Prevents crashes when inputs are invalid.

---

## 🛠️ Built With

* [Python 3.x](https://www.python.org/)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI library
* [Pillow](https://python-pillow.org/) - Image processing support
* [Itertools](https://docs.python.org/3/library/itertools.html) - Combinatorial logic

---

## 💻 Running from Source Code

If you prefer to run the raw Python code (or if you are grading the syntax), follow these steps:

1.  **Clone the repository**
    ```bash
    git clone [YOUR_GITHUB_REPO_LINK_HERE]
    ```
2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application**
    ```bash
    python main.py
    ```

---

## 👤 Author

**[YOUR NAME HERE]**
* **Course:** S-CSPC212 – Discrete Structures 1
* **Date:** December 2025

---
