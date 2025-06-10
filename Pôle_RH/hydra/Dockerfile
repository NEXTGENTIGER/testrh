### hydra/Dockerfile
FROM debian:bookworm

RUN apt-get update && \
    apt-get install -y hydra && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["sleep", "infinity"]
