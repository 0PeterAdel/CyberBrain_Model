from transformers import TrainingArguments

training_args = TrainingArguments(
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    warmup_steps=5,
    max_steps=100,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    output_dir="outputs",
    optim="adamw_8bit",
    eval_strategy="steps",  # Use eval_strategy instead of evaluation_strategy
    eval_steps=20,
)

#################################################
#################################################

from trl import SFTTrainer

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    dataset_text_field="text",
    max_seq_length=2048,
    args=training_args,
)
