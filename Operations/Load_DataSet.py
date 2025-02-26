from datasets import load_dataset
dataset = load_dataset("json", data_files="DataSet/DataSet.json")


# Define the text template
prompt_template = """### Instruction:
{instruction}

### Response:
{response}"""

# Get the EOS token from the tokenizer
EOS_TOKEN = tokenizer.eos_token

# Data formatting function
def formatting_func(examples):
    texts = []
    for inst, resp in zip(examples["instruction"], examples["Response"]):
        text = prompt_template.format(instruction=inst, response=resp) + EOS_TOKEN
        texts.append(text)
    return {"text": texts}

# Apply formatting to the dataset
dataset = dataset.map(formatting_func, batched=True)

## Splitting the dataset
dataset = dataset["train"].train_test_split(test_size=0.1)
train_dataset = dataset["train"]
eval_dataset = dataset["test"]
