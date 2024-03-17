# KTU Notifications Relevancy Classifier

Code to inference and fine tune a [distilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) model based on **KTU Notification Data**. To be used for live notification relevancy filter for [KTU Bot](https://github.com/devadathanmb/ktu-bot).

The dataset used to fine tune the model is [data.json](./data.json)

Notebook used to train the model is provided at [relevancy_classifier.ipynb](./relevancy_classifier.ipynb)

## Examples

### Example : 1

- Notification

```
Notification : Exam registration date extended - B.Tech S2/S4/S6/S8 Exam May 2024(2019 scheme)
```

- Result

```json
[
  [
    {
      "label": "LABEL_1",
      "score": 0.9998329877853394
    },
    {
      "label": "LABEL_0",
      "score": 0.00016703762230463326
    }
  ]
]
```

### Example : 2

- Notification

```
Notification : APJ Abdul Kalam Technological University invites Expression of Interest (EOI) from firms for installation of pandal and stage, seating arrangements, internal electrification, public address system/ sound system, decoration of stage and pandal etc
```

- Result

```json
[
  [
    {
      "label": "LABEL_0",
      "score": 0.9993565678596497
    },
    {
      "label": "LABEL_1",
      "score": 0.000643469684291631
    }
  ]
]
```

> **Note**
> LABEL_0 indicates irrelevancy and LABEL_1 indicates relevancy of the given notification.

## To use this fine tuned model

This fine tuned model is deployed on [HuggingFace](https://huggingface.co/) as a free serverless inference API.

To see how to use the huggingface inference API and to test the model, see [this](https://huggingface.co/devadathanmb/ktu-notifs-relevancy-bert).

## To run the inference API locally

1. Make sure [python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) is installed.
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
