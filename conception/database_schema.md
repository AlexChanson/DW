# Table diagrams


Since we plan on using Mondarian with a classical relational database as the backend of our project we have converted our multidimentional schema into a star of tables.

###Chart Entry

![Chart Entry](../figures/ER1.svg)

#### Foreign Keys
**track_id** in **Chart_Entry** refers to **track_id** in **Track**  
**week_id** in **Chart_Entry** refers to **week_id** in **Weeks**  
**country_id** in **Chart_Entry** refers to **country_id** in **Country**  
**country_id** in **Artist** refers to **country_id** in **Country**  


###Song Features

![Song Features](../figures/ER2.svg)

##### Foreign Keys
**track_id** in **Song_features** refers to **track_id** in **Track**


