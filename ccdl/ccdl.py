import time
import os
import shutil
import glob
import subprocess
import datetime
import re
import sys
import json 
import youtube_dl
from colorama import Fore, Style

class CcDownload:

  def download(self):
    success = True
    print(Fore.GREEN + "\nDownloading files" + Style.RESET_ALL)
    return_value = youtube_dl.YoutubeDL().download([self.url])
    if return_value > 0:
      print(Fore.RED + "\nFailed to downlaod file via YoutubeDL\n" + Style.RESET_ALL)
      success = False
    return success
    

  def get_new_filename(self, show, text):
    print(Fore.GREEN + "\nDetermining new file name" + Style.RESET_ALL)
    episodepattern = re.compile("ep-(\d+)(\d\d\d)/*$")
    match = episodepattern.search(text)
    season = match.group(1)
    episode = match.group(2)
    return show + "." + "S" + season + "E" + episode + ".mp4"

  def create_temp_dir(self):
    print(Fore.GREEN + "\nCreating temporary folder" + Style.RESET_ALL)
    ts = str(time.time()).split(".")[0]
    self.temp_dir = "/tmp/" + ts
    os.mkdir(self.temp_dir)

  def merge(self):
    print(Fore.GREEN + "\nMerging files" + Style.RESET_ALL)
    new_files = []
    i = 1
    for file_name in sorted(os.listdir(os.getcwd())):
      file_name_out = str(i) + "_out.ts"
      subprocess.call("avconv -ss 0 -i \"" + file_name + "\" -vcodec libx264 -acodec aac -bsf:v h264_mp4toannexb -f mpegts -strict experimental -y \"" + file_name_out + "\"", shell=True)
      new_files.append(file_name_out)
      i = i + 1
    mergecall = "avconv -i concat:\"" + "|".join(new_files) + "\" -c copy -bsf:a aac_adtstoasc -y \"" + self.new_filename + "\""
    print(mergecall)
    subprocess.call(mergecall, shell=True)

  def set_url(self, url):
    self.url = url
    found_show = False
    for show in  self.config_data["shows"]:
      if show["regex"] in url:
        self.show = show["name"]
        self.copy_to = show["copy_to"]
        found_show = True
        break
    if not found_show:
      print(Fore.RED + "\nCould not determine show using fallback directory " + self.config_data.fallback_dir  + Style.RESET_ALL)
      self.show = "unknown"
      self.copy_to = self.config_data.fallback_dir

  def read_configuration(self):
    home = os.path.expanduser("~")
    config_path = os.path.join(home, ".ccdl-config")
    try:
      json_data_file =  open(config_path)
      config_data = json.load(json_data_file)
      self.config_data = config_data
      return True
    except ValueError as e:
      print(Fore.RED + "\nConfig file " + config_path + " has invalid format: " + str(e) + "\n" + Style.RESET_ALL)
    except FileNotFoundError:
      print(Fore.RED + "\nCould not find config file at " + config_path + "\n" + Style.RESET_ALL)
    return False

  def check_configuration(self):
    return True 

  def copy(self):
    print(Fore.GREEN + "\nCopying files" + Style.RESET_ALL)
    shutil.copy(self.temp_dir + "/" + self.new_filename, self.copy_to)

  def clean(self):
    print(Fore.GREEN + "\nCleaning up\n" + Style.RESET_ALL)
    shutil.rmtree(self.temp_dir)

  def run(self, url):
    read_config = self.read_configuration()
    if not read_config:
      return 1
    check_config = self.check_configuration()
    if not check_config:
      return 1
    self.set_url(url)
    cwd = os.getcwd()
    self.create_temp_dir()
    os.chdir(self.temp_dir)
    try:
      download = self.download()
      if not download:
        return 1
      self.download()
      self.new_filename = self.get_new_filename(self.show,self.url)
      self.merge()
      self.copy()
    except:
      print(Fore.RED + "\nUnexpected error:" + str(sys.exc_info()[0]) + "\n" + Style.RESET_ALL)
      return 1
    finally:
      try:
        self.clean()
      finally:
        os.chdir(cwd)
    return 0

