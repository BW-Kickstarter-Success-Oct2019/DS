# Model API
The model API takes a JSON POST string and serves a prediction.

The expected JSON POST format is:
`{'name': string, 'blurb': string, 'goal': float, 'country': string(2), 'duration': float, 'category': string,}`

Prediction will be returned in this JSON format:
`{'pred': float}`

Here's an example command:
```curl -X POST -H "Content-Type: application/json" -d '{"name": "This is a test Kickstarter header", "blurb": "This is an example description of a kickstarter project to test for the API. I would like to thank my wife, parents, and all my loving family members for this to work. I would also like to thank all the Kickstarter team members and project leads for making this possible.", "goal": 800.0, "country": "US", "duration":15.0, "category": "fashion"}' http://127.0.0.1:5000/predict```

Here's an example comand with high success probability
```curl -X POST -H "Content-Type: application/json" -d '{"goal": 2011.0, "country": "US", "duration":67.0, "category": "publishing"}' http://127.0.0.1:5000/predict```



## Directory Structure:
```
├── README.md
│
├── api                <- Model serving app
│
├── data               <- Not on github      
│    ├── processed     <- The final, canonical data sets for modeling.
│    └── raw           <- The original, immutable data dump.
│
├── notebooks          <- Jupyter notebooks
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│    |
│    └── figures       <- Generated graphics and figures to be used in reporting
│
├── weights            <- Trained and serialized models, model predictions, or model summaries
│
├── Pipfile
│
├── Dockerfile
│
└── requirements.txt
```
## Change log:
2019-11-08 - Han - Organized project directory.

2019-10-22 - Luc - Added one naive model notebook, model accuracy of .86

2019-10-21 - Han - Deployed using ngrok tunneling for front/backend to test.

2019-10-21 - Han - Made RestAPI with Flask and format. Tested locally.

2019-10-21 - Han - Added EDA and two naive model notebooks. Created a model 0.68 accuracy.  

2019-10-21 - Han - Setup project structure.
