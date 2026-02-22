# awardPoints

As an alternative to calling [addToScore](addtoscore.md) or [addToScoreOnce](achievement.md), you can call awardPoints or [awardPointsOnce](awardpointsonce.md) on an Achievement object. This then automatically awards the number of points associated with the Achievement (i.e. defined in the points property of the Achievement object). For example, to have the player awarded 2 points for disposing of the demons, we might change the appropriate ShowTopic thus:

```tads3

++ GiveShowTopic @baarasRoot
   topicResponse
   {
     "As you produce the baaras root and hold it up before their demonic little
       eyes, it starts to glow an eerie pink colour...
      ...
      ...   they
      shimmer and dissolve, turning into plumes of oily black smoke which
      vanishes like a mist. ";
      demons.moveInto(nil);
      achievement.awardPoints();
   }

   achievement : Achievement { +2 "exorcizing the demons" }
;

```

Note that since the demons can only ever be exorcized once, we don't need any checks to prevent the points being awarded several times over. Otherwise, it would be more convenient to use [awardPointsOnce](awardpointsonce.md). Note also the use of the [Achievement template](achievementtemplate.md).

So why do we need awardPoints and awardPointsOnce in addition to addToScore and addToScoreOnce? There are two implications here:

|  | 1. | With awardPoints and awardPointsOnce the Achievement object determines the number of points awarded. With addToScore and addToScoreOnce the function/method call determines the number of points awarded. |
|---|---|---|

|  | 2. | Which set of methods you use can have implications for the calculation of the [maximum score](maxscore.md). |
|---|---|---|
