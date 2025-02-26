>**Below is a comparison table of several free methods for fine-tuning large language models, with a focus on training from books on devices with limited hardware resources (weak devices). The table compares Unsloth with LoRA, Hugging Face Transformers with PEFT (including LoRA/QLoRA), DeepSpeed, and Hugging Face Accelerate.**


| **Method**                           | **Resource Consumption**                                                                                         | **Ease of Use**                                                 | **Suitability for Books-Based Fine-Tuning**                                                       | **Accuracy & Performance**                                                        | **Pros**                                                                                                                                              | **Cons**                                                                                                                   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Unsloth with LoRA**                | - Uses 4-bit quantization<br>- Low memory usage via LoRA adaptation<br>- Best with GPU, but CPU training is very slow | - Designed specifically for consumer hardware<br>- Integrated into Unsloth ecosystem | - Very suitable; tailored to fine-tuning domain-specific texts (e.g., technical books)             | - High accuracy if fine-tuned properly<br>- Fast on GPU (with proper offloading settings)            | - Free and optimized for limited resources<br>- Easy to set up<br>- Reduces training cost by adapting only a small subset of parameters                | - Requires GPU for best performance<br>- May need custom device maps/offloading if GPU memory is limited                     |
| **Hugging Face Transformers with PEFT (LoRA/QLoRA)** | - QLoRA further reduces memory usage<br>- Efficient fine-tuning via partial weight updates                       | - Straightforward integration with popular Transformers library<br>- May require additional parameter tuning | - Very suitable; flexible approach that works well with instruction-response datasets from books  | - High accuracy and performance when fine-tuning is optimized<br>- QLoRA provides excellent memory efficiency on weak GPUs | - Highly flexible and widely adopted<br>- Open source and actively maintained<br>- QLoRA is particularly effective on limited hardware                | - Requires careful tuning and configuration<br>- Setup may be more involved than Unsloth with LoRA                       |
| **DeepSpeed**                        | - State-of-the-art optimizations for memory and speed<br>- Designed for distributed/multi-GPU training            | - More complex configuration<br>- Requires familiarity with distributed training concepts           | - Suitable if you have a large dataset and a multi-GPU setup<br>- Might be overkill for small book datasets | - Extremely fast on well-equipped systems<br>- Can scale to very large models, but may not be ideal on weak devices        | - Cutting-edge performance and scalability<br>- Significant memory and speed optimizations available in distributed settings                             | - Complex setup; not ideal for devices with limited hardware (especially single low-end GPUs or CPU-only systems)             |
| **Hugging Face Accelerate**          | - Does not reduce memory usage by itself; helps manage and distribute load across devices                         | - Easy-to-use interface for multi-device management<br>- Simplifies hardware utilization           | - Good for distributed training setups<br>- Not specifically optimized for low-resource devices on its own             | - Accuracy similar to base Transformers<br>- Improves utilization in multi-device environments                          | - Simplifies the process of leveraging available hardware<br>- Open source and well-integrated with Transformers                                       | - Does not inherently reduce memory footprint<br>- Best suited for multi-GPU/distributed setups rather than very weak devices |

### Key Considerations for Our Project

- **Training Data from Books:**  
  Our training dataset is derived from technical books on cyber security, processed into instruction-response pairs. This domain-specific data helps the model learn detailed, specialized content.  
  [Books file used for training](https://github.com/0PeterAdel/CyberBrain/blob/main/Create-DataSet/books.jsonl)

- **Max Sequence Length (`max_seq_length`):**  
  This parameter defines the context window for the model. While a higher value (e.g., 2048) provides more context, it also requires more memory. On devices with limited GPU RAM, consider reducing this value to 1024 or even 512 to reduce resource consumption.

- **Number of Training Epochs (`num_train_epochs`):**  
  This parameter controls how many complete passes over the dataset are performed. For initial experiments on a weak device, using fewer epochs (e.g., 1–3) is advisable to reduce training time and prevent overfitting.

- **Gradient Accumulation (`gradient_accumulation_steps`):**  
  This setting simulates a larger batch size by accumulating gradients over several steps. For example, using 8 accumulation steps allows you to benefit from a larger effective batch size without increasing memory usage per step.

- **GPU Definition and Device Mapping:**  
  For GPU-based training, it is crucial to ensure that your graphics card is correctly defined and recognized before training starts. In our project, if using a GPU like the NVIDIA Quadro M620 Mobile (with ~1.956 GB VRAM), we employ custom device mapping to offload heavy components (such as transformer layers) to the CPU while keeping critical components (like embeddings and LM head) on the GPU. This balances performance and memory constraints.

### Which Method is Best for Our Project?

For training an AI model on technical books for Ethical Cyber Security on a weak device:
- **Unsloth with LoRA** is a strong candidate because it is specifically designed for efficient fine-tuning on limited hardware and is straightforward to use.
- **Hugging Face Transformers with PEFT (LoRA/QLoRA)** is also a great option, offering flexibility and further memory optimizations (with QLoRA) but may require more careful tuning.
- **DeepSpeed** and **Hugging Face Accelerate** are excellent for distributed and high-performance scenarios but might be overkill or too complex for our use case on a weak device.

Given our goals—training on books with domain-specific data on a device with limited GPU resources—**Unsloth with LoRA** (or a well-tuned PEFT/QLoRA approach) offers the best balance between resource consumption, ease of use, and fine-tuning accuracy.

---

🤍 Thank you for checking out **CyberBrain**! Happy training!

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>
</p>

