#Facts

We describe our database with thoses facts schemas :

###Chart Entry 

![Chart Entry fact](../figures/DF1.svg)

This schema represent the popularity of a song on spotify with the rank by the number of streams.

####Aggregation matrix:

|         | track | country | week  |
|---------|-------|---------|-------|
| rank    | max   | avg     | avg   |
| streams | sum   | sum     | sum   |
| nbEntry | count | count   | count |

**Warning:** We allow n-n relations between tracks and artists this can lead to inconsistencies in some sum agregates.

###Song Features 

![Song Features fact](../figures/DF2.svg)

This fact represent song informations like the song length or the  loudness by genre, years and the song title.

####Aggregation matrix:

|              | track |
|--------------|-------|
| loundness    | avg   |
| danceability | avg   |
| length       | avg   |

