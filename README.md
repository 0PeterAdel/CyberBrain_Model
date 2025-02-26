# CyberBrain_Model

CyberBrain_Model is an advanced AI project designed for fine-tuning the model `unsloth/DeepSeek-R1-Distill-Qwen-14B` specifically for cyber security tasks. This repository provides tools and scripts for training and fine-tuning large language models efficiently using minimal hardware resources. The goal is to adapt the model for ethical cyber security applications, making it efficient even on devices with limited computational power, whether you have a low-end CPU or a GPU with limited VRAM.

In this project, we use technical content extracted from various cyber security sources as our primary training data. The raw text is processed into instruction-response pairs tailored for fine-tuning the model on cyber security scenarios. You can access the training data [here](./DataSet).

![AI Training](assest/ai.jpg)

## 📦 Project Structure

```
assest/                         # Assets, images, and other media files
Configure_Training_Arguments.py  # Script for configuring training arguments
DataSet/                         # Directory containing dataset files
Load_DataSet.py                  # Script to load the dataset
LoRA_Configuration.py            # Script for LoRA configuration
map.md                           # Documentation about mapping
Model_Loading_with_Unsloth.py    # Script to load the model using Unsloth
README.md                        # This file
requirements.txt                 # Required dependencies for the project
Table-Ways.md                    # Documentation about table ways
Train_Start.py                   # Script to start training the model
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/CyberBrain_Model.git
cd CyberBrain_Model
```

### 2. Set Up the Environment

Create a new virtual environment (Python 3.11 is recommended):

```bash
python -m venv .env
# Activate the environment:
# On Linux/Mac:
source .env/bin/activate
# On Windows:
.env\Scripts\activate
```

### 3. Install Required Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install torch==2.5.1+cu118 --index-url https://download.pytorch.org/whl/cu118
pip install torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## 🤖 Running the Project

- **Model Loading:** Run `Model_Loading_with_Unsloth.py` to load the model.
- **Training:** Run `Train_Start.py` to start the fine-tuning process.
- **Configurations:** Review `LoRA_Configuration.py` and `Configure_Training_Arguments.py` for training settings.

## 📄 Additional Documentation

Refer to the following files for more details:
- `map.md`
- `Table-Ways.md`

---

This repository is designed to be modular and flexible, making it easy to customize for your training needs on cyber security tasks. Feel free to modify scripts and settings to suit your project requirements.

## 🚀 Quick Start on Google Colab

To quickly run CyberBrain_Model on Google Colab, follow these steps:

1. **Clone the Repository**  
   Open a new Colab notebook and run:
   ```bash
   !git clone https://github.com/YourUsername/CyberBrain_Model.git
   %cd CyberBrain_Model
   ```

2. **Install Dependencies**  
   Install the required packages by running:
   ```bash
   !pip install --upgrade pip
   !pip install -r requirements.txt
   !pip install torch==2.5.1+cu118 --index-url https://download.pytorch.org/whl/cu118
   !pip install torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

3. **Open and Run `main.ipynb`**  
   Open the `main.ipynb` notebook in Colab. This notebook provides a step-by-step guide to:
   - Load the dataset from the `DataSet` directory.
   - Load the model using `Model_Loading_with_Unsloth.py`.
   - Configure training arguments via `Configure_Training_Arguments.py`.
   - Start training using `Train_Start.py`.
   - Evaluate the model and monitor training progress.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Contact

For questions or contributions, feel free to open an issue or contact us directly through GitHub.

- Portfolio: [peteradel.netlify.app](https://peteradel.netlify.app)
- LinkedIn: [linkedin.com/in/1peteradel](https://linkedin.com/in/1peteradel)

## ⭐ Give a Star

If you find this project useful or interesting, please give it a star! Your support helps improve the project and motivates further development.

![AI Training](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXNhdWQzZWM0NzB6ZzRxcHZvdmxmMHJ3OWIwZ3RnZDY1dGJjZ3MxaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/H1eVHxFk781UxUNMul/giphy.gif)

---

🤍 Thank you for checking out **CyberBrain**! Happy training!

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>
</p>
```
