# Django-Pyinstaller

Pyinstaller used as follows:-

Generate the manage.spec file to add datas and hidden imports to it, then run pyinstaller
```
pyi-makespec manage.py
```
```
$pyinstaller --name=resnet manage.spec
```
And with --onefile to create single executable with everything in it.

```
$pyinstaller --name=resnet manage.spec --onefile
```


Run the server with:-
```
.dist/resnet/resnet runserver --noreload
```

Errors Encountered:-

-> GDAL thing

-> 'resnet18.joblib' not found , solved by https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile

-> module urls.py not found , solved by deleting dist/build generated from previous run of pyinstaller(-_-)(tried many things from google).
