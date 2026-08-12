#Bringing the API data to Rscript
######
#install rfema package
install.packages("rfema", repos = "https://ropensci.r-universe.dev")

#use library to pull the packages.
library(dplyr)
library(tidyverse)
library(lubridate)
library(rfema)

fema_df <- open_fema(data_set = "DisasterDeclarationsSummaries")
# Enter 1 to get the data.
fema_df <- fema_df[1, ]
######


# Check structure
glimpse(fema_df)

#Organize the original data
#Filter the state, declaration date, and incidentType.
fema_df<- fema_df|>
  select(state, declarationDate,incidentType)



#I made a new column that has only the month. 
fema_df <- fema_df |> 
  mutate(month = month(declarationDate, label = TRUE, abbr = TRUE))

# Remove redundant operations
fema_df <- fema_df |> select(state, month, incidentType)

#I viewed what kind of incidentTypes there are in this data.
unique(fema_df$incidentType)

#I recognized that there are incidentTypes that are not natural disasters.
# List of non-natural disaster categories to exclude
non_natural <- c(
  "Biological",
  "Human Cause",
  "Terrorist",
  "Toxic Substances",
  "Chemical",
  "Dam/Levee Break",
  "Fishing Losses",
)
# Define non-natural disaster categories to exclude
define_non_natural_disasters <- function() {
  c(
    "Biological",
    "Human Cause",
    "Terrorist",
    "Toxic Substances",
    "Chemical",
    "Dam/Levee Break",
    "Fishing Losses"
  )
}

non_natural <- define_non_natural_disasters()

# Filter them out
fema_df <- fema_df |> filter(!(incidentType %in% non_natural))
  )

#I viewed what states there are in this data.
unique(fema_df$state)

#I sorted the states into different regions:
# U.S. Census-defined regions:
northeast <- c("CT","ME","MA","NH","RI","VT","NJ","NY","PA")
midwest   <- c("IL","IN","MI","OH","WI","IA","KS","MN","MO","NE","ND","SD")
south     <- c("DE","FL","GA","MD","NC","SC","VA","WV",
               "AL","KY","MS","TN",
               "AR","LA","OK","TX")
west      <- c("AZ","CO","ID","MT","NV","NM","UT","WY",
               "AK","CA","HI","OR","WA")
territories <- c("DC", "PR", "GU", "AS", "VI", "MP", "FM", "MH", "PW")


# Adding region column based on state
fema_df <- fema_df |>
  mutate(region = case_when(
    state %in% northeast ~ "Northeast",
    state %in% midwest   ~ "Midwest",
    state %in% south     ~ "South",
    state %in% west      ~ "West",
    state %in% territories ~ "Territories",
  ))


##Sort the month into. four seasons, just to know what season it occurred.
#(Dec-Jan: winter, Mar-May:spring, Jun-Aug: summer, Sep-Nov: fall)

fema_df<-fema_df |>
  mutate(season = case_when(
    month %in% c("Dec", "Jan", "Feb") ~ "Winter",
    month %in% c("Mar", "Apr", "May") ~ "Spring",
    month %in% c("Jun", "Jul", "Aug") ~ "Summer",
    month %in% c("Sep", "Oct", "Nov") ~ "Fall"
  ))

#I would like to 4 multi panels divded by seasons 
#and inside each panels, it has points about incidentType and state,
# and the color shows the frequency of it like as a heatmap.

# Define a function to create the heatmap plot
define_heatmap_plot <- function(data) {
  ggplot(data, aes(x = region, y = disaster_group, fill = count)) + 
    geom_tile(color = "white") + 
    facet_wrap(~season, scale = "free")+
    scale_fill_viridis_c(option = "plasma") + # Color gradient indicates frequency
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    labs(
      title = "Frequency of Natural Disasters by Region and Season",
      x = "Region",
      y = "Incident Type",
      caption = "Source: FEMA OpenFEMA API, Disaster Declarations Summaries (v2), accessed Dec 13, 2025.",
      fill = "Count"
    )
}

# Create the heatmap plot
define_heatmap_plot(fema_count)
