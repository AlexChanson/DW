#Facts

We describe our database with thoses facts schemas :

###Chart Entry 

![Chart Entry fact](../figures/DF1.svg)

This schema represent the popularity of a song on spotify with the rank by the number of streams.

####Aggregation matrix:

|         | track | country | week  | genre |
|---------|-------|---------|-------|-------|
| rank    | max   | avg     | avg   | max   |
| streams | sum   | sum     | sum   | sum   |
| nbEntry | count | count   | count | count |

###Song Features 

![Song Features fact](../figures/DF2.svg)

This fact represent song informations like the song length or the  loudness by genre, years and the song title.

####Aggregation matrix:

|              | genre | track | week |
|--------------|-------|-------|------|
| loundness    | avg   | avg   | avg  |
| danceability | avg   | avg   | avg  |
| length       | avg   | avg   | avg  |

###Google Searches

![Google Searches fact](../figures/DF3.svg)

 This fact represent the number searches on Google for a song. We chose to keep this fact separate as it is from a different source and it migh be considered without the Chart entries when making queries.

####Aggregation matrix:

|      | track | country | week |
|------|-------|---------|------|
| hits | sum   | sum     | sum  |