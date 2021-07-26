import dateutil
import datetime
from datetime import date,datetime
import time
import dateutil.parser

class Date_spilt:

    def datetimeconverter(self):
        # get time, to use in a filename
        ts = time.time()
        ds = datetime.fromtimestamp(ts).strftime('%d%m%Y%H%M')
        return ds