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

## ⬆️ Pushing to GitHub from Colab

If you are working on Colab and want to push your changes to GitHub, follow these steps:

1. **Configure Git with your user details:**

   ```bash
   !git config --global user.email "youremail@example.com"
   !git config --global user.name "YourUsername"
   ```

2. **Clone your GitHub repository into Colab (if not already cloned):**

   ```bash
   !git clone https://github.com/YourUsername/CyberBrain_Model.git
   %cd CyberBrain_Model
   ```

3. **Add all files to Git:**

   ```bash
   !git add .
   ```

4. **Commit the changes with a descriptive message:**

   ```bash
   !git commit -m "Initial commit of CyberBrain_Model project with all necessary files"
   ```

5. **Push the changes to GitHub:**

   ```bash
   !git push
   ```

   You may be prompted to enter your GitHub credentials or token. If you are using a token, set it as instructed by GitHub.

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

