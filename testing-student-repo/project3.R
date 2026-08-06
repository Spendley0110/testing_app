library(tidyverse)
library(Lahman)
library(table1)
library(scales)


###Topic: Do the awarded players tend to have higher salaries than other players?
###glimpse through three datasets to see what each datatset includes
glimpse(People)
glimpse(AwardsPlayers)
glimpse(Salaries)

###Organizing the awarded players
#I combined the People and AwardsPlayers by playerID so that we can see who received awards.
PlayerswithAwards <- People|>
  left_join(AwardsPlayers, by = "playerID")


#I found that the code above includes all the players that were not awarded.
#To resolve this, I changed the code to have People inside the AwardsPlayers.
PlayerswithAwards <- AwardsPlayers|>
  left_join(People, by = "playerID")


PlayerswithAwards <- PlayerswithAwards |> select(playerID, nameFirst, nameLast, awardID, yearID) |> unique()


###Combining the salary data with PlayerswithAwards and organizing the data
#I combined the PlayerswithAwards and Salaries by playerID so that we can see who received awards.
#However, PlayerswithAwards showed NA for salaries, which is not what I expected.
PlayerswithAwards1 <- PlayerswithAwards|> 
  left_join(Salaries, by = 'playerID') 


#I found that Salaries only have data which is from 1985 to 2016.
Salaries|>
  count(yearID)

#I filtered the PlayerwithAwards to only include data which has yearID between 1985 to 2016
PlayerswithAwards <- PlayerswithAwards |> filter(yearID %in% 1985:2016) |> left_join(Salaries, by = c('playerID', 'yearID')) |> group_by(playerID, nameFirst, nameLast, yearID, salary) |> summarize(awards = paste(unique(awardID), collapse = ','), .groups = 'drop')
#I organized the data by using group_by only for playerID, nameFirst, nameLast, yearID, salary.
#I combined all the different awards in to "awards" by using summarize so that the salary shows only one time.
PlayerswithAwards<- PlayerswithAwards|>
  group_by(playerID, nameFirst, nameLast, yearID, salary)|>
  summarize(awards = paste(unique(awardID), collapse = ","),
            .groups = "drop")
PlayerswithAwards

#I filtered the PlayerswithAwards so that they only have data that excludes data that have NA for salary.
PlayerswithAwards <- PlayerswithAwards|>
  filter(!is.na(salary))
PlayerswithAwards

###Gathering the players that are not awarded and combining the salary data
#I am going to use anti_join for allplayers data and the PlayerswithAwards 
#so that I can have all the other data which is players that weren't awarded and their salaries that year.

AllPlayers <- People |> left_join(Salaries, by = c('playerID')) |> select(playerID, nameFirst, nameLast, yearID, salary) |> filter(!is.na(salary))
PlayerswithoutAwards <- AllPlayers |> anti_join(PlayerswithAwards, by = c('playerID', 'yearID'))
PlayerswithoutAwards


#To make sure that this works, I double checked it using sample slicing.
sample_awards <- PlayerswithAwards |> slice_sample(n = 20)
sample_noawards <- PlayerswithoutAwards |> slice_sample(n = 20)
AllPlayers_sample <- AllPlayers |> slice_sample(n = 50)


###Making the Plot
#mutate column called type that differentiates to Awards and No Awards.
PlayerswithAwards<- PlayerswithAwards|>
  mutate(Type = "Awards")
PlayerswithAwards

PlayerswithoutAwards<- PlayerswithoutAwards|>
  mutate(awards = "None")|>
  mutate(Type = "No Awards")
PlayerswithoutAwards


all_players <- bind_rows(PlayerswithAwards, PlayerswithoutAwards) |> mutate(Type = factor(Type, levels = c('Awards', 'No Awards')))
all_players

#I plotted the graph using all_players using boxplot
#to focus on the main boxplot than the outliers, I used the log10 and used dollar format to show in dollars.
#I added the notch to show the median efficiently.

ggplot(all_players, aes(x = Type, y = salary, fill = Type))+
  geom_boxplot(notch = TRUE)+
  labs(title = "Salaries of the Awarded Players and the Others",
       x = "Type",
       y = "Salaries($)"
       )+
  scale_y_log10(labels = dollar_format())+
  theme_minimal()



ggplot(all_players, aes(x = Type, y = salary, fill = Type)) + geom_boxplot(notch = TRUE) + labs(title = 'Salaries of the Awarded Players and the Others', x = 'Type', y = 'Salaries($)', y = 'Salaries($)' ) + scale_y_log10(labels = dollar_format()) + theme_minimal()
table1(~salary | Type, data = all_players)

all_players$Type <- relevel(as.factor(all_players$Type), ref = 'No Awards')
out <- aov(salary ~ Type, data = all_players)
ci_noawards <- confint(out)

all_players$Type <- relevel(as.factor(all_players$Type), ref = 'Awards')
out <- aov(salary ~ Type, data = all_players)
ci_awards <- confint(out)

summary(out)
#We are 95% confident that the players who received awards earn in the CI(4285375,4527860)
# and the players who did not receive awards earn in the CI(1751743,1837599).
#The summary shows that this data is statistically significant, having the P-value smaller than 0.001.
#Overall, the analysis strongly suggests that award-winning players earn significantly higher salaries than other players.







