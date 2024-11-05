import datetime, time, requests

# only 10 requests per minute by default (for baseball-reference)
# started from: https://github.com/jldbc/pybaseball/blob/master/pybaseball/datasources/bref.py
class Session():

    def __init__(self, max_per_min : int = 10) -> None:

        self.max_per_min = max_per_min
        self.cnt = 0
        self.session = requests.Session()

    '''
    Helper function 1
    Behavior: handle maximum api call rate: 10 calls per 1 min.
    Usage: called inside fetch().
    '''
    def handle_call_rate(self) -> None:
        
        self.cnt += 1
        
        if self.cnt % self.max_per_min == 0:
            print(F"have called {self.cnt} apis: 1 min break starts") 
            time.sleep(60) 
        
    '''
    Helper function 2
    Behavior: general api call with given url -> return data in json format(dict)
    Usage: called inside other api call functions.
    '''
    def fetch(self, url : str) -> requests.Response:

        response = self.session.get(url)
        self.handle_call_rate()
    
        if response.status_code != 200:
            print(F"response status not 200: {response.status_code}")
            
            # occasionally api server throws this error code
            if response.status_code == 500:
                print("instant server error, trying again.")
                time.sleep(3)
                fetch(url)
            
        return response
        