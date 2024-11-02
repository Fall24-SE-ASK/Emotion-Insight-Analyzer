# Project-Location: Emotion-Insight-Analyzer/realworld/

## apps.py:
Used to configure the application for the Django project.

The `RealWorldConfig` class inherits from `AppConfig`, and the attribute `name` is changed to `realworld`, which will be the name of the current application.

Django will use this name to recognize the application and include it in the project.

## views.py:
Contains all the functions that handle sentiment analysis.

### newsanalysis(request):
Makes a POST API call to `scrapNews(topicname)`, where `topicname` is user-given input. The `scrapNews()` function scrapes new articles on this topic and stores their summaries in `news.json`.

The summaries from the JSON are all stored in a `news[]` list. The `detailed_analysis(news)` function is called with `news[]` as input. This function then performs sentiment analysis on the news and provides output.

Finally, the result is rendered through the `render()` function so that the sentiment is displayed to the user using `results.html`.

### analysis(request):
Renders the base analysis page.

### input(request):
Handles the uploading, processing, and sentiment analysis for files such as PDFs or text files.

Determines the file extension and then stores the uploaded file into a temporary location in the file system for further processing. The `detailed_analysis()` function is called with the processed text from the file. The sentiment analysis result is stored and rendered from `realworld/results.html`.

### inputimage(request):
This function is for sentiment analysis on images.

Takes an image as input, determines the extension, and stores the uploaded image in a temporary location. Uses the DeepFace library to perform analysis on the image: each of the sentiment scores is aggregated and normalized.

The dominant emotion is then detected based on the emotion with the maximum score. The emotion and their scores are then rendered.

### productanalysis(request):
The product page link is taken as input.

Uses the product and then calls the spider script `amazon_review.py`, which scrapes Amazon reviews for this product. The reviews are consolidated and stored. The `detailed_analysis()` function is called, which performs sentiment analysis on the consolidated reviews and provides a sentiment output.

The sentiment output is then rendered through `results.html`.

### determine_language(texts):
Uses `detect()` from the `langdetect` library to detect the language based on the input text given.

### fbanalysis(request):
`fb_sentiment_score()` collects reviews from Facebook, consolidates them, and performs sentiment analysis on all these reviews. The result of the sentiment analysis is then rendered.

### twitteranalysis(request):
`twitter_sentiment_score()` collects reviews from Twitter, consolidates them, and performs sentiment analysis on all these reviews. The result of the sentiment analysis is then rendered.

### audioanalysis(request):
Takes an audio file as input, determines the extension, and stores it in a location. Uses `speech_to_text()` (which uses `speech_recognition` from the Google Web Speech API to convert audio to text) to convert audio to text.

Calls `detailed_analysis()` on the text to perform sentiment analysis, and the result is then rendered.

### pdfparser(request):
Converts pdf file to text
