FROM google/cloud-sdk:310.0.0-alpine

ENV PATH="/scripts:$PATH"

RUN apk add --update --no-cache openjdk8-jre
RUN gcloud components install cloud-datastore-emulator beta --quiet

VOLUME /opt/data

COPY ./entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/*

ENTRYPOINT ["entrypoint.sh"]
