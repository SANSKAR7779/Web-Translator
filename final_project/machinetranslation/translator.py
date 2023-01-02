"""This module converts fr-en and en-fr."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey=os.environ['J-tuFBJh6VFTV9NkNYEcidpyhjUwT6GPKaPUhmQSI8Ln']
# pylint: disable=line-too-long
url=os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/7ebc4109-21fd-49fc-9132-20f81775e8c8']
# pylint: enable=line-too-long

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishtofrench(englishtext):
    #write the code here
    """Function translating language en-fr."""
    frenchtranslation=language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    return frenchtranslation.get("translation")[0].get("translation")

def frenchtoenglish(frenchtext):
    #write the code here
    """Function tranlating language fr-en."""
    englishtranslation=language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    return englishtranslation.get("translation")[0].get("translation")
