# Analysis of Weather Patterns in Oahu, Hawaii

## Purpose
The purpose of this analysis was to study weather patterns to determine viability of a surf and ice cream shop, Surf's Up, year round. For a business like Surfs Up, weather plays a pivotal role in how much foot traffic is seen and how many sales will be made. In this analysis, two months were chosen (June and December) to analyze weather patterns for multiple weather stations based around Oahu, Hawaii. June and December were chosen due to the typically extreme differences in weather patterns between these two months in order to get a broader picture of how climate might affect business.

## Results

Luckily, Oahu is fairly temperate year round so the differences in weather are quite minor. However, there are some key differences between the two months to consider:

- December will likely see a dip in business on days where temperatures drop lower than usual. With a low of 56, only the extremely dedicated will be likely to go surfing, let alone buy icecream.

- In addition to lower temperatures, there are also spikes in precipitation that can be observed in December's weather patterns compared to June's fairly dry climate.

<p align="center">
<img width="432" height="288" src="https://user-images.githubusercontent.com/85508764/129216858-17916695-760c-4474-84fb-b2f5dfdb9534.png">
</p>

- Finally, the bottom 25% of temperatures in June is slightly higher than that of Decembers. Once again, however, the differences are well within an acceptable range that it won't make a large difference.


## Summary

To reiterate, the differences between June and December are negligble at best and a slight dip in potential business at worse. However, there 10 other months to examine to get a fuller picture of how weather will affect business year-round.

It would be helpful to also examine spring and fall weather patterns through similar functions:


### Function to examine Spring weather (April)
```
temperature = session.query(Measurement.tobs).\
    filter(extract('month', Measurement.date)==4).all()
```

### Function to examine Fall weather (September)

```
temperature = session.query(Measurement.tobs).\
    filter(extract('month', Measurement.date)==9).all()
```
