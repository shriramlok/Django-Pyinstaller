# Django-Pyinstaller

Pyinstaller to be run using:-

```
$pyinstaller manage.spec
```
Run the server with:-
```
.dist/manage/manage runserver --noreload
```

Errors Encountered:-

-> GDAL thing

-> 'resnet18.joblib' not found , solved by https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile

-> module urls.py not found , solved by deleting dist/build generated from previous run of pyinstaller(-_-)(tried many things from google).
