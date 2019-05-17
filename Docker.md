
# Docker知识储备

## 1:Orientation and set up

1. **Install required packages**. `yum-utils` provides the `yum-config-manager` utility, and `device-mapper-persistent-data` and `lvm2` are required by the `devicemapper` storage driver.（安装需要的yum包）

    ``` bash
    $ sudo yum install -y yum-utils \
    device-mapper-persistent-data \
    lvm2
    ```

2. Use the following command to set up the `stable` repository.(设置yum安装包为稳定版的docker包)

    ```bash
    $ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
    ```

    Optional: Enable the nightly or test repositories.

    ```bash
    sudo yum-config-manager --enable docker-ce-nightly
    sudo yum-config-manager --enable docker-ce-test
    sudo yum-config-manager --disable docker-ce-nightly
    sudo yum-config-manager --disable docker-ce-test
   ```

3. INSTALL DOCKER CE
   * Install the latest version of Docker CE and containerd(安装最新版本):

     ```bash
     sudo yum install docker-ce docker-ce-cli containerd.io
     ```

   * To install a specific version of Docker CE（安装特定版本）, list the available versions in the repo, then select and install:

      ```bash
      yum list docker-ce --showduplicates | sort -r

      docker-ce.x86_64  3:18.09.1-3.el7                     docker-ce-stable
      docker-ce.x86_64  3:18.09.0-3.el7                     docker-ce-stable
      docker-ce.x86_64  18.06.1.ce-3.el7                    docker-ce-stable
      docker-ce.x86_64  18.06.0.ce-3.el7                    docker-ce-stable

      sudo yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io
      ```

    >Install a specific version by its fully qualified package name, which is the package name (`docker-ce`) plus the version string (2nd column) starting at the first colon (`:`), up to the first hyphen, separated by a hyphen (`-`). For example, `docker-ce-18.09.1`.

4. Start Docke

   ```bash
    sudo systemctl start docker
   ```

5. Verify that Docker CE is installed correctly by running the `hello-world` image.

    ```bash
    sudo docker run hello-world
    ```

# Uninstall Docker CE

1. Uninstall the Docker package:
    >$ sudo yum remove docker-ce

2. Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes
    >$ sudo rm -rf /var/lib/docker

```bash
## List Docker CLI commands
docker
docker container --help

## Display Docker version and info
docker --version
docker version
docker info

## Execute Docker image
docker run hello-world

## List Docker images
docker image ls

## List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq
```

---
