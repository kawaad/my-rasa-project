# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

 
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from urllib.request import urlopen
from bs4 import BeautifulSoup

class ultima_noticia(Action):

	def name(self) -> Text:
		return "ultima_noticia"
	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		url = urlopen("https://www.ifb.edu.br/brasilia/noticiasbrasilia")
		soup = BeautifulSoup(url.read(), "html.parser")
		link_noticia = []
		for item in soup.select(".tileHeadline"):
			link = ("https://www.ifb.edu.br/brasilia/noticiasbrasilia" + item.a.get('href'))
			link_noticia.append(link)
		Link=link_noticia[0]
		#print("Link: ",tracker.get_slot('LINK'))
		#dispatcher.utter_message(utter_site,Link)
		dispatcher.utter_template("utter_site",tracker,link=Link)
		return []
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
