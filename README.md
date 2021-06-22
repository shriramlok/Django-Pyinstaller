# Django-Pyinstaller

Pyinstaller used as follows:-

Generate the manage.spec file to add datas(classifier folder) and hidden imports to it, then run pyinstaller
```
pyi-makespec manage.py
```
```
$pyinstaller manage.spec
```

Run the server with:-
```
.dist/manage/manage runserver --noreload
```

Above will create a directory which can be distributed.
And with --onefile to create single executable with everything in it.

```
$pyinstaller manage.spec --name resnet --onefile --add-data classifier:classifier
```



Errors Encountered:-

-> GDAL thing

-> 'resnet18.joblib' not found , solved by https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile

-> module urls.py not found , solved by deleting dist/build generated from previous run of pyinstaller(-_-)(tried many things from google).
