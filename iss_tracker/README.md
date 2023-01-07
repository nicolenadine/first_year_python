# Day 33 International Space Station Tracker

Based on the coded constant values this application will monitor the location of the ISS
and send a notification email when it is above the specified location.


My goal with this applicaiton was to practice interacting with two APIs 
* [ISS Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now)
* [Sunrise & Sunset](https://sunrise-sunset.org/api)

I also explored SMTP through python's SMTPLIB package. 

### UPDATE 1/8/2023
I recently learned about using environment variables to improve the security of my code. 
So, I updated all of the variables that would contain private data (previous I left it as empty strings)
to instead use the os module to utilize environment variables. 

### Enjoy!
