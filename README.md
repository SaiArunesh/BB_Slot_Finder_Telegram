# BB_Slot_Finder_Telegram
Big Basket Slot finder with reminder sent via Telegram Bot

Tested on Python 3.8

1. To install python dependencies
```
pip install -r requirements
```
2. Requires Initial One Time Setup of Telegram Bot Visit https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot for instructions
3. Bot Token (you can get from ```@BotFather```) and Chat ID is required for this program to function
4. Paste your token and run **code_to_find_chat_id_and_test_bot.py**
5. Send ```/start``` to the bot from your Telegram Client
6. Bot will reply with your chat ID

Running the main code:  
**Note: preload your cart with atleast 1 item**

1. Paste your token and chat id into **BB_slot.py** and run it
2. Login   
**Note: Sometimes it deafults to Bangalore generic address be sure to click on the address to be delivered**
3. The program will take care of the rest and will send the message "SLOTTTT!!!!!!" to you. 
4. Make sure to enable notification for your Telegram bot in your chat client

Quick Troubleshooting Steps:  

 - Send ```/start``` to bot to make sure it is active before running **BB_Slot.py**

 - To check if bot is working you can use **code_to_find_chat_id_and_test_bot.py**. It should return the chat ID.

 - In case token is forgot  Visit https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot on instructions 

 - In case shell prints an error stating button is not clickable, just click once inside the checkout page.
 
