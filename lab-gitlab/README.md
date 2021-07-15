
```shell
cd 
cd docker-aston-poec
source venv/bin/activate
docker-compose up -d
docker exec -it lab-gitlab_gitlab-ce_1 bash
gitlab-rails console -e production
# enter these following lines
   user = User.where(id: 1).first
   user.password = '12345678'
   user.password_confirmation = '12345678'
   user.save
   exit
```