# Yubikey-Copier-Slackbot

## Why catching yubikey OTP in Slack?
Many enterprise environment make use of Yubikey as hardware 2FA. For time to time, people keep accidentally triggering the Yubikey touch and sending the OTP to somewhere, mostly, Slack channels. Then they have to immediately delete the OTP embarassingly.    
I could not resist to create a Slack app to automatically capture the OTP and humiliate them (in a friendly way).

## Configuration
None. Check out the steps of creating a Slack app and simply run the script somewhere when the Slack app setup is done.

## Security
While the OTP is somewhat sensitive, it is not the end of the day if you accidentally exposed it. See [this post]()

## Demo
(Obviously not an output from my own Yubikey with critical usage)
![image](https://user-images.githubusercontent.com/44156690/222180017-c72ddec2-44c3-4b88-84f7-214440e35561.png)
