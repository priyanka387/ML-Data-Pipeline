
import os



##Cloud_API_Details
API_KEY = "76JTIQVFGZEFJOM6" #os.getenv('API_KEY',None)
API_SECRET_KEY = "S68Y4nAJbuq9KiBdMCscPPh2EJLP8WNaS3r68UmU5bYWs1ry8n0Lk0Wa+doDn08F" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER =  "pkc-41p56.asia-south1.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)

## Environment Security 
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)


##Schema Registry key
ENDPOINT_SCHEMA_URL  = "https://psrc-znpo0.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY = "2E7GCZW24WZN4VLV" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "PX6FJexGR+tEGsQc5JyFH/C36Y/5MmmubJXdn5/tdwck7LHdgwgL8jPV9T4Mh7Wo" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf


def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()


