from pixivpy3 import *
import random
api = AppPixivAPI()
api.login("user_yaew2385", "Le168814")

json_result = api.search_illust("Gay", search_target='partial_match_for_tags', sort='date_desc', duration=None)
gegs = random.choices(json_result.illusts, k=3)
for ill in gegs:
    api.download(ill.image_urls.large)