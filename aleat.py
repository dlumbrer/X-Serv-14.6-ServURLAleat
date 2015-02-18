#!/usr/bin/python

import webapp
import random


class aleatorioServidor(webapp.webApp):

	def process(self, parsedRequest):
		return ("200 OK", "<html><body><p>Hola, <a href='http://localhost:1234/"+
				str(random.randrange(10000000000000)) +
				"'>Dame Otra!!</a></p></body></html>")

if __name__ == "__main__":
	servaleat = aleatorioServidor("localhost", 1234)
