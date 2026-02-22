# awardPointsOnce

In cases where you want to prevent points being awarded several times for the same feat, you could use awardPointsOnce in preference to [awardPoints](awardpoints.md) and as an alternative to [addToScoreOnce](achievement.md).

```tads3
+++ bronzeBowl : Container 'bronze bowl/vessel' 'bronze bowl'
  "It's of ancient and somewhat curious design, cast with two rows of
    pomegranates all the way round the outside. "
   bulkCapcity = 4
   bulk = 5
   weight = 5
   dobjFor(Take)
   {
     action()
     {
       achievement.awardPointsOnce();
       inherited;
     }
   }
   achievement : Achievement { +3 "recovering the bronze bowl" }
;
```

Once again, note the use of the [Achievement template](achievementtemplate.md) here.
