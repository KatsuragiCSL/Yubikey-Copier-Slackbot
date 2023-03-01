import os, re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html

yubikeyRE = re.compile("[cbdefghijklnrtuv]{44}")

@app.message(yubikeyRE)
def say_hello_regex(message, say):
    # regular expression matches are inside of context.matches
    otp = re.search(yubikeyRE, message['text']).group()
    say(f"<@{message['user']}>, I got your Yubikey OTP: {otp}!")

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
