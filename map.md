Below is a detailed, step-by-step plan to set up the work environment for fine-tuning our AI model on ethical cyber security using technical books as the training data. This plan covers everything from cloning the repository to configuring GPU settings, preparing the dataset, and launching the training process.

---

## 1. Project Overview and Objectives

- **Objective:** Fine-tune the DeepSeek-R1 model for Ethical Cyber Security using domain-specific data extracted from technical books.
- **Data Source:** Books containing technical content on cyber security, processed into instruction-response pairs.  
  **Books File Link:** [books.jsonl](https://github.com/0PeterAdel/CyberBrain/blob/main/Create-DataSet/books.jsonl)
- **Approach:** Use Unsloth with LoRA to efficiently fine-tune the model on limited hardware, leveraging 4-bit quantization and offloading heavy layers to the CPU when needed.
- **Hardware Consideration:**  
  For GPU-based training, we assume a system with a GPU like the NVIDIA Quadro M620 Mobile (≈1.956GB VRAM). We'll use a custom device map to balance the load between the GPU and CPU.

---

## 2. Environment Setup

### a. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/0PeterAdel/CyberBrain.git
cd CyberBrain
```

### b. Create and Activate the Conda Environment

Create an environment with Python 3.11:

```bash
conda create -n deepseek python=3.11
conda activate deepseek
```

### c. Install Required Dependencies

Install necessary packages and toolkits:

```bash
conda install -c conda-forge gcc_linux-64 gxx_linux-64
conda install -c conda-forge cudatoolkit=11.7
pip install -r requirements.txt
```

This ensures compatibility with GPU training and the correct versions of GCC and CUDA.

---

## 3. Data Preparation

### a. Raw Data from Books

- **Source:** Our training data is extracted from technical books on cyber security.
- **File:** The raw books file is located in the `Create-DataSet/` folder.  
  **Link:** [books.jsonl](https://github.com/0PeterAdel/CyberBrain/blob/main/Create-DataSet/books.jsonl)

### b. Data Processing

- Use the provided dataset creation scripts to convert the raw text into instruction-response pairs.
- **Goal:** Each data entry should be a JSON object with an `"instruction"` (e.g., a technical query or topic) and an `"output"` (detailed explanation).

### c. Verify the Dataset

- Make sure the processed dataset (e.g., `cybersecurity_training_data.jsonl`) is correctly formatted.
- Place this file in an accessible location and update paths in your training scripts accordingly.

---

## 4. Model Loading and GPU Configuration

### a. Loading the Model with Unsloth and LoRA

For GPU-based training, we use Unsloth to load the DeepSeek-R1 model with 4-bit quantization. Because our GPU has limited memory, we need a custom device map:

- **Critical Layers on GPU:** Embedding layers and LM head.
- **Heavy Transformer Layers Offloaded:** Offload transformer layers to the CPU.

**Command Example:**

```python
from unsloth import FastLanguageModel

model_name = "unsloth/DeepSeek-R1-Distill-Llama-8B-unsloth-bnb-4bit"
max_seq_length = 2048

# Define a custom device map for limited GPU memory
device_map = {
    "model.embed_tokens": 0,  # Load embedding layer on GPU
    "lm_head": 0,             # Load language model head on GPU
    "model.layers": "cpu"     # Offload transformer layers to CPU
}

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=model_name,
    max_seq_length=max_seq_length,
    load_in_4bit=True,
    device_map=device_map,
)

print("Model loaded successfully with GPU and custom device map!")
```

### b. Verify GPU Settings

Before proceeding with training, verify that your GPU is recognized:
- Run `nvidia-smi` in your terminal.  
- Ensure that your GPU (e.g., Quadro M620 Mobile) is detected and that the memory available is approximately 1.956 GB.

---

## 5. Training Settings and Fine-Tuning Process

### a. Key Training Parameters

- **max_seq_length:**  
  Controls the maximum number of tokens per input.  
  - **Default:** 2048  
  - **If GPU memory is limited:** Consider reducing to 1024 or even 512.  
  **Explanation:** Lowering this value decreases memory usage per input but reduces the amount of context.

- **num_train_epochs:**  
  Number of complete passes over the training dataset.  
  - **Recommended for initial experiments:** 1–3 epochs  
  **Explanation:** Fewer epochs mean faster experiments and lower resource consumption.

- **gradient_accumulation_steps:**  
  Simulates a larger batch size by accumulating gradients over multiple steps.  
  - **Example:** 8 steps  
  **Explanation:** This allows stable training without increasing the per-step memory footprint.

### b. Fine-Tuning Process

1. **Prepare the Dataset:**  
   Use Hugging Face’s Datasets library to load and tokenize the instruction-response pairs.  
   Adjust the `max_seq_length` in your preprocessing function as needed.

2. **Configure the Trainer:**  
   Set up the `TrainingArguments` with the parameters outlined above.  
   Use a small per-device batch size (e.g., 1) and appropriate gradient accumulation steps.

3. **Launch Training:**  
   Start the training process by running the trainer script (e.g., `trainer-v2.py`).  
   Monitor training progress and adjust parameters if you encounter memory or speed issues.

**Sample Usage Command:**

```bash
python trainer-v2.py
```

---

## 6. Summary of Each Stage

1. **Environment Setup:**  
   - Clone the repository, create and activate the Conda environment, and install all dependencies.

2. **Data Preparation:**  
   - Process technical books into a dataset of instruction-response pairs.  
   - Verify that the dataset (from [books.jsonl](https://github.com/0PeterAdel/CyberBrain/blob/main/Create-DataSet/books.jsonl)) is correctly formatted.

3. **Model Loading:**  
   - Load the DeepSeek-R1 model with Unsloth using 4-bit quantization.  
   - Define a custom device map to balance GPU and CPU usage, ensuring the GPU (e.g., Quadro M620) handles only critical parts.

4. **Training Configuration:**  
   - Set `max_seq_length`, `num_train_epochs`, and `gradient_accumulation_steps` based on your device’s capabilities.  
   - These settings help manage memory usage and training speed on limited hardware.

5. **Fine-Tuning:**  
   - Use the trainer scripts (trainer-v2.py or trainer.py) to fine-tune the model on your dataset.  
   - Monitor training progress, evaluate, and save the model for later inference.

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
