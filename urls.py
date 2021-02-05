import elk_logger
from flask import Blueprint

router = Blueprint('router', __name__)

@router.route('/', methods=['GET'])
def send_log():
    logger = elk_logger.create_logger('elk-logger')
    logger.info('hello elk-logstash')
    return 'hello'
