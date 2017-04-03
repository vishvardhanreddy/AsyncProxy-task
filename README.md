
This is a Simple asynchronous HTTP proxy with range header and range query parameter support. This progam fulfills following requirements.



## Running using Docker

```
docker-compose pull
docker-compose up -d
```

To run the proxy on different port or address edit the environment section in docker-compose.yml.

Your task is to build an asynchronous HTTP proxy (see definition in RFC2616) complying to the requirements specified below.

Requirements

Range requests must be supported as defined in RFC2616, but also via range query parameter.

HTTP 416 error must be returned in case where both header and query parameter are specified, but with a different value.

Program must start with a single command docker-compose up.

Proxy must be reachable at http://<docker-host>:8080 .

Usage statistics must be available at http://<docker-host>:8080/stats

total bytes transferred
uptime
Code must run with Python 3.5+.

Code must be delivered as a link to public GitHub repository.

## Usage
### Basic usage

```
curl -x http://<proxy_host>:<proxy_port> <request url> -o <destination_file>
```

### With range query parameter

```
curl -x http://<proxy_host>:<proxy_port> <url>?range=bytes=0-9999 -o <destination_file>
```  
  
### Statistics
Stat page can be viewed at this following location. 

```
http://<proxy_host>:<proxy_port>/stats
```

```