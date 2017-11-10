# nyumelee
Part of program to help NYU melee players sift through all tournament brackets to see records against various players, display game counts in sets, and see all wins and losses over each season. 

In order to use this program you will need to run initialize.txt in your Mac Terminal. This program will add autodl.txt to the crontab so that it will be run every Friday morning. This file downloads the information about the turnament from the previous thursday night. This is done as an alternative to web API integration because it is much faster to constantly pull data from json files rather than the web. Not yet integrated with Analytics app.
