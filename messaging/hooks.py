# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "messaging"
app_title = "Messaging"
app_publisher = "Africlouds Ltd"
app_description = "Managed way to send messages to customers through different channels (Email, SMS, etc.) Track deliveries in different channels. Choose which channel to deliver [D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "arwema@africlouds.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/messaging/css/messaging.css"
# app_include_js = "/assets/messaging/js/messaging.js"

# include js, css files in header of web template
# web_include_css = "/assets/messaging/css/messaging.css"
# web_include_js = "/assets/messaging/js/messaging.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "messaging.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "messaging.install.before_install"
# after_install = "messaging.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "messaging.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"messaging.tasks.all"
# 	],
# 	"daily": [
# 		"messaging.tasks.daily"
# 	],
# 	"hourly": [
# 		"messaging.tasks.hourly"
# 	],
# 	"weekly": [
# 		"messaging.tasks.weekly"
# 	]
# 	"monthly": [
# 		"messaging.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "messaging.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "messaging.event.get_events"
# }

