
This is a Simple asynchronous HTTP proxy with range header and range query parameter support. This progam fulfills following requirements.


Task is to build an asynchronous HTTP proxy (see definition in RFC2616) complying to the requirements specified below.

Range requests must be supported as defined in RFC2616, but also via range query parameter.

HTTP 416 error must be returned in case where both header and query parameter are specified, but with a different value.

Program must start with a single command docker-compose up.

Proxy must be reachable at http://<docker-host>:8080 .

Usage statistics must be available at http://<docker-host>:8080/stats




To run the proxy on different port or address edit add and edit environment section in docker-compose.yml.


Running using Docker

```
docker-compose build --pull
docker-compose up -d

```

Usage stats tracked:

```
total bytes transferred
uptime
```

Requires

```
Python 3.5+
tornado library
```

Default values 

```
proxy_host = 0.0.0.0
proxy_port = 8080

```

To run the proxy on different port or address edit and add edit environment section in docker-compose.yml.

```
curl -x http://<proxy_host>:<proxy_port> <request url> -o <destination_file>
```

With range query parameter

```
curl -x http://<proxy_host>:<proxy_port> <url>?range=bytes=0-9999 -o <destination_file>
```  
  
Stat page can be viewed at this following location. 

```
http://<proxy_host>:<proxy_port>/stats
```
