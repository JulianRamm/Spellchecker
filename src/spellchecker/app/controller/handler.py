import json

from app.spellchecker import SpellChecker
from app.connectors import db_connector
import datetime
import pytz

instance = SpellChecker()


def spell_check(event, context):
    request_text = json.loads(event.get("body"))["text"]
    request_response = instance.spell_check_sentence(request_text)
    request_id = event.get("requestContext").get("requestId")
    request_date = datetime.datetime.fromtimestamp(float(event.get("requestContext").get("requestTimeEpoch") / 1000),
                                                   pytz.timezone("America/Bogota"))
    db_connector.insert_row_into_request_history(request_id, request_date, request_text, request_response)
    body = {
        "text": request_response,
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def request_history(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(db_connector.get_all_rows_from_request_registry())
    }
