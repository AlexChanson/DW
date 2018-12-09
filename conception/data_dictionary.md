| Attribute    | Description                                                                                           | M   | D   | O   |
|--------------|-------------------------------------------------------------------------------------------------------|-----|-----|-----|
| artist       | agregation by artist, who played a part in the track                                                  | no  | yes | no  |
| album        | agregation by album, that contains the track                                                          | no  | yes | no  |
| title        | the title of the song (ex "Master of puppets")                                                        | no  | no  | yes |
| week         | a chart entry (eg a song beeing n?1 or 12) is valid for a week this will be our finest time agragate  | no  | yes | no  |
| month        | time aggreagation, we will use the 544 cycle                                                          | no  | yes | no  |
| years        | time aggreagation                                                                                     | no  | yes | no  |
| decade       | time agregation, classifing music by decade is very common                                            | no  | yes | no  |
| genre        | The genre of the artist (eg pop, rock, classic, death metal ...)                                      | no  | yes | no  |
| rank         | The rank of the music in a chart (from 1 to 200)                                                      | yes | no  | no  |
| streams      | how many time the music was listened to on spotify                                                    | yes | no  | no  |
| loudness     | general volume of the song                                                                            | yes | no  | no  |
| dancability  | how dancable is the song (from 0 to 1)                                                                | yes | no  | no  |
| length       | length of song in ms                                                                                  | yes | no  | no  |
| country      | agregation by country, ie the country where the chart entry holds true                                | no  | yes | no  |
| region       | agregate by subcontinent (ex north america)                                                           | no  | yes | no  |
| track        | agregate by specific song                                                                             | no  | yes | no  |
| entryNb      | used to count chart entries, always 1 for primary events                                              | yes | no  | no  |
| popularity   | Measures the popularity of a song, will be computed and added in second semester                      | yes | no  | no  |
| release_year | The year the song was released                                                                        | no  | yes | no  |
| followers    | The follower count by slices (0 to 10K, 10K to 100K, 100K to 1M, 1M to 2M, 2M to 3M, 3M to 5M, > 5M)  | no  | yes | no  |
