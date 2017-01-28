import yaml_mako
import pprint
import datetime

stream = open( 'example.yaml' )
today = datetime.date.today()
tomorrow = today + datetime.timedelta( 1 )
pprint.pprint( yaml_mako.load( stream, start_date = today, end_date = tomorrow ) )
