#!/usr/bin/env python

# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0

import argparse
import requests
import smtplib

def main(args):

    # Define Headers
    headers = {'Host' : 'www.inoxmovies.com',
            'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) \
                    Gecko/20100101 Firefox/50.0',
            'Accept' : '*/*',
            'Accept-Language' : 'en-US,en;q=0.5',
            'Accept-Encoding' : 'gzip, deflate, br',
            'X-Requested-With' : 'XMLHttpRequest',
            'Referer' : 'https://www.inoxmovies.com/Index.aspx',
            'Cookie' : 'InoxCityCookie=CityID=Wpu3J5wC3A33ejfMG9heYw==&CityNam \
                    e=Hyderabad; _ga=GA1.2.12057937.1483898455; _gat=1',
            'Connection' : 'keep-alive',
            'Cache-Control' : 'max-age=0',
            'Content-Length' : '0',
            'user-agent' : 'my-app/0.0.1'}
    
    # Request URL
    r = requests.get(args.url,headers=headers)

    if args.movie_name in r.text:
        # Fill values
        gmail_user = args.email
        gmail_pwd = args.password
        FROM = 'noreply@service.com'
        TO = args.email
        SUBJECT = "Please book tickets for " + args.movie_name + " in \
                inoxmovies.com"
        TEXT = "Subject says it all"
        
        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s \
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        
        # Send Email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print 'Successfully sent the mail'
        except:
            print "Failed to send mail"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reminder to \
                                      book tickets in inox movies online.')
    parser.add_argument('-m', '--movie-name',
                        type=str,
                        required=False,
                        default='Khaidi',
                        help='Movie Name')
    parser.add_argument('-e', '--email',
                        type=str,
                        required=False,
                        default='rohitsakala@gmail.com',
                        help='Gmail Id',)
    parser.add_argument('-p', '--password',
                        type=str,
                        required=True,
                        help='Gmail password')
    parser.add_argument('-u', '--url',
                        type=str,
                        required=False,
                        default='https://www.inoxmovies.com/Handlers/TestQuickBookingHandler.ashx?GetMovieList=True&CinemaID=0',
                        help='Inox Movies Movies List URL')
    while(1):
        main(parser.parse_args())
