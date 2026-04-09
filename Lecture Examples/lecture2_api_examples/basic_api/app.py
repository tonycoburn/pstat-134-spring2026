from fastapi import FastAPI
# create an instance of the FastAPI application:
app = FastAPI()

# telling FastAPI the function right below should handle GET requests sent to the
# "greet" endpoint
@app.get("/greet")
# the function that will run when greet is requested
def greet():
  return {"message": "Hello, friend!"}
# this is a Python dictionary, FastAPI converts these to JSON

# if the file is being run directly ("python app.py"),
if __name__=="__main__":
  import uvicorn
  # start the server. run app, listen only on my local machine, use port 8000
  uvicorn.run(app, host="127.0.0.1", port=8000)
# 127.0.0.1 is the IP address for "localhost", your own computer. it would be the same for any of you. you could also say host="localhost"
# there are lots of port number options. for development, 8000, 5000, 3000, 8888 are conventional. ports range from 0 - 65535. 0 - 1023 usually are reserved. 1024 - 49151 are generally usable (but some may already be in use on your machine, it depends)