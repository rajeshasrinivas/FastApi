# FastApi



1. Create the Virtual Environment
~~~
   python -m venv my_evn
~~~
2. Activate the Virtual Environment:

On Windows (PowerShell).
~~~
    my_env\Scripts\Activate.ps1
~~~

On macOS/Linux (Bash/Zsh)
~~~
    source my_env/bin/activate
~~~

3. To deactivate the virtual environment, simply type:
~~~   
    deactivate
~~~


Install FastApi
~~~
    pip install fastapi uvicorn pydantic
~~~

Run FastAPI
~~~
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
~~~

# Http Status Codes

2xx: Successful

200 OK	The request is OK (this is the standard response for successful HTTP requests) -  get, post
201 Created	The request has been fulfilled, and a new resource is created - post
204 No Content	The request has been successfully processed, but is not returning any content - delete

3xx: Redirection

4xx: Client Error

400 Bad Request	The request cannot be fulfilled due to bad syntax
401 Unauthorized	The request was a legal request, but the server is refusing to respond to it. For use when authentication is possible but has failed or not yet been provided
402 Payment Required	Reserved for future use
403 Forbidden	The request was a legal request, but the server is refusing to respond to it
404 Not Found	The requested page could not be found but may be available again in the future

5xx: Server Error

500 Internal Server Error	A generic error message, given when no more specific message is suitable
502 Bad Gateway	The server was acting as a gateway or proxy and received an invalid response from the upstream server
503 Service Unavailable	The server is currently unavailable (overloaded or down)
