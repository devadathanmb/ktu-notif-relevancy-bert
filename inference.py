# Import necessary libraries
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer

# Load the trained model for inference
model = DistilBertForSequenceClassification.from_pretrained("./trained_model")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)  # Ensure the model is on the same device as input tensors
model.eval()


def predict(input_text):
    # Test on custom input
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    tokenized_input = tokenizer(input_text, return_tensors="pt")
    input_ids = tokenized_input["input_ids"].to(device)
    attention_mask = tokenized_input["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)

    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()

    return bool(predicted_class)
