#!/bin/bash

install_sf(){

    apk --no-cache update
    apk --no-cache add bash curl gcc wget mysql-client openssl-dev
    apk --no-cache add python3-dev libffi-dev musl-dev py3-virtualenv

    # get binary zip from nexus
    wget -q -O vfc-gvnfm-vnfres.zip "https://nexus.onap.org/service/local/artifact/maven/redirect?r=snapshots&g=org.onap.vfc.gvnfm.vnfres.res&a=vfc-gvnfm-vnfres-res&v=${pkg_version}-SNAPSHOT&e=zip" && \
    unzip vfc-gvnfm-vnfres.zip && \
    rm -rf vfc-gvnfm-vnfres.zip
    wait
    pip install --upgrade setuptools pip
    pip install -r /service/vfc/gvnfm/vnfres/res/requirements.txt
}

add_user(){

    addgroup -g 1000 -S onap
    adduser onap -D -G onap -u 1000
    chown onap:onap -R /service
}

config_logdir(){

    if [ ! -d "/var/log/onap" ]; then
       mkdir /var/log/onap
    fi 
   
    chown onap:onap -R /var/log/onap
    chmod g+s /var/log/onap
    
}

clean_sf_cache(){

    rm -rf /var/cache/apk/*
    rm -rf /root/.cache/pip/*
    rm -rf /tmp/*
}

install_sf
wait
add_user
config_logdir
clean_sf_cache


