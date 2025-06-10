### metasploit/Dockerfile
FROM kalilinux/kali-rolling

RUN apt-get update && \
    apt-get install -y metasploit-framework && \
    rm -rf /var/lib/apt/lists/*

CMD ["msfconsole"]
