from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi'):
        return 'hey! how is it going!'
    if user_message in ('who are you', 'who are you?'):
        return 'I am Rundong the bot ^^'
    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H;%M:%S')

        return str(date_time)

    return "that's too much for me human >_<"

