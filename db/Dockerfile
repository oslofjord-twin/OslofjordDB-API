FROM timescale/timescaledb-ha:pg14-latest
RUN apt-get update \
&& apt-get install -y postgresql-12-postgis-3 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*