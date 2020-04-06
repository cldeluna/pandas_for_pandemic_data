# Using Pandas to look at Pandemic Data

Uncertainty is never comfortable and when the uncertainty relates to a new virus that can infect your loved ones rather than your computer, lack of comfort can turn into outright fear.

Often numbers can help with uncertainty but sadly the numbers, as they are being reported to us, are suspect, incomplete, and have no context.   I find that troubling and irresponsible.

Since one of my goals during this period of social distancing is to improve my Python skills, what better way to do that (and improve my Pandas skills) than to look at the numbers myself.

## Numbers are suspect

I think in the US, politics and the media have engendered an environment of fear-mongering and one-upmanship like no other because it is particularly harmful given the situation.   I won't belabor that point.  We see it in action every day.   I'm not saying the situation is not serious, clearly it is. 

My point is that I don't think we are getting the numbers we need to make informed decisions.

Different organizations are counting different things and counting those things differently.  Are the things that need to be counted being counted?

#### It all starts with the data

When I decided to use Pandas and Python to look at this data I had to start with getting data.  That was an eye opener.

[Worldometers](https://www.worldometers.info) had some wonderful data, all sources identified, and nicely put together but I could not find a way to get to raw data.  I suspect that it is available through their subscription service and kudos to [Worldometers](https://www.worldometers.info) as they are not taking this opportunity, unlike so many others, to drive up subscriptions.  You actually have to hunt around to get pricing.  

Eventually I stumbled on to the source of the data that is often cited in the medial, [The Center for Systems Science and Engineering (CSSE)](https://systems.jhu.edu/) at John Hopkins University (JHU).  

Their [CSSE JHU Dashboard](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) is very good and **major kudos to them** for making the raw data set publicly available [on GitHub](https://github.com/CSSEGISandData).  They started sharing this data in early February, 2020.  This is a daunting task undertaken by JHUs CSSE which becomes all the more clear if you look a the issues log in the GitHub repository.  The (mostly) constructive collaborative effort to update, correct, keep the data set consistent, add data to the data set for more functionality (yes..two mutually exclusive things) is extreme.  As of this writing, almost 900 people are actively watching the repository, over 10,000 people have forked it, and it has almost 20,000 stars.

Many have taken this data, added to it, and shared their own work.

- [JHU Region Mapper](https://github.com/WolfgangFahl/jhuregionmapper)
- [Current COVID-19 Statistics](https://track-coronavir.us/)
- [Covid Trends](https://aatishb.com/covidtrends/)
- [Lucas Czarnecki - COVID-19-CLEANED-JHUCSSE](https://github.com/Lucas-Czarnecki/COVID-19-CLEANED-JHUCSSE)
  - A standard repo dealing with new columns so as to offload that work form the CSSE team
- [COVID19 Live Interactive Dashboard (v3)](https://datastudio.google.com/u/0/reporting/f56febd8-5c42-4191-bcea-87a3396f4508/page/GQFJB) from *Kok Han*

Other (raw) data that is available:

- [WHO](https://who.sprinklr.com/) 
  - Note the download icon on the lower right of the map
- [European Centre for Disease Prevention and Contro](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)l
  - [European data in JSON!!!](https://opendata.ecdc.europa.eu/covid19/casedistribution/json/)
- [New York Times US Data GitHub Repository](https://github.com/nytimes/covid-19-data)

#### What to count

As I tuned in to the conversations around the CSSE JHU data set, it became clear that there is much ongoing discussion about what to count and track.  The data started out with 'Province_State', 'Country_Region', 'Last_Update' ,'Latitude', 'Longitude', 'Confirmed', 'Deaths', and 'Recovered'. In mid March 'FIPS' and 'Admin2' were added to track county information in the US.    

The CSSE JHU data set data set provides this data:

Column Headings of the data set: 
['FIPS' 'Admin2' 'Province_State' 'Country_Region' 'Last_Update' 'Lat'
 'Long_' 'Confirmed' 'Deaths' 'Recovered' 'Active' 'Combined_Key'] *<< this represents a list of column names*

The New York Times provides a subset of the John Hopinks data.

Column Headings of the data set: 
['date' 'state' 'fips' 'cases' 'deaths']

WHO Data set (which needs clean up to be read into Pandas)

Column Headings of the data set: 
['day' 'Country' 'CountryName' 'Region' 'Deaths' 'CumulativeDeaths'
 'Confirmed' 'CumulativeConfirmed']

So basically everyone is tracking, at a minimum, by day:

- Country

- Regional info (State, County, Province, etc.)

- Deaths

- Confirmed

  

#### How we count it

Deaths.  Should that number be the single focus?  

What is noticeably missing is any data on testing.  It may be that the death talley is the focus because that is the only number the media has.  But looking into that number is also uncomfortable and not just for the reasons you think.   How a COVID19 death is counted varies wildly.  And that highlights another issue.  Everyone is counting differently, not only within organizations in the US but across the globe.

See this excellent article which illustrates the disparity and complexity in counting deaths: 
[Coronavirus: Why death and mortality rates differ](https://www.bbc.com/future/article/20200401-coronavirus-why-death-and-mortality-rates-differ).

I believe this complexity exists for every data category tracked.



#### What *should* we be tracking?

My initial analysis based on the CSSE JHU data set showed that comparatively speaking the numbers were not horrific.  Given the situation, I could only conclude that the data being tracked was incomplete.

What else would help to better understand the situation and the risk to us.

- The rate of infection and death or recovery is certainly something to track and there are sites that are now doing that thanks to the CSSE JHU data 
- A quantitative value of number of tested and testing capability is key, I should think.  The lack of data here is worrisome to say the least.  This is so obvious that one can only conclude its not getting any attention because it either does not exist or its so dire it calls into question all the other numbers.
- Some data sets are now including population which I think is a valuable metric.
- A measure of the impact to the healthcare providers is of great interest.

It occurred to me that there had to be data on past flu impacts and I wondered what that data tracked.

The CDC publishes an [annual "flu" report](https://www.cdc.gov/flu/about/burden/2018-2019.html).

Interestingly they track the following data:

- Symptomatic Illnesses
- Medical Visits
- Hospitalizations
- Deaths

across 5 age groups:

- 0-4 yrs
- 5-17 yrs
- 18-49 yrs
- 50-64 yrs
- 65+

This makes perfect sense.  I should think tracking COVID 19 using the same parameters that are used to report on the seasonal flu would be a sound strategy.   If the "flatten the curve" efforts are all about controlling the rate of Medical Visits and Hospitalizations then how can we not be tracking this?   

Data is available from the [American Hospital Association](https://www.aha.org/statistics/fast-facts-us-hospitals) **Fast Facts on US Hospitals** that would allow us to better understand the risk.  For example, in 2018, there were:

- 6,146 hospitals in the US with 
- 924,107 Total Staffed Beds 
- 107,276 Intensive Care Beds and part of that total includes 
  - 7,419 beds categorized as "Other Intensive Care" (assuming we need most of the other)

| [Medical-Surgical   Intensive Care 4 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote4) | 55,663  |
| ------------------------------------------------------------ | ------- |
| [Cardiac   Intensive Care 5 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote5) | 15,160  |
| [Neonatal   Intensive Care 6 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote6) | 22,721  |
| [Pediatric   Intensive Care 7 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote7) | 5,115   |
| [Burn   Care 8 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote8) | 1,198   |
| [Other   Intensive Care 9 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote9) | 7,419   |
|                                                              |         |
|                                                              | 107,276 |

This is the kind of data that would allow us to make informed decisions.  

- What are the chances of the virus killing us? (As an absolute)
- What are the chances of the virus killing us if the appropriate medical care, including medical professionals, tools, and medicine, is not available when we get sick?

But in general all we see are the death totals, and those without any real context.



## Numbers have no context

Lets take a look at some comparisons.  

From COVID19 Data available from the CSSE JHU data set, California had 348 deaths as of 5 April 2020.  According to [Statista.com](https://www.statista.com/statistics/241581/births-and-deaths-in-the-us-by-state/), California had 268,189 deaths in 2017 (the only publicly available data I could find at the time for comparison).   

That results in approximately 22,349 deaths per month via simple division.  

So 348 COVID-19 deaths over approximately 3 months  vs 22,349 deaths/month in California in 2017.

Taking that same data we see that there have been 4159 deaths in New York attributed to COVID19 and in 2017 there were 12,947 deaths/month (155,358 total).

So now I have 348 deaths in California and 4159 deaths in New York in some sort of context.   

At a national level, the [CDC and the National Center for Health Statistics](https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_09-508.pdf) shows 2,813,503 deaths in 2017. That tells me that on average, the US had 234,459 deaths/month in 2017.    The John Hopkins data shows 9619 deaths as of 5 April 2020.

In and of themselves those numbers are not horrifying, but there are questions.

Are these comparisons valid?  Are the COVID19 deaths reported in addition to the expected deaths?

Of the deaths, what percentage had underlying conditions?

There  is no way to look at this and not conclude that we don't have all the numbers. Further, that the numbers we have have no context or are taken out of context.  I understand "I don't know" is not very re-assuring but neither is an incomplete picture, or guesswork.  I'll take "here are the numbers we have today and here are the ones we are working on but right now we don't know" over someones speculation 100% of the time.

My other conclusion is that what is horrifying is the US Medias inability to properly arm us with information at a time when it is most needed.   It a fundamental breakdown of the social contract.

I am in no way an expert in any of this but I understand numbers and trends and absent numbers without agenda, source, or speculation, I'll try to figure it out on my own while keeping in mind Rahm Emanuels haunting comment (the second part) below.

Rahm Emanuel:"You never want a serious crisis to go to waste. And what I mean by that is ***an opportunity to do things you think you could not do before."***




