`This repository contains about different high level design Implementation and low level Implementation`

## HLD

<details>
<summary><a href="https://github.com/poorvaditya18/system-design">LOAD BALANCER:</a></summary>

- What is a load balancer? A load balancer is a `software` or `hardware` device that keeps any one server from becoming overloaded.
- Why do we need it? Consider an application, let’s say it is a website that people purchase mangos from, that server has a finite amount of memory and CPU. As traffic increases, the single server starts to struggle.
- It helps to distribute load among various resources/servers (s1, s2, s3,...).
- There are many popular ones out there such as NGINX, HAProxy, Traefik, etc.
- In practice, the load balancer acts like a proxy fronting the underlying servers (or backends).
- `Load Balancing Algorithm`: helps to set rules on how to distribute load among different servers.
- There are two primary approaches to load balancing - `Dynamic Load Balancing` and `Static Load Balancing`.

</details>

## LLD
