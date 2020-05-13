# Automated Amazon Affiliate Store.
    
>⚠️ Disclaimer: All the money made with this project will be sent to [SavetheChildren](https://www.savethechildren.es/donacion-ong/donar-coronavirus-en-espana-familias-vulnerables), to help needy families with this Coronavirus crisis in Spain. 

This project consists in a completely automated Amazon Affiliate Store. It’s like a normal affiliate store, but automated. 🤗

## How does it make money? 💸️
It's simple. When you register yourself into the Amazon Affiliates Program, you can get an affiliate link for every product on Amazon. 
When someone buys something through that link, you get your commision (up to 10%). 
You can check commission rates and more [here](https://afiliados.amazon.es/help/operating/schedule)	

## How does it work? ⚙️
I think that an outline will make it more understandable: 
![Image of Yaktocat](https://raw.githubusercontent.com/mpl1018/Automated-Amazon-Affiliate-Store/master/readmeImages/esquema.png)
The interesting part of all this, is the automation part. In order to keep the store stock updated, I made a Python script (myBot.py) that scrapes amazon search results, adds them to your store and deletes old items. 
Using a GCL VM, you can write the following cronjob: 
```
# m h  dom mon dow   command
1 1 * * * /route/to/Python-3.7.5/python /route/to/bot/myBot.py 'your firebase category' 'your amazon search' >
```
For example: 
```
1 4 * * * /home/mascarillavirus/Python-3.7.5/python /home/mascarillavirus/bot/myBot.py guantes guantes desechables 
```
> Note: I used an scraper instead of Amazon PA API because this api is only avalaible for stores that already have a great amount of sells (not my case).
## Getting Started 🚀
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
- 1-[Click here for the vue project instructions](https://github.com/mpl1018/Automated-Amazon-Affiliate-Store/tree/master/app)
- 2-[Click here for the python sript instructions](https://github.com/mpl1018/Automated-Amazon-Affiliate-Store/tree/master/bot)

### Built with 
- [Vue.js](https://vuejs.org/)
- [Firebase](https://firebase.google.com/?hl=es)
- [Google Cloud Platform](https://cloud.google.com/)
- [Selenium](https://www.selenium.dev/)