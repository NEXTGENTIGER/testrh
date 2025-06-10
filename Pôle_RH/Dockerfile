### metasploit/Dockerfile
FROM kalilinux/kali-rolling

RUN apt-get update && \
    apt-get install -y metasploit-framework && \
    rm -rf /var/lib/apt/lists/*

CMD ["msfconsole"]


### openvas/Dockerfile
FROM debian:bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        gnupg curl lsb-release && \
    curl -fsSL https://downloads.greenbone.net/gpg.key | gpg --dearmor -o /usr/share/keyrings/greenbone.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/greenbone.gpg] https://packages.greenbone.net/community-edition/debian bookworm main" > /etc/apt/sources.list.d/greenbone.list && \
    apt-get update && \
    apt-get install -y greenbone-vulnerability-manager && \
    gvm-setup && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 9392

CMD ["gvmd", "--foreground"]


### hydra/Dockerfile
FROM debian:bookworm

RUN apt-get update && \
    apt-get install -y hydra && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["sleep", "infinity"]
