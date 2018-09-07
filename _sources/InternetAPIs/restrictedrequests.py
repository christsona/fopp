# most restricted version
"""
This solution works in runestone - however it is much more limited.
An error does not occur in the same way in the textbook as it does 
for the command line. Since HTTPError is not currently available in
Runestone, I had to change the exception. 
Decode and Encode are not available in Runestone, so there might be
issues with reponses.
Does not use the status attribute for urlopen, would be nice to have
that back.
Does not work on regular web pages (like google or the michigan daily).
Might be because it returns binary data, and can't be converted to a
string because we can't use encode/decode.
"""
from urllib.request import urlopen

class Response:

	def __init__(self, data, url):
		self.text = data
		self.url = url

	def __str__(self):
		return "A response object for the following request: {}".format(self.request_url)


def requestURL(baseurl, params = {}):
	if len(params) == 0:
		return baseurl
	complete_url = baseurl + "?"
	pairs = [str(pair) + "=" + str(params[pair]).replace(" ", "+") for pair in params]
	complete_url += "&".join(pairs)
	return complete_url

def get(baseurl, params = {}):
    user_req = requestURL(baseurl, params)
    try:
        data = urlopen(user_req)
        text_data = data.read().strip()
        if len(text_data) > 0:
            user_resp_obj = Response(text_data, user_req)
            return user_resp_obj
        else:
            return Response("ERROR: You did not get anything back from the response. The data will need to be converted to a string or the query might not be valid.", user_req)
    except:
        return Response("ERROR: We are unable to get a response at this time, likely due to a server error. Try another API or try again later.", user_req)

