from instapy import InstaPy
from selenium import webdriver


# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder

dont_like = []
ignore_words = []
friend_list = []

# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")



InstaPy(username="cyclingsteven", password="Pickone1!", nogui=True)\
  .login()\
  .like_by_tags(['cycling'], amount=10) \
  .end()


