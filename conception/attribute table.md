\begin{table}[]
\begin{tabular}{lllll}
Attribute   & Description                                                                                          & M   & D   & O   \\
artist      & agregation by artist                                                                                 & no  & yes & no  \\
album       & agregation by album                                                                                  & no  & yes & no  \\
title       & the title of the song (ex "Master of puppets")                                                       & no  & no  & yes \\
week        & a chart entry (eg a song beeing n?1 or 12) is valid for a week this will be our finest time agragate & no  & yes & no  \\
month       & time aggreagation                                                                                    & no  & yes & no  \\
years       & time aggreagation                                                                                    & no  & yes & no  \\
genre       & The genre of the music (eg Pop, rock, classic death metal ...)                                       & no  & yes & no  \\
rank        & The rank of the music in a chart (from 1 to 200)                                                     & yes & no  & no  \\
streams     & how many time the music was listened to                                                              & yes & no  & no  \\
years       & year of publication of the song                                                                      & no  & yes & no  \\
loudness    & general volume of the song                                                                           & yes & no  & no  \\
dancability & how dancable is the song (from 0 to 1)                                                               & yes & no  & no  \\
length      & length of song                                                                                       & yes & no  & no  \\
hits        & number of google searches for a specific song                                                        & yes & no  & no  \\
country     & agregation by country                                                                                & no  & yes & no  \\
region      & agregate by subcontinent (ex north america)                                                          & no  & yes & no  \\
track       & agregate by specific song                                                                            & no  & yes & no 
\end{tabular}
\end{table}