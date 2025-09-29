# FinancialAlgorithm

**FinancialAlgorithm** is a collection of **numerical algorithms for option pricing**, implemented in **Python and C++**.  
It covers multiple option types and compares different computational methods such as **closed-form solutions, binomial trees, and Monte Carlo simulations with variance-reduction techniques**.  

This repository not only demonstrates **algorithm design & numerical methods**, but also highlights the connection between **financial engineering and computer science**, such as the use of data structures and search algorithms in derivative pricing.  

---

## Features
- **5 categories of derivatives**:
  - Implied Volatility
  - Vanilla Option (European & American)
  - Lookback Option
  - Rainbow Option
  - Average (Asian) Option
- **Multiple numerical methods**:
  - Black-Scholes closed-form solution
  - CRR Binomial Tree (European & American)
  - Monte Carlo Simulation (with Antithetic Variates & Moment Matching)
- **Cross-language support**:
  - Python: rapid prototyping, visualization
  - C++: high-performance implementation
- **GUI project** (C++ / Visual Studio) for interactive pricing  
  - Self-developed by the author  
  - Explanation document is provided in [`/docs/FinAlgoGUI.pdf`](./docs/FinAlgoGUI.pdf)  
  - The GUI source code (C++ / Visual Studio) is included in this repository under `/gui/`.  
    Due to file size limitations, compiled binaries (`.exe`, `.pdb`, `/x64/Debug/`) are **not included in the repository**.  
  - 👉 Pre-compiled executable is available via Google Drive:  
    [Download GUI Executable](https://drive.google.com/drive/folders/19rN5I7lyPibIerePZmzA9pS2DChA1oQm?usp=sharing)
---

## Academic Background
These algorithms were implemented as part of **Financial Computation**,  
a graduate-level course taught by **Prof. Jr-Yan Wang** (Department of International Business, National Taiwan University).  

Prof. Wang holds both **B.S. and M.S. in Computer Science**, and later pursued his Ph.D. in Finance.  
This cross-disciplinary background strongly influenced the course design, which integrates **financial mathematics** and **computational algorithms**.  

👉 Full lecture notes and course materials are available on Prof. Wang’s website:  
[Financial Computation (graduate level) – Prof. Jr-Yan Wang](https://homepage.ntu.edu.tw/~jryanwang/courses/Financial%20Computation%20or%20Financial%20Engineering%20(graduate%20level)/FC_graduate.htm)

---

## Algorithms & Data Structures
Some option pricing algorithms directly involve **data structure concepts**:
- **Lookback Option** → implemented using **tree structures**  
- **Average (Asian) Option** → implemented with **tree structures + binary search / interpolation search**  

This demonstrates how computer science fundamentals (trees, search algorithms)  
are applied in financial engineering to handle path-dependent payoffs.

---

## 📂 Repository Structure
```plaintext
FinancialAlgorithm/
│── README.md
│── main.py                 # Demo entry point
│
├── docs/                   # Documentation
│   └── FinAlgoGUI.pdf      # GUI explanation
│
├── src/                    # Core implementations
│   ├── vanilla_option/
│   ├── rainbow_option/
│   ├── lookback_option/
│   ├── average_option/
│   └── implied_volatility/
│
└── gui/                    # Visual Studio C++ GUI project
    ├── FinancialAlgorithm_Project.sln
    └── FinancialAlgorithm_Project/
```

---

## ⚡ Quick Start
### Run demo
To showcase multiple option pricing methods:
```bash
python main.py
```
This script demonstrates **Vanilla, Rainbow, Lookback, Average, and Implied Volatility** pricing  
with results from different algorithms, followed by **financial interpretations**.

---

## 📖 Why This Matters
This project illustrates:
- **Algorithm design & validation**: closed-form vs. simulation vs. tree-based  
- **Cross-language implementation**: Python prototyping vs. C++ performance  
- **Software engineering practices**: modular design, reproducibility, and GUI development  
- **CS–Finance synergy**: applying **trees, search algorithms, and numerical methods** to real-world financial problems  

---

## 🔮 Future Work
- GPU acceleration (CUDA) for Monte Carlo simulations  
- Integration with financial data APIs  
- Packaging as a Python library (`pip install financialalgorithm`)  

---

## 📌 Author
Developed by **Po-Yen Chen**  
M.S. in Finance, National Taiwan University  
B.A. in Economics, National Chengchi University  
