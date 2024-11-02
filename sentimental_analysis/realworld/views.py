import os
import json
import csv
from io import StringIO
import subprocess
import shutil
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.template.defaulttags import register
from django.http import HttpResponse
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import nltk
from pydub import AudioSegment
from .newsScraper import *
from .utilityFunctions import *
from nltk.corpus import stopwords
from .fb_scrap import *
from .twitter_scrap import *
import cv2
from deepface import DeepFace
from langdetect import detect
from spanish_nlp import classifiers
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from nrclex import NRCLex

def pdfparser(data):
    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()

    text_file = open("Output.txt", "w", encoding="utf-8")
    text_file.write(data)

    text_file = open("Output.txt", 'r', encoding="utf-8")
    a = ""
    for x in text_file:
        if len(x) > 2:
            b = x.split()
            for i in b:
                a += " "+i
    final_comment = a.split('.')
    return final_comment

def analysis(request):
    return render(request, 'realworld/index.html')

def get_clean_text(text):
    text = removeLinks(text)
    text = stripEmojis(text)
    text = removeSpecialChar(text)
    text = stripPunctuations(text)
    text = stripExtraWhiteSpaces(text)
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    stop_words.add('rt')
    stop_words.add('')
    newtokens = [item for item in tokens if item not in stop_words]

    textclean = ' '.join(newtokens)
    return textclean

def detailed_analysis(result):
    result_dict = {}
    neg_count = 0
    pos_count = 0
    neu_count = 0
    total_count = len(result)

    for item in result:
        cleantext = get_clean_text(str(item))
        sentiment = sentiment_scores(cleantext)
        pos_count += sentiment['pos']
        neu_count += sentiment['neu']
        neg_count += sentiment['neg']

    total = pos_count + neu_count + neg_count
    result_dict['pos'] = (pos_count/total)
    result_dict['neu'] = (neu_count/total)
    result_dict['neg'] = (neg_count/total)

    return result_dict

def input(request):
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        pathname = 'sentimental_analysis/media/'
        extension_name = file.name
        extension_name = extension_name[len(extension_name)-3:]
        path = pathname+file.name
        destination_folder = 'sentimental_analysis/media/document/'
        shutil.copy(path, destination_folder)
        useFile = destination_folder+file.name
        result = {}
        finalText = ''
        if extension_name == 'pdf':
            value = pdfparser(useFile)
            result = detailed_analysis(value)
            finalText = result
        elif extension_name == 'txt':
            text_file = open(useFile, 'r', encoding="utf-8")
            a = ""
            for x in text_file:
                if len(x) > 2:
                    b = x.split()
                    for i in b:
                        a += " " + i
            final_comment = a.split('.')
            text_file.close()
            finalText = final_comment
            result = detailed_analysis(final_comment)
        folder_path = 'sentimental_analysis/media/'
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

        return render(request, 'realworld/results.html', {'sentiment': result, 'text': finalText})
    else:
        note = "Please Enter the Document you want to analyze"
        return render(request, 'realworld/home.html', {'note': note})

def inputimage(request):
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        pathname = 'sentimental_analysis/media/'
        extension_name = file.name
        extension_name = extension_name[len(extension_name)-3:]
        path = pathname+file.name
        destination_folder = 'sentimental_analysis/media/document/'
        shutil.copy(path, destination_folder)
        useFile = destination_folder+file.name
        image = cv2.imread(useFile)
        detected_emotion = DeepFace.analyze(image)
        
        emotions_dict = {'happy': 0.0, 'sad': 0.0, 'neutral': 0.0}
        for emotion in detected_emotion:
            emotion_scores = emotion['emotion']
            happy_score = emotion_scores['happy']
            sad_score = emotion_scores['sad']
            neutral_score = emotion_scores['neutral']

            emotions_dict['happy'] += happy_score
            emotions_dict['sad'] += sad_score
            emotions_dict['neutral'] += neutral_score

        total_score = sum(emotions_dict.values())
        if total_score > 0:
            for emotion in emotions_dict:
                emotions_dict[emotion] /= total_score

        print(emotions_dict)
        finalText = max(emotions_dict, key=emotions_dict.get)
        return render(request, 'realworld/resultsimage.html', {'sentiment': emotions_dict, 'text' : finalText, 'analyzed_image_path': useFile})

