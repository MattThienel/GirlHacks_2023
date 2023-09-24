# GirlHacks_2023
### GirlHacks 2023 Hackathon project following the space theme. Project detects type of trash disposed on the ISS to provide statistical analysis to reduce waste.
## Inspiration
### We wanted to solve a real problem during this hackathon following the space theme. During our research we found on Northrop Grumman's website that over 10 years they have delivered approximately 130,000 pounds of cargo, and have transferred 91,000 pounds of waste from the International Space Station. We wanted to figure out a way to deliver less wasteful material on to the ISS by classifying what is being wasted. This data could be analyzed before a resupply to pinpoint areas where there are more waste.
## What it does
### Our project classifies images of the waste produced using TensorFlow into their material type. That data is stored into a Redis database that can be analyzed to aid in pinpointing the areas of the most waste. We also designed a website using Figma to assist in analyzing this data in an easy to understand manner.
![Website design to visualize the data collected and stored in a database.](/images/website.png)
![The output of the python script printing the output of the classifier, along with the image be classified.](/images/output.png)
## How we built it
### We broke up the project into three parts, the UI design, AI training and the Redis Database implementation. Through careful planning, we allowed our team of three to work on each part separately but in a way to easily integrate each part together once each individual part was completed. 
## Challenges we ran into
### The image classifier data that we ended up using did not provide accurate results and we did not have time to fix it or find and implement another dataset. Additionally, we ran into the problem of understanding and integrating Redis properly, but were able to overcome that challenge in the end. As no of us are trained in web development, we had some issues getting the website running.
## Accomplishments that we're proud of
### Seeing as we were all first time hackathon participants and Computer Engineering students, we are all proud of what we were able to accomplish. We were all able to bring ourselves up to speed on the technology that we had little to no prior experience in. 
## What we learned
### We learned a lot about what it takes in order to get things in space, and how hard it is. We also learned a lot about technical aspects. There are many tools designed to streamline the development process, like Figma, Redis, and more! This was the first time we have heard of these services, and we will surely use them again! It was great to come together as a team and design a really interesting project. This was our first hackathon, and we can't wait to attend more!
## What's next for ISS Garbage Classificator
### As happy as we are to have done the progress we have, there are still some holes to fill. The garbage classification model is not as perfect as we would like it to be, and still gets some things wrong. We would love to be able to feed it more data in the future. We would also like to flesh out the UI in a more expansive way. We also would love to include a physical design, so the trash can be autonomously collected and sorted.
