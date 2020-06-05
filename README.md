# Libpostal Python Rest Api

This project aims to create a microservice as a rest api that gets concatenated address and returns as a parsed address object.

For this purpose it uses [pypostal](https://github.com/openvenues/pypostal) and  [libpostal](https://github.com/openvenues/libpostal) which is a C library for parsing/normalizing street addresses around the world using statistical NLP and open data. It is trained on over 1 billion addresses in every inhabited country on Earth. 

For managing deploy and containarization it uses Docker. Docker installs required packages and installs libpostal C library. 

API is created in Python with flask.


##  Build and Run

Firstly we create the docker image 

```sh
$ docker build -t fridaychallenge . 
```

And then we can  run this image and bind to 4444 port

```sh
$ docker run -d --name fridaychallenge -p 4444:4444  fridaychallenge 
```

We can now open demo page with test addresses, also we can enter any address to input and parse
```sh
http://localhost:4444/demo
```

Also we can use api endpoint to post address and get parsed address

```sh
curl -XPOST -H "Content-type: application/json" -d '{
	"address":"200 Broadway Av"
}' 'http://localhost:4444/parseAddress'
```