def productanalysis(request):
    if request.method == 'POST':
        blogname = request.POST.get("blogname", "")

        text_file = open(
            "Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/ProductAnalysis.txt", "w")
        text_file.write(blogname)
        text_file.close()

        spider_path = r'Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_review.py'
        output_file = r'Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/reviews.json'
        command = f"scrapy runspider \"{spider_path}\" -o \"{output_file}\" "
        result = subprocess.run(command, shell=True)

        if result.returncode == 0:
            print("Scrapy spider executed successfully.")
        else:
            print("Error executing Scrapy spider.")
       
        with open(r'Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/reviews.json', 'r') as json_file:
            json_data = json.load(json_file)
        reviews = []

        for item in json_data:
            reviews.append(item['Review'])
        finalText = reviews
        result = detailed_analysis(reviews)
        return render(request, 'realworld/results.html', {'sentiment': result, 'text' : finalText})
    else:
        note = "Please Enter the product blog link for analysis"
        return render(request, 'realworld/productanalysis.html', {'note': note})

def text_emotion_analysis(text):
    emotion_counts = {}
    text_emotion = NRCLex(text)
    for emotion, score in text_emotion.raw_emotion_scores.items():
        emotion_counts[emotion] = emotion_counts.get(emotion, 0) + score
    return emotion_counts

def textanalysis(request):
    if request.method == 'POST':
        text_data = request.POST.get("textField", "")
        final_comment = text_data.split('.')
        result = {}
        finalText = final_comment
        lang = determine_language(final_comment)
        if lang == "en":
            result = detailed_analysis(final_comment)
            result['emotions'] = text_emotion_analysis(' '.join(final_comment))
        elif lang == "es":
            sc = classifiers.SpanishClassifier(model_name="sentiment_analysis")
            result_string = ' '.join(final_comment)
            result_classifier = sc.predict(result_string)
            result = {
                'pos': result_classifier.get('positive', 0.0),
                'neu': result_classifier.get('neutral', 0.0),
                'neg': result_classifier.get('negative', 0.0)
            }
        elif lang == "fr":
            text = ' '.join(final_comment)
            blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
            polarity = blob.sentiment[0]
            
            # Estimate separate scores
            if polarity > 0.1:
                result =  {"pos": polarity, "neg": 0.0, "neu": 1 - polarity}
            elif polarity < -0.1:
                result =  {"pos": 0.0, "neg": abs(polarity), "neu": 1 - abs(polarity)}
            else:
                result = {"pos": 0.0, "neg": 0.0, "neu": 1.0}
        else:
            result = {'error': f'{lang} is not supported yet!'}
        return render(request, 'realworld/results.html', {'sentiment': result, 'text' : finalText})
    else:
        note = "Enter the Text to be analysed!"
        return render(request, 'realworld/textanalysis.html', {'note': note})
    
def determine_language(texts):
    langs = []
    try:
        for text in texts:
            langs.append(detect(text))
    except Exception as e:
        # Handle potential exceptions when using langdetect
        print(f"Error detecting language: {e}")
        return False
    unique_langs = list(set(langs))
    if len(unique_langs) != 1:
        return False
    return unique_langs[0]

    
def fbanalysis(request):
    if request.method == 'POST':       
        current_directory = os.path.dirname(__file__)
        result = fb_sentiment_score()
       
        csv_file_fb = 'fb_sentiment.csv'
        csv_file_path = os.path.join(current_directory, csv_file_fb)

        # Open the CSV file and read its content
        with open(csv_file_path, 'r') as csv_file:
            # Use DictReader to read CSV data into a list of dictionaries
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        text_dict = {"reviews" : data}
        print("text_dict:",text_dict["reviews"])
        # Convert the list of dictionaries to a JSON array
        json_data = json.dumps(text_dict, indent=2)

        reviews = []

        for item in text_dict["reviews"]:
            #print("item :",item)
            reviews.append(item["FBPost"])
        finalText = reviews

       
        return render(request, 'realworld/results.html', {'sentiment': result, 'text' : finalText})
    else:
        note = "Please Enter the product blog link for analysis"
        return render(request, 'realworld/productanalysis.html', {'note': note})

