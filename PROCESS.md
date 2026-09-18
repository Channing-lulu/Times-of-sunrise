# Process
First, I chose the data I wanted to obtain.

On the Hong Kong Observatory data website provided by the teacher, I found the method for retrieving the data I wanted. I looked at the examples given on the website, noted the data name, and identified the year and month of the sunrise time I wanted to extract. Because the autumn equinox falls in September, I selected the SRS data for September 2024.

I used DeepSeek to help me understand what fetch.py does, and I modified fetch.py and plot.py myself (at this step, the AI told me where to make changes and why).

Finally, I wanted to study the relationship between sunrise time and the equinox line, so I asked DeepSeek to write a plot2.py to present the data in a different way, which generated a new image.
<!-- Same as assignment 1, same honesty. Which tools you used and for what; one
thing you kept and why it was good; one thing you rejected and why it was wrong.
"I did not use any" is fine if it is true.

If a model wrote most of plot.py, which is likely and allowed, the interesting part
is what you had to correct: did it invent a column name, use pandas where a list
would do, silently drop the rows it could not parse? -->

## Tools
DeepSeek and ChatGpt
## Kept
I kept the AI's suggestions for the code, and I directly used AI coding for the second image. Because I have no programming background, I can only rely on AI explanations to understand the code.
## Rejected
DeepSeek gave me five ways to visualize the data. I chose the one I thought was the most intuitive way to present it