# KTU Notifications Relevancy Classifier

Code to inference and fine tune a [distilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) model based on **KTU Notification Data**. To be used for live notification relevancy fitler for [KTU Bot](https://github.com/devadathanmb/ktu-bot).

The dataset used to fine tune the model is [data.json](./data.json)

Notebook used to train the model is provided at [relevancy_classifier.ipynb](./relevancy_classifier.ipynb)

## To run the inference API locally

1. Make sure [python]() and [pip]() is installed.
2. Clone the repo using

```bash
git clone https://github.com/devadathanmb/ktu-notif-relevancy-bert.git
```

3. Create a python virtual environment. For more info see [this](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
4. Install the dependencies using

```bash
pip install -r requirements.txt
```

5. Run the flask application using

```
flask run
```

6. Test the API using

```
curl -X POST http://localhost:5000/api/relevancy -H 'Content-Type: application/json' --data-raw '{"text": "BTech S6(R, S) result published on KTU web portal"}'
```

## To use this fine tuned model

This fine tuned model is deployed on [HuggingFace](https://huggingface.co/) as a free serverless inference API. For more information, see [this](https://huggingface.co/devadathanmb/ktu-notifs-relevancy-bert).
