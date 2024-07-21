FROM ubuntu:latest

RUN apt-get update && apt-get install -y ansible python3-pip

WORKDIR /ansible

COPY . /ansible

RUN pip3 install jinja2

CMD ["ansible-playbook", "-i", "hosts", "webserver.yml", "-e", "web_server=nginx vhost_name=my_site server_name=example.com document_root=/var/www/html"]
