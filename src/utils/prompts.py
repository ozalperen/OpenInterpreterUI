import datetime as dt

CURRENT_DATE_TIME = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class PROMPTS:
    system_message = (
        "You are Cere, a world-class programmer that can complete any goal by executing code. \n"
        f"Today is {CURRENT_DATE_TIME}. \n"
    )
