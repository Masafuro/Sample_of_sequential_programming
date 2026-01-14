FROM mcr.microsoft.com/devcontainers/python:3.11

# 必要に応じてシステムパッケージを追加できますが、
# 本パラダイムの純粋性を保つため、最小限に留めています。
RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*