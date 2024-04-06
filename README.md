# WiseStocks
MariHacks 2024 project made by Davigbit, flavieq88, 2183911, Elena-Lungoci.

## Introduction
As part of our project for MariHacks 2024, we designed a website to display AI-predicted stock values. We trained a linear regression model using data about the stock market we collected and processed, updated daily. The website also displays the graph of stock values from the past month and the change in stock value of the day. 

## How we built it
For implementing the back-end, we used Python and the following libraries: pandas, numpy, sk-learn, joblib, plotly, pyplot, json.
We collected our data from the AlphaVantage API.
We divided the data into training and testing sets, and trained the linear regression object. The model was used to generate a json file that can be used for front-end. 

We implemented the front-end using the Svelte framework. 

## Challenges we encountered
We initially tried to build our own neural network from scratch to classify if the stock will rise or fall, but the classifier was struggling with overfitting, therefore validation was bad.
Collecting and processing our data using the API was also very time-consuming.
THe deployment of the json file to front-end was also very difficult.

## Accomplishments that we are proud of
We are satisfied with the friendly user interface we built, where anyone can access the most recent data of several stocks with accurate predictions, based on historical data.

## What we learned
For the members who were less experiences, we learned how to use JavaScript and to use APIs.
We also learned different front-end techniques for making the user interface better.

## What's next for WiseStocks
We want to add more companies to predict stock for, as we are currently limited to 4 companies. 
We could also gather more meaningful data to make our model more accurate. 
Lastly, we would like to implement a section with a News API that would display the most recent news articles related to the stock.