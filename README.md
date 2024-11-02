# <img src="https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/blob/master/sentimental_analysis/realworld/static/images/logo-black-2.png" height="42" width="42"/>Emotion Insight Analyzer
## Software Engineering Project for CSC 510

[![DOI](https://zenodo.org/badge/881529485.svg)](https://doi.org/10.5281/zenodo.14028705)
[![GitHub Release](https://img.shields.io/github/release/Fall24-SE-ASK/Emotion-Insight-Analyzer)](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/releases)
![Build](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/actions/workflows/main.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-v3.11-brightgreen.svg)
![GitHub contributors](https://img.shields.io/github/contributors/Fall24-SE-ASK/Emotion-Insight-Analyzer)
![GitHub issues](https://img.shields.io/github/issues/Fall24-SE-ASK/Emotion-Insight-Analyzer)
![GitHub closed issues](https://img.shields.io/github/issues-closed/Fall24-SE-ASK/Emotion-Insight-Analyzer)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Fall24-SE-ASK/Emotion-Insight-Analyzer)](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/pulls)
![GitHub language count](https://img.shields.io/github/languages/count/Fall24-SE-ASK/Emotion-Insight-Analyzer)
[![GitHub-size](https://img.shields.io/github/languages/code-size/Fall24-SE-ASK/Emotion-Insight-Analyzer)](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer)
[![github workflow](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/actions/workflows/code_coverage.yml/badge.svg)](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/actions/workflows/code_coverage.yml)
[![codecov](https://codecov.io/gh/Fall24-SE-ASK/Emotion-Insight-Analyzer/branch/master/graph/badge.svg)](https://app.codecov.io/gh/Fall24-SE-ASK/Emotion-Insight-Analyzer)

---
The Emotion Insight Analyzer is a versatile tool that can perform sentiment analysis on different types of data, including text, audio, reviews, and news articles. Sentiment analysis is one of the fastest-growing research areas in computer science, making it challenging to keep track of all the activities in the area. In our project, we aim to achieve our goal of accurately predicting a user's sentiment by analyzing the data provided using different types of input data.

## Working Demo

[![Working Demo Video](https://img.youtube.com/vi/EVJx20iVmuI/0.jpg)](https://www.youtube.com/watch?v=EVJx20iVmuI)


---

## Table of Contents
1. [Introduction](#intro)
2. [Emotion Insight Analyzer Features](#feat)
3. [How to use Emotion Insight Analyzer?](#exec)
4. [Roadmap and Progress](#roadmap)
5. [Case Study](#casestudy)
6. [Contributing to the product](#contribute)
7. [Connect with us](#Connectwithus)
8. [Team Members](#team)

---
<a name="intro"></a>
## Introduction

### What is Emotion Insight Analyzer?
Sentiment analysis, also known as opinion mining, is the process of determining the sentiment or emotional tone in a piece of text, audio, or other forms of data. It involves identifying whether the sentiment expressed is positive, negative, or neutral.

### Why is it important?
<ul>
  <li>Sentiment analysis can help businesses and organizations understand how their customers or users feel about their products, services, or experiences. </li>
  <li>Companies can gauge public opinion about their products or services, track trends, and identify emerging issues or opportunities in the market.</li>
  <li>News agencies and media companies use sentiment analysis to analyze public sentiment towards news articles or events. This helps in generating content that aligns with the interests of the audience.</li>
  <li>Sentiment analysis is used in politics to understand public sentiment towards political candidates, parties, or policies. It is also used to gauge public opinion on social issues.</li>
</ul>

### Why use Emotion Insight Analyzer?

The Emotion Insight Analyzer provides the following:
<ul>
  <li><b>Comprehensive Insights: </b>Different types of data sources provide diverse perspectives. An all-encompassing tool can provide a more comprehensive understanding of public sentiment.</li>
  <li><b>Multichannel Data Analysis:</b> In today's world, opinions and sentiments are expressed across various channels, including social media, customer reviews, audio recordings, and news articles. A tool that can analyze these diverse data sources offers a more accurate picture of public sentiment.</li>
  <li><b>Cost-Efficiency:</b> Instead of using multiple specialized tools, a single tool that can handle multiple data types is cost-effective and streamlines the analysis process.</li>
</ul>

![meme](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/blob/master/assets/images/sentiment_analysis.jpg)

### How was Emotion Insight Analyzer developed?
The complete development was achieved using the following technologies:
- Python3
- Django
- HTML
- CSS
- Scrapy
- Vader Analysis Tool
- Tensorflow
- TextBlob
- NRCLex

Although HTML and CSS are used for the front end, the users can merge the backend logic with any of the front end frameworks they wish to use such as React, and AngularJS.

---

<a name="feat"></a>
## What can Emotion Insight Analyzer do?
|Feature|Description  |
|--|--|
|Product Analysis |```Sentimental analysis of Amazon product reviews```|
|News Analysis  |```Sentimental analysis of any recent news topic```|
|Text Analysis | ```Sentimental analysis and emotion analysis of text input```|
|Audio Analysis   |``` Sentimental analysis of audio file``` |
|File Analysis   |``` Sentimental analysis of text file``` |
|Live Sentimental Analysis   |``` Sentimental analysis of live recorded audio``` |
|Facebook Post Analysis   |``` Sentimental analysis of Facebook Post``` |
|Twitter Post Analysis   |``` Sentimental analysis of Twitter Post``` |
---

<a name="exec"></a>
## How to use Emotion Insight Analyzer?
### Installation
1. Clone this project:
```
git clone https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer.git
```
2. Make sure you are using Python 3.11. You can get it here: https://www.python.org/downloads/release/python-3115/
3. Install dependencies for the project from the root directory of the project:
```
cd <your_repo_dir>
pip install -r requirements.txt
```
4. Install ffmpeg:  
For Windows:  
```
winget install ffmpeg
```  
For Linux (Ubuntu):  
```
sudo apt install ffmpeg
```  
For Mac:  
```
brew install ffmpeg
```
5. Download required NLTK data
```
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```
6. Run Django Server using manage.py (Note: Make sure you are in root directory of the project.)
```
cd <your_repo_dir>
python .\sentimental_analysis\manage.py runserver
```
7. Next, open your browser and type in `localhost:8000` in the search bar to open the user interface of the application.

Now, you are good to go.

![](https://media.giphy.com/media/AgrfqPt5AyiTm/giphy.gif)

### Usage

<a name="usecases"></a>
- Start the django server to get to the homepage
![First](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/blob/master/assets/gifs/Startup.gif)

---
<a name="roadmap"></a>
## Roadmap and Progress
### Past Achievement(Previous Work)
- [x] Facebook post Analysis using Deep Learning Feature inclusion
- [x] Twitter post Feature inclusion
- [x] Text analysis for Spanish language inclusion

### Current Achievements
☑️  Text analysis for French language inclusion<br>
☑️  Emotion detection for English text<br>
☑️  UI Improvement for enriching User interaction with the Application<br>
☑️  Documentation Improvement for reflecting project's value accurately<br>
☑️  Addition of Builds and Workflows for better development activities<br>

### Future Scope
- [ ] Implement User Authentication to store the history of each User
- [ ] Recommendation System based on Product Analysis Results 
- [ ] Enhance the Product Analysis by considering the number of users rated for each Product!
- [ ] Add support for more languages in text analysis!
      
---  
<a name="casestudy"></a>
## Case Study: Amazon Product Review Sentiment and Text Analysis
We have done a Case Study for our Sentiment Analysis Project. It can be found [here](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/blob/master/Case_Study.md).

---
<a name="contribute"></a>
## Eager to Contribute?
To Contribute to our application, please refer to [CONTRIBUTING.md](https://github.com/Fall24-SE-ASK/Emotion-Insight-Analyzer/blob/master/CONTRIBUTING.md)

---

<a name="team"></a>
## Team Members

- Ajith Kanumuri
- Suhas Adidela
- Venkata Krishna Mangapuram
