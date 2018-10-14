#Introduction
Our warehouse is designed with the needs of artists and music labels/producers in mind. They should be able to perform analytics on the charts with various time and regional granularities. They will need to analyse trends for example the rising popularity of a genre in a specific country or region. The warehouse will also be used to perform more open explorations as we aim to identify the importance of different features in song popularity. This warehouse will therefore need to be focused on large aggregation over time/genre/region/artists and will not contain user specific informations.
Those needs will guide our DW design process, we will use the needs driven approach.

#Typical Queries
| Query Number | Natural language                                                                                 |
|--------------|--------------------------------------------------------------------------------------------------|
| Q1           | What songs were in the top 50 for more than a month in 20XX in France ?                          |
| Q2           | Which pop artists got more than 5 songs in the top 10 this year in the USA ?                     |
| Q3           | How many times the number one artist of the top 50 of the year 2017 has been searched on google ?|
| Q4           | How much song Kanye had in the chart in france this month ? Comparing to in China ?              |
| Q5           | Which artist of the top 50 of July has the most of streams ?                                     |
| Q6           | What is the most popular genre in the last 5 years ?                                             |
| Q7           | What is the average length of a track in the top 50 ?                                            |
| Q8           | What the most popular rap artist in Italy in 2018 ?                                              |
| Q9           | How many google searches for pop artists in 2017 in Germany ?                                    |
| Q10          | How many google searches for the last Taylor Swift album in 2015 in Asia ?                       |

#Workload Table
| Dimensions   | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|--------------|----|----|----|----|----|----|----|----|----|-----|
| track        | X  | X  | X  | X  | X  |    | X  | X  |    | X   |
| week         | X  | X  | X  | X  |    | X  |    |    | X  | X   |
| genre        |    | X  |    |    |    | X  |    | X  | X  |     |
| country      | X  | X  |    | X  |    |    |    | X  | X  | X   |
| Measures     |    |    |    |    |    |    |    |    |    |     |
| rank         | X  | X  | X  | X  | X  | X  |    | X  |    | X   |
| streams      |    |    |    |    | X  |    |    | X  |    |     |
| loundness    |    |    |    |    |    |    |    |    |    |     |
| danceability |    |    |    |    |    |    |    |    |    |     |
| length       |    |    |    |    |    |    | X  |    |    |     |
| hits         |    |    | X  |    |    |    |    |    | X  | X   |

#Formal Workload
#### Q1
```
    CHART_ENTRY[track, month, rank<51, year='20XX']
```
#### Q2
```
    CHART_ENTRY[artist, genre='pop', rank<11, country='USA']
```
#### Q3
```
    GOOGLE_SEARCHES[keyword=CHART_ENTRY[artist, rank=23, year=2017]].sum(hits)
```
#### Q4
```
    CHART_ENTRY[artist='kanye', country='france'].count
```
#### Q5
```
    CHART_ENTRY[artist, month='July'].max(streams)
```
#### Q6
```
    This query has vocation to be answer by our coumpound popularity metric.
```
#### Q7
```

```
#### Q8
```

```
#### Q9
```

```
#### Q10
```

```