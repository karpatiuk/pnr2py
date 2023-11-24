T_ITINERARY = 'T_ITINERARY'

PATTERN_LINE_NUMBER = r'^\d{1,2}(.\W|\W)'
PATTERN_FLIGHT_NUMBER = r'(([A-Z]{2}\W*\d*)|([A-Z]{1}\d{1}\W*\d*)|(\d{1}[A-Z]{1}\W*\d*))([A-Z]{1}| [A-Z]{1})'
PATTERN_DATE = r'\W[0-9]{2}(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\W'
PATTERN_ONE_CHAR = r'^[A-Z]{1}\W'
PATTERN_WEEK_DAYS = r'^\W(MO|TU|WE|TH|FR|SA|SU)\W'
PATTERN_ITINERARY = r'\W{0,1}([A-Z]{6})( ([A-Z]{2}\d{1,2})|(\*([A-Z]{2}\d{1,2})))'
PATTERN_TIME = (r'(\W([0-9]{3,4})(N|A|P)?(\+([0-9])?|\||(\W\#[0-9]{1})|(\W\-[1-2]{1}))?\W)|(\W([0-9]{3,4})'
                r'(N|A|P)?(\+([0-9])?|\||(\W\#[0-9]{1})|(\W\-[1-2]{1}))?)')
PATTERN_DEP_ARR_DAYS = (r'((MO|TU|WE|TH|FR|SA|SU)\/(MO|TU|WE|TH|FR|SA|SU))|((MO|TU|WE|TH|FR|SA|SU)'
                        r'(MO|TU|WE|TH|FR|SA|SU))|((MO|TU|WE|TH|FR|SA|SU))')
PATTERN_REF_ID = r'(\/DC[A-Z]{2}\*[0-9A-Z]{6})|([A-Z]{2}\/[0-9A-Z]{5,6})'

N_LINE_NUMBER = 'LINE_NUMBER'
N_FLIGHT_NUMBER = 'FLIGHT_NUMBER'
N_DEPARTURE_DATE = 'DEPARTURE_DATE'
N_DAY_OF_WEEK_ONE_CHAR = 'DAY_OF_WEEK_ONE_CHAR'
N_DAY_OF_WEEK_2CHAR = 'N_DAY_OF_WEEK_2CHAR'
N_AIRPORTS = 'AIRPORTS'
N_DEPARTURE_TIME = 'DEPARTURE_TIME'
N_ARRIVAL_TIME = 'ARRIVAL_TIME'
N_ARRIVAL_DATE = 'ARRIVAL_DATE'
N_DEPARTURE_ARR_DAYS = 'DEPARTURE_ARR_DAYS'
N_REF_ID = 'REF_ID'


ITINERARY_LINE = (
    (N_LINE_NUMBER, PATTERN_LINE_NUMBER, True),
    (N_FLIGHT_NUMBER, PATTERN_FLIGHT_NUMBER, True),
    (N_DEPARTURE_DATE, PATTERN_DATE, True),
    (N_DAY_OF_WEEK_ONE_CHAR, PATTERN_ONE_CHAR, False),
    (N_DAY_OF_WEEK_2CHAR, PATTERN_WEEK_DAYS, False),
    (N_AIRPORTS, PATTERN_ITINERARY, True),
    (N_DEPARTURE_TIME, PATTERN_TIME, True),
    (N_ARRIVAL_TIME, PATTERN_TIME, True),
    (N_ARRIVAL_DATE, PATTERN_DATE, False),
    (N_DEPARTURE_ARR_DAYS, PATTERN_DEP_ARR_DAYS, False),
    (N_REF_ID, PATTERN_REF_ID, False)
)

DATE_FORMAT_GDS = '%d%b'
APP_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
CURR_DATE_GDS_FORMAT = '%d%b%Y'
