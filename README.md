# About
This repository contains the code needed to run the python service needed to arm, disarm and silence 
the alarm as part of the [Security with Machine Learning Spice Makes Everything Nice](https://medium.com/dvt-engineering/security-with-machine-learning-spice-makes-everything-nice-778c1c3011b5) project.

# System Requirements
* Docker and Docker compose for Raspberry Pi - [How To Install Docker and Docker-Compose On Raspberry Pi](https://dev.to/elalemanyo/how-to-install-docker-and-docker-compose-on-raspberry-pi-1mo) 
* Raspbian 11 (bullseye) OS version - [Install Raspberry Pi OS Bullseye on Raspberry Pi (Illustrative Guide)](https://raspberrytips.com/install-raspbian-raspberry-pi/)
* Git  - [How to Install Git on Raspberry Pi](https://linuxize.com/post/how-to-install-git-on-raspberry-pi/)
# Usage
1. Clone this repository onto your Raspberry Pi using Git
2. Navigate to the directory containing the docker-compose file
3. Update the docker-compose file's `SECURITY_MICRO_SERVICE_HOST_IP` and `ALERTER_RABBITMQ_HOST` environment variables with the IP 
   address of your control hub system (there are a number of ways to find the IP address of RaspberryPi's on your local network, here is one I typically use - [How to Find the Current IP Address of a Raspberry Pi?](https://raspberrytips.com/find-current-ip-raspberry-pi/))
4. If other configurations are needed, you can update the relevant environment variable (but the default should suffice if you are following along with the [Security with Machine Learning Spice Makes Everything Nice](https://medium.com/dvt-engineering/security-with-machine-learning-spice-makes-everything-nice-778c1c3011b5) project)
5. Execute `docker-compose up` in the same directory as the `docker-compose.yml` file

# Help 
If you are stuck and need a hand, please reach out to me via email [piandarduinoguy@gmail.com](piandarduinoguy@gmail.com)