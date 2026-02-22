# Passage Template

For passages, allow special syntax to point to the master side of the passage.

```tads3
Passage template ->masterObject inherited;
```

Here, 'inherited' refers to the Thing or VocabObject template, so this equates to:

```tads3
Passage template -> masterObject;
Passage template -> masterObject 'vocabWords';
Passage template -> masterObject 'vocabWords' 'name' @location? "desc"?
```
