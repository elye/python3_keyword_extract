### Description

This repository has 2 folders
- script 
   - noun_count.py and noun_trend.py
- data 
   - Google IO keynote transcript from 2016 - 2019, 2021 - 2024
   - Google IO Developer  keynote transcript from 2017 - 2019, 2021 - 2024
   - Kotlin Conf 2017 - 2019, 2023 - 2024
   - WWDC 2011 - 2023

### Usage

#### noun_count.py
Find the keywords occurance in Google IO 2024
`python3 ./script/noun_count.py ./data/IO-2024 `

#### nount_trend.py
Find the trend of a certain keyword through Google IO, Google Dev IO and KotlinConf e.g.
`python3 ./script/noun_trend.py kotlin`