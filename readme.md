### To run local server:
```
$ python app.py
```

### Deploy on Heroku:
Details can be found here: 
https://dash.plotly.com/deployment

Follow the instruction until Deploy the app

### Troubleshooting:
```
fatal: 'heroku' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```
fix it by:
```
$ heroku git:remote -a YourAppName
```

Setting Config Vars for Mapbox token in Heroku->App->Settings

Use Python for Buildpacks
