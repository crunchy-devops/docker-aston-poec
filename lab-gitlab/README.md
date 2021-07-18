# lab-gitlab


## Configure
```shell
cd 
cd docker-aston-poec
source venv/bin/activate
docker-compose up -d
docker exec -it lab-gitlab_gitlab-ce_1 bash
# or use portainer
gitlab-rails console -e production
# enter these following lines
   user = User.where(id: 1).first
   user.password = '12345678'
   user.password_confirmation = '12345678'
   user.save
   exit
```

## First steps
Import a project from your github repo  
Select user and edit profile  
select ssh keys
```shell
ssh-keygen -t rsa -b 4096
# copy the public key in gitlab
vi ~/.ssh/id_rsa.pub
# get a repo locally
git clone ssh://git@localhost:2222/root/todo-flask-postgres.git
```

## Merge request
Create a branch
```shell
git checkout -b dev
# change 
