# host names, as defined in the `docker-compose.yml`
HN_MESSAGE_BROKER = 'messageBroker'

# get exchages
EXCHANGE_EVENTS = os.environ.get('EXCHANGE_EVENTS')

# the default date format used for encoding and decoding messages
RFC3339_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
RFC3339_REGEX = r'^([0-9]+)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]+)?$'

