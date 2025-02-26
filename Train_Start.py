# Start Train
trainer.train()

#  Model Evaluation
trainer.evaluate()

# Save form and tokenizer:
model.save_pretrained("CyberBrain_model")
tokenizer.save_pretrained("CyberBrain_model")
