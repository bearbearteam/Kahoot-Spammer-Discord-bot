"""A simple Kahoot Flooder made in Python with Selenium."""
#credits : https://github.com/stampixel/Kahoot-Spammerl
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from time import sleep
from names import FIRST, LAST
from random import choice
from sys import platform
bot = commands.Bot(command_prefix='.')
@bot.command()
async def kahoot(ctx,gamepin,namee):

  PATH = ""
  if platform == "linux":
      PATH = "chromedriver/chromedriverlinux"
  elif platform == "darwin":
      PATH = "chromedriver/chromedrivermac"
  elif platform == "win32":
      PATH = "chromedriver/chromedriverwindows.exe"
  USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/" \
               "537.36 (KHTML, like Gecko) Chrome/" \
               "87.0.4280.88 Safari/537.36"
  tab_number = 0
  

  # Getting the required user input
  pin_input = gamepin
  name_choice = ""
  bot_name_input = namee
  bot_amount_input = int(10)
  
  await ctx.send('sending bots')
  
  # Declaring the options
  options = webdriver.ChromeOptions()
  options.headless = True
  options.add_argument(f"user-agent={USER_AGENT}")
  options.add_argument("--window-size=1920,1080")
  options.add_argument("--ignore-certificate-errors")
  options.add_argument("--allow-running-insecure-content")
  options.add_argument("--disable-extensions")
  options.add_argument("--proxy-server='direct://'")
  options.add_argument("--proxy-bypass-list=*")
  options.add_argument("--start-maximized")
  options.add_argument("--disable-gpu")
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--no-sandbox")
  driver = webdriver.Chrome(executable_path=PATH, options=options)


# Main loop that runs the amount of times the user specifies
  def create_bot(tab, pin, bot_name):
      """
      Create a bot.
  
      Uses the pin and name to create as many bots as the user wants.
  
      :param tab: Keeps track of which tab the browser is on.
      :param pin: The pin for the Kahoot.
      :param bot_name: The name for each bot to be created.
      :return: None
      """
      if tab != 0:
          driver.execute_script("window.open('');")
          driver.switch_to.window(driver.window_handles[tab])
  
      # Navigating to Kahoot! (headless), then joining the game using
      # the provided pin and name the amount of times specified
      driver.get("https://kahoot.it")
  
      # Sending the bots
      pin_entry = driver.find_element_by_id("game-input")
      pin_entry.send_keys(pin)
      pin_entry.send_keys(Keys.RETURN)
      try:
          WebDriverWait(driver, 1).until(
              ec.presence_of_element_located(
                  (By.ID, "nickname")))
          bot_name_entry = driver.find_element("nickname")
          bot_name_entry.send_keys(bot_name + str(i + 1))
          bot_name_entry.send_keys(Keys.RETURN)
      except TimeoutException:
          sleep(6)
      driver.delete_all_cookies()
  
  
  for i in range(bot_amount_input):
      create_bot(tab_number, pin_input, bot_name_input)
      tab_number += 1
  driver.quit()
  await ctx.reply('done')
# Once the bots have been delivered, let the user wait until they want to
# delete them.
@bot.event
async def on_ready():
  print('ready')
bot.run('token')
