# client-profile

### Описание
TODO
___
### Запуск
Локальный запуск
```commandline
uvicorn main:app --reload
```

Запуск в Docker
```commandline
docker build . -t client-profile:latest
docker run -d -p 7777:8000 client-profile
```

Пуш образа в Docker
```commandline
docker tag client-profile:latest vladsergeichev/client-profile:latest
docker push vladsergeichev/client-profile:latest
```
___
### Тестирование
Проверка покрытия кода тестами
```commandline
coverage run -m pytest
coverage report
```