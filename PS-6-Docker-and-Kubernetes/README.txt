There are 2 methods for this practical:

1. Install Docker Desktop, then login. After this go to settings -> kubernetes -> enable kubernetes single cluster.
Then you will be prompted to install kubernetes, download and install in docker desktop itself.
Then use these 2 commands to show if both are isntalled:
- docker --version
- kubectl version --client

2. Install wsl using:
- wsl --install

Then install any distro. Then do the following:
- Sudo apt update
- Sudo apt install docker.io
- Curl -sfL https://get.k3s.io | sh -