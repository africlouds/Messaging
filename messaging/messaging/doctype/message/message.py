# -*- coding: utf-8 -*-
# Copyright (c) 2017, Africlouds Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import requests
from frappe import _

class Message(Document):
	def on_submit(self):
		self.send()

	def send(self):
		if self.channel == "Email":
			self.send_email()
		elif self.channel == "SMS":
			self.send_sms()

	def send_email(self):
		from frappe.email.queue import send
		send(recipients=self.recipient,
			subject = _(self.type),
			message = self.message
			)

	def send_sms(self):
		api_key = "a5e3910e"
		api_secret = "2b9050f2d38347cc"
		payload = {
			'api_key': "a5e3910e",
			'api_secret': "2b9050f2d38347cc",
			'to': self.recipient,
			'from': "WASAC",
			'text': self.message 
		}
		requests.post("https://rest.nexmo.com/sms/json", data=payload)
