from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/scrap')
def scrap():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    browser.get('https://lexica.art/')
    title = browser.title
    return title
