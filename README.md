
This is a Simple asynchronous HTTP proxy with range header and range query parameter support. This progam fulfills following requirements.


Task is to build as an asynchronous HTTP proxy (see definition in RFC2616) complying to the requirements specified below.

Range requests is supported as defined in RFC2616, but also via range query parameter.

HTTP 416 error is returned in case where both header and query parameter are specified, but with a different value.

Program starts with a single command docker-compose up.

Proxy is reachable at http://<docker-host>:8080 .

Usage statistics are available at http://<docker-host>:8080/stats



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

Run Commands

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
