model = FastLanguageModel.get_peft_model(
    model,
    r=16,  # Adjust the LoRA rank as needed
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],  # Specify key modules
    lora_alpha=16,
    lora_dropout=0.05,  # You can adjust dropout to prevent overfitting
    bias="none"
)
