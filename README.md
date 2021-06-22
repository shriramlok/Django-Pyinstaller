# Django-Pyinstaller

Pyinstaller used as follows:-

Generate the manage.spec file to add datas(classifier folder) and hidden imports and name to it, then run pyinstaller
```
pyi-makespec manage.py
```
```
$pyinstaller manage.spec
```

Run the server with:-
```
./resnet/resnet runserver --noreload
```

Above will create a directory inside dist/ which contain all packages and everything.

We need to add --onefile to create a single executable.

```
$pyinstaller manage.spec --name resnet --onefile --add-data classifier:classifier
```
(Too big executable file,mostly because of torch)(The directory generated from --onedir(default) and the executable from --onefile are same size but just the execitable uses more resources while running). 


Errors Encountered:-

-> GDAL thing

-> 'resnet18.joblib' not found , solved by https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile

-> module urls.py not found , solved by deleting dist/build generated from previous run of pyinstaller(-_-)(tried many things from google).
