# Using Pandas to look at Pandemic Data

Uncertainty is never comfortable and when the uncertainty relates to a new virus that can infect us and those close to us rather than our computers, lack of comfort can turn into outright fear.

Often numbers can help with uncertainty but sadly the numbers, as they are being reported to us, are suspect, incomplete, and lack context.   I find that troubling and irresponsible.

Since one of my goals during this period of social distancing is to improve my Python skills, what better way to do that (and improve my Pandas skills as well) than to look at the numbers myself.

| Sidebar                                                                                                                                                                              |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| If you can do without yet another persons take on our current situation and want to get right to the numbers, here is the link to the repository I've put together to check numbers: |     |
| [Using Pandas to look at Pandemic Data](https://github.com/cldeluna/pandas_for_pandemic_data) on GitHub                                                                              |     |

## The numbers are suspect

It's always hard to count at any sufficiently large scale so from the start this is a non-trivial problem.  How are cities rolling up data to their counties, the counties to the states, the states to the federal level?  Throw in political agendas and one wonders that we have any numbers at all.

When we do have numbers, their quality and provenance aside, they are often presented to drive agendas.

I guess that has always been true but never at such an egregious level and when the stakes could be so high.

- 56% percent of Californians will be infected in the next 8 weeks?
- 50% of New Yorkers will be infected?

Perhaps saying, "here is what we know so far but we don't know much yet" would lead to panic but I, for one, would prefer it.   On what basis are those claims made?  Since testing is a big problem, how could we even confirm that?   Do I care that 56% of Californians will be infected?  In and of itself that is not enough information.   I do care if that 56% is predominantly in the high risk groups.  I care less about the percentage and much more about the infrastructure required to take care of the percentage that will need medical attention.   That number is not part of the conversation.

My point is that I don't think we are getting the numbers we need to make informed decisions.   

Different organizations are counting different things and counting those things differently.  Are the things that need to be counted being counted?   

#### It all starts with the data

When I decided to use Pandas and Python to look at this data, the first step was actually getting some data.  That effort was an eye opener.

[Worldometers](https://www.worldometers.info) had some wonderful data, all sources identified, and nicely put together but I could not find a way to get to raw data.  I suspect that it is available through their subscription service and kudos to [Worldometers](https://www.worldometers.info) as they are not taking this opportunity, unlike so many others, to drive up subscriptions.  I didn't want to do screen scraping so I decided to use the Worldometers data for comparison.

Eventually I stumbled on to the source of the data that is often cited in the media from [the Center for Systems Science and Engineering (CSSE)](https://systems.jhu.edu/) at **John Hopkins University** (JHU).  

Their [CSSE JHU Dashboard](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) is very good and **major kudos to them** for making the raw data set publicly available [on GitHub](https://github.com/CSSEGISandData)!  They started sharing this data in early February, 2020.  This is a thankless and daunting task undertaken by JHU's CSSE. This becomes all the more clear if you look at the issues log in the GitHub repository.  The (mostly) constructive collaborative effort to update, correct, keep the data set consistent, add data to the data set for more functionality (yes..two mutually exclusive things) is extreme.  As of this writing, almost 900 people are actively watching the repository, over 10,000 people have forked it, and it has almost 20,000 stars.

Many have taken this data and manipulated it to fix issues and share their own work.

- [JHU Region Mapper](https://github.com/WolfgangFahl/jhuregionmapper)
- [Current COVID-19 Statistics](https://track-coronavir.us/)
- [Covid Trends](https://aatishb.com/covidtrends/)
- [Lucas Czarnecki - COVID-19-CLEANED-JHUCSSE](https://github.com/Lucas-Czarnecki/COVID-19-CLEANED-JHUCSSE)
  - A standard repo dealing with new columns so as to offload that work form the CSSE team 
- [COVID19 Live Interactive Dashboard (v3)](https://datastudio.google.com/u/0/reporting/f56febd8-5c42-4191-bcea-87a3396f4508/page/GQFJB) from Kok Han

Other (raw) data is available from:

- [WHO](https://who.sprinklr.com/) 
  - Note the download icon on the lower right of the map
- https://covidtracking.com/api
  - This site offers and API and actually grades states on their data!!!
- [European Centre for Disease Prevention and Contro](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)l
  - [European data in JSON!!!](https://opendata.ecdc.europa.eu/covid19/casedistribution/json/)
- [New York Times US Data GitHub Repository](https://github.com/nytimes/covid-19-data)

I'm in California so I'm very interested in California data and it looks like the California Department of Public Health is doing a good job of sharing the data in machine consumable formats!

- [California COVID-19 Hospital Data and Case Statistics](https://data.chhs.ca.gov/dataset/california-covid-19-hospital-data-and-case-statistics)
  - Check out to see what your Department of Public Health has to offer in terms of raw data

The rest of my family is in Mexico and to date I can't find anything better than screen scraping or going by WHO data.

#### What to count

As I tuned in to the conversations around the CSSE JHU data set, it became clear that there is much ongoing discussion about what to count and how to identify things.  The data started out with 'Province_State', 'Country_Region', 'Last_Update' ,'Latitude', 'Longitude', 'Confirmed', 'Deaths', and 'Recovered'. In mid March 'FIPS' and 'Admin2' were added to track county information in the US.    As of this writing, 'Recovered' is no longer being tracked because its very difficult to do so.  Sadly the data set uses the value "US" in 'Country_Region' but full country names elsewhere rather than standardizing on the [ISO 3166  country codes](https://www.iban.com/country-codes).  That makes it harder to join data sets should you need to.

The CSSE JHU data set data set provides this data:

['FIPS' 'Admin2' 'Province_State' 'Country_Region' 'Last_Update' 'Lat'
 'Long_' 'Confirmed' 'Deaths' 'Recovered' 'Active' 'Combined_Key'] *<< this represents a list of column names*

The New York Times provides a subset of the John Hopkins data.

['date' 'state' 'fips' 'cases' 'deaths']

WHO Data set (which needs clean up to be read into Pandas)

['day' 'Country' 'CountryName' 'Region' 'Deaths' 'CumulativeDeaths'
 'Confirmed' 'CumulativeConfirmed']

So basically everyone is tracking, at a minimum:

- Country
- Regional info (State, County, Province, etc.)
- Deaths
- Confirmed

All over time (typically by day). 

What is noticeably missing is any data on testing in the US.

[Worldometers](https://www.worldometers.info) is counting critical cases as well as totals and new (additional from previous day) so we can map out trends.   Critical cases speaks directly to the medical infrastructure question and so is key, in my mind.

The [French Department of Public Health](https://www.santepubliquefrance.fr/maladies-et-traumatismes/maladies-et-infections-respiratoires/infection-a-coronavirus/articles/infection-au-nouveau-coronavirus-sars-cov-2-covid-19-france-et-monde) is tracking much more hospitalization data although there is some debate right now around how they are counting confirmed cases and it may be that the confirmed number actually contains confirmed and suspected cases.   They specifically track "at risk" communities (the elderly and those in care facilities).

![infog_coronavirus_060420](./images/infog_coronavirus_060420.jpg)

#### How we count it

So the current debate about the numbers from France highlights this next issue.    How are the counts calculated?  

Lets take our most predominant measure, "deaths".

Looking into that number is uncomfortable and not just for the obvious reasons.   How a COVID19 death is counted *varies wildly*.   Everyone is counting differently, not only within organizations but across the globe, making it even more difficult to understand what is happening.  If I die from a pre-existing condition but die while infected with COVID-19 do we count that as a COVID-19 death?  It is far more nuanced than I could have ever imagined.  See this excellent article which illustrates the disparity and complexity in counting deaths: 
[Coronavirus: Why death and mortality rates differ](https://www.bbc.com/future/article/20200401-coronavirus-why-death-and-mortality-rates-differ).

I believe this complexity exists, to varying degrees, for every data category tracked.

In addition to how the numbers are calculated, the physical tracking of the actual data is a huge undertaking and I've not seen much of that mentioned in the media.   As you saw from my personal example, numbers are available but not in any consistent format.  To look at California, I was able to do a simple download of the data.  To look at data for Mexico I either have to trust data that is machine consumable from other sources or parse the web page that has the data I want myself.   That is why the CSSE JHU data set is so impressive.

These are not "sexy" questions, I realize, and pale in comparison to "how many dead" but they are important ones that don't get much play.

#### What *should* we be tracking?

My initial analysis based on the CSSE JHU data set showed that comparatively speaking the numbers were not horrific.  Given the situation, I could only conclude that the data being tracked or at least being discussed was incomplete.

What else would help to better understand the situation and the risk to us?

- The rate of infection and death or recovery is certainly something to track and there are sites that are now doing that many based on the CSSE JHU data 
  - I'd like to see rate of infection broken out by age groups
- A quantitative value of number of tested and testing capability is key, I should think.  The lack of data here is worrisome to say the least.  This is so obvious that one can only conclude its not getting any attention because it either does not exist or its so dire it calls into question all the other numbers.
- Some data sets are now including population which I think is a valuable metric.
- A measure of the impact to the medical infrastructure is absolutely critical

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

Data is available from the [American Hospital Association](https://www.aha.org/statistics/fast-facts-us-hospitals) **Fast Facts on US Hospitals** that would allow us to better understand the risk in overrunning our medical system and our medical professionals.  

For example, in 2018, there were:

- 6,146 hospitals in the US with 
- 924,107 Total Staffed Beds 
- 107,276 Intensive Care Beds and part of that total includes 
  - 7,419 beds categorized as "Other Intensive Care" (assuming we need most of the other)

| [Medical-Surgical   Intensive Care 4 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote4) | 55,663  |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------- |
| [Cardiac   Intensive Care 5 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote5)          | 15,160  |
| [Neonatal   Intensive Care 6 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote6)         | 22,721  |
| [Pediatric   Intensive Care 7 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote7)        | 5,115   |
| [Burn   Care 8 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote8)                       | 1,198   |
| [Other   Intensive Care 9 Beds in Community Hospitals](https://www.aha.org/statistics/fast-facts-us-hospitals#footnote9)            | 7,419   |
|                                                                                                                                     |         |
|                                                                                                                                     | 107,276 |

This is the kind of data that would allow us to make informed decisions.  

- What are the chances of the virus killing us (broken out by age group and perhaps some demographics)? 
- What are the chances of the virus killing us if the appropriate medical care, including medical professionals, tools, and medicine, is not available when we get sick?

## Numbers have no context

Lets take a look at some comparisons.  

From COVID19 Data available from the CSSE JHU data set, California had 348 deaths as of 5 April 2020.  According to [Statista.com](https://www.statista.com/statistics/241581/births-and-deaths-in-the-us-by-state/), California had 268,189 deaths in 2017 (the only publicly available data I could find at the time for comparison).   

That results in approximately 22,349 deaths per month via simple division.  

So 348 COVID-19 deaths over approximately 3 months  vs 22,349 deaths/month in California in 2017.

Taking that same data set, we see that there have been 4159 deaths in New York attributed to COVID19 and in 2017 there were 12,947 deaths/month (155,358 total).

So now I have 348 deaths in California and 4159 deaths in New York in some sort of context.   

At a national level, the [CDC and the National Center for Health Statistics](https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_09-508.pdf) shows 2,813,503 deaths in 2017. That tells me that on average, the US had 234,459 deaths/month in 2017.    The John Hopkins data shows 9619 deaths as of 5 April 2020.

In and of themselves those numbers are not horrifying, but there are questions.

Are these comparisons valid?  Are the COVID19 deaths reported in addition to the expected deaths?  What is the rate of increase?

Of the deaths, what percentage had underlying conditions?

## Final Thoughts

There  is no way to look at this and not conclude that **we don't have all the data**.  I understand "*I don't know*" is not very re-assuring but neither is an incomplete picture, or guesswork presented as anything other than that.  

I'll take "*here are the numbers we have today and here are the ones we are working on but right now we don't know*" over speculation (couched as fact) 100% of the time. 

I am in no way an expert in any of this but I understand numbers and trends and absent numbers without agenda, source, or speculation, I'll try to figure it out on my own.   I think looking at the data has helped me to appreciate the issues and ask better questions.  Isn't that what data is all about?

If you want to look at the data yourself, as I mentioned,  I've put together a small repository to get you started using Python and Pandas.

[Using Pandas to look at Pandemic Data](https://github.com/cldeluna/pandas_for_pandemic_data) on GitHub