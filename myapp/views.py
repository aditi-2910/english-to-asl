from django.shortcuts import render
from django.http import HttpResponse
from nltk.tokenize import word_tokenize
from .utils import convert_eng_to_isl, lemmatize_tokens, filter_stop_words, pre_process
from django.contrib.staticfiles import finders
import nltk


def home_view(request):
    return render(request, "home.html")


def about_view(request):
    return render(request, "about.html")


def animationView(request):
    if request.method == "POST":
        input_text = request.POST.get("sen")
        print("Input Text: ", input_text)
        
        input_text = input_text.lower()
        print("Input Text in Lower Case: ", input_text)

        isl_parsed_token_list = convert_eng_to_isl(input_text)
        print("Parsed Text: ", isl_parsed_token_list)

        pos_tagged = nltk.pos_tag(isl_parsed_token_list)

        lemmatized_isl_token_list = lemmatize_tokens(isl_parsed_token_list, pos_tagged)
        print("Lemmatized: ", lemmatized_isl_token_list)

        filtered_isl_token_list = filter_stop_words(lemmatized_isl_token_list)
        print("Removed Filter words: ", filtered_isl_token_list)

        isl_text_string = ""
        for token in filtered_isl_token_list:
            isl_text_string += token
            isl_text_string += " "

        words = list(isl_text_string.split())
        print("Pre output sentence: ", words)
        f = open("words.txt", "r")
        eligible_words = f.read()
        f.close()
        final_string = ""

        for word in words:
            if word not in eligible_words:
                for letter in word:
                    final_string += " " + letter
            else:
                final_string += " " + word

        words = word_tokenize(final_string)
        print("animation output: ", words)

        return render(request, "animation.html", {"words": words, "text": input_text})
    else:
        return render(request, "animation.html")
