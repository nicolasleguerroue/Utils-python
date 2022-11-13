#!/usr/bin/env python3
#-- coding: utf-8 --

class User:

	def __init__(self, username="defaultUsername", ttl=3600):

		self.name = username
		self.ttl = ttl
