#!/usr/bin/env python
# -*- coding: utf-8 -*-
from instabot import InstaBot

bot = InstaBot(login=["login1", "login2"], password=["password1", "password2"],
               like_per_day=1000,
               comments_per_day=0,
               tag_list=['mihabodytec','ems', 'xbody'],
               max_like_for_one_tag=50,
               follow_per_day=150,
               follow_time=5*60*60,
               unfollow_per_day=150,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0,
               prox =[{"http" : "http://107.151.152.219:80"},{"http" : "http://107.151.152.222:80"} ]
               )


bot.new_auto_mod()
