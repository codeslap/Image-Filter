# Image Filter

### Description:

&nbsp;
&nbsp;

Image Filter is a web application that allows users to upload image files

and in return receive a filtered version of that image. There are various

filters to choose from including: blur, black and white, sepia, and edges.

<p>
  <img src="bg.png" width="620" title="hover text" title="Image Filter Index">
</p>



The program uses Python with flask for the back end, and HTML and CSS for

the frontend design. It checks to make sure a filter is selected and that a file is 

uploaded. Image Filter supports image bit depths of 24 and 32.

&nbsp;
&nbsp;

Inside the python applicaiton (app.py) are a couple routes for the index

and another path for the download that includes the filename.

It takes a file of any name and adds filtered to the beginning (i.e

image.jpg comes out as filteredimage.jpg when rendered.) I used

threading to delete the images 8 seconds after the POST request is received.


&nbsp;
&nbsp;


Improvements could include a different method of deletion, because if multiple users

or one users filters images too quickly, the old set of images remain in storage.

Another improvement would be to force the download after submitting instead of showing

the image and the user having to right click --> download. Images auto download

for .webp files but didn't work with .jpg or .png.


&nbsp;
&nbsp;


Aside from what was learned in CS50 regarding python,flask, and filters, I also had to

do some research on other topics to complete this project. One of the first tasks I was

struggling to get to work was the download capability of Image Filter. I received many 

error codes before I stumbled upon a wonderful blog that helped me set up the backend for 

uploading a user file to the server and then letting them download the filtered image. (1)


&nbsp;
&nbsp;


Another concept that took some time was calling a function without needing to wait for a 

return. I tried many different methods from various forums such as stackoverflow, Python 

documentation flask documentation and others. Some of them said to use the async module 

and other said to use threading. In the end threading ended up working, when I finally 

read through source (2).In combination with threading I also had to use the time module 

to keep track of time.Both of those modules allowed me to call a function to delete the 

user uploaded files after a certain amount of time (8 seconds).


&nbsp;
&nbsp;


For my frontend design, I used four html files and two static files. My html files were

for the index (main page), download(for download page), aplogy (to handle errors),

and layout. My static files were for styles using css and a background image (anime.jpg)

used in the index. One of the cool new feautures I used was opacity which helped make the 

header that reads "Image Filter" semi-transperent using opacity. I also used bootstrap 

for my selection of filter types. and one last noticeable thing is a copyright at the bottom of the  page 

which would always be visible (even through scrolling), given the page was longer.



### Sources:
(1) - https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask

(2) - https://stackoverflow.com/questions/66024208/call-function-from-another-function-and-move-on-dont-wait-for-finish-python
