# Mission-to-Mars

## Purpose
    - It seeks to generate a web scraping process to obtain the information of
    the pages selected automatically through a python script.

## Results
    - As we can see we were able to save the addresses and titles of the images
    in mongo (image A-1).
    
![](https://github.com/maadpeal/Mission-to-Mars/blob/main/Resources/A-1.png)

(image A-1)

    - Then once these images are obtained we can load them in an html file through 
    python and its flask framework (image B-1).
    
![](https://github.com/maadpeal/Mission-to-Mars/blob/main/Resources/B-1.png)

(image B-1)

    - Finally we can see all the information loaded in the html (image C-1).
    
![](https://github.com/maadpeal/Mission-to-Mars/blob/main/Resources/C-1.png)

(image C-1)

## Summary
    - The first thing to do is to inspect the pages from which you want to
    obtain the required information.
    - Review the structures of the pages that we want to obtain the information to know which tags
     we should get (image D-1).
     
![](https://github.com/maadpeal/Mission-to-Mars/blob/main/Resources/D-1.png)

(image D-1)

    - Get the html using SPLINTER
    - Parse the html into an object with BeautifulSoup
    - Once the object is obtained, we can extract all the information that we require to save it in mongo.
    - Once in mongo we can retrieve it through apis calls with flask.
    - We load the data with html enhanced with bootstrap.
    - A diagram to appreciate the general process (image E-1)
    
![](https://github.com/maadpeal/Mission-to-Mars/blob/main/Resources/Diagram.jpg)

(image E-1)