def twitteranalysis(request):
    if request.method == 'POST':       
        current_directory = os.path.dirname(__file__)
        result = twitter_sentiment_score()
       
        csv_file_fb = 'twitt.csv'
        csv_file_path = os.path.join(current_directory, csv_file_fb)

        # Open the CSV file and read its content
        with open(csv_file_path, 'r') as csv_file:
            # Use DictReader to read CSV data into a list of dictionaries
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        text_dict = {"reviews" : data}
        print("text_dict:",text_dict["reviews"])
        # Convert the list of dictionaries to a JSON array
        json_data = json.dumps(text_dict, indent=2)

        reviews = []

        for item in text_dict["reviews"]:
            #print("item :",item)
            reviews.append(item["review"])
        finalText = reviews

       
        return render(request, 'realworld/results.html', {'sentiment': result, 'text' : finalText})
    else:
        note = "Please Enter the product blog link for analysis"
        return render(request, 'realworld/productanalysis.html', {'note': note})

def audioanalysis(request):
    if request.method == 'POST':
        file = request.FILES['audioFile']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        pathname = "sentimental_analysis/media/"
        extension_name = file.name
        extension_name = extension_name[len(extension_name)-3:]
        path = pathname+file.name
        result = {}
        destination_folder = 'sentimental_analysis/media/audio/'
        shutil.copy(path, destination_folder)
        useFile = destination_folder+file.name
        text = speech_to_text(useFile)
        finalText = text
        result = detailed_analysis(text)

        folder_path = 'sentimental_analysis/media/'
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return render(request, 'realworld/results.html', {'sentiment': result, 'text' : finalText})
    else:
        note = "Please Enter the audio file you want to analyze"
        return render(request, 'realworld/audio.html', {'note': note})


def livespeechanalysis(request):
    if request.method == 'POST':
        my_file_handle = open(
            'sentimental_analysis/realworld/recordedAudio.txt')
        audioFile = my_file_handle.read()
        result = {}
        text = speech_to_text(audioFile)

        finalText = text
        result = detailed_analysis(text)
        folder_path = 'sentimental_analysis/media/recordedAudio/'
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return render(request, 'realworld/results.html', {'sentiment': result, 'text' : finalText})


@csrf_exempt
def recordaudio(request):
    if request.method == 'POST':
        audio_file = request.FILES['liveaudioFile']
        fs = FileSystemStorage()
        fs.save(audio_file.name, audio_file)
        folder_path = 'sentimental_analysis/media/'
        files = os.listdir(folder_path)

        pathname = "sentimental_analysis/media/"
        extension_name = audio_file.name
        extension_name = extension_name[len(extension_name)-3:]
        path = pathname+audio_file.name
        audioName = audio_file.name
        destination_folder = 'sentimental_analysis/media/recordedAudio/'
        shutil.copy(path, destination_folder)
        useFile = destination_folder+audioName
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

        audio = AudioSegment.from_file(useFile)
        audio = audio.set_sample_width(2)
        audio = audio.set_frame_rate(44100)
        audio = audio.set_channels(1)
        audio.export(useFile, format='wav')

        text_file = open("sentimental_analysis/realworld/recordedAudio.txt", "w")
        text_file.write(useFile)
        text_file.close()
        response = HttpResponse('Success! This is a 200 response.', content_type='text/plain', status=200)
        return response

def newsanalysis(request):
    if request.method == 'POST':
        topicname = request.POST.get("topicname", "")
        scrapNews(topicname)

        with open(r'sentimental_analysis/realworld/news.json', 'r') as json_file:
            json_data = json.load(json_file)
        news = []
        for item in json_data:
            news.append(item['Summary'])
        finalText = news
        result = detailed_analysis(news)
        return render(request, 'realworld/results.html', {'sentiment': result, 'text' : finalText})
    else:
        return render(request, 'realworld/index.html')

def speech_to_text(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text


def sentiment_analyzer_scores(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    return score


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key, 0)
