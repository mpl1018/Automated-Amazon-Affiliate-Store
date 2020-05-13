### Python script configuration.

In order to run the python script you will need to run the following command with pip. 

```
pip install -r requirements.txt 
```

⚠️Note: It seems that "firebase-tools" only works with Python3.7.5. So try installing these version if the pip install doesn't work.  

### Running script
After intalling all the libraries, setting up your proyect in firebase, downloading your firebase credentials and creating your affiliate account, your are ready to run: 
``` 
python myBot.py 'your firebase category' 'your amazon search'
```
And then magic will happen, amazon results will be in your firebase database. 