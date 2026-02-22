# Enterable Template

For enterables, allow special syntax to point to the connector which an actor uses to traverse into the enterable.

`Enterable template ->connector inherited;`

In this context inherited refers to the [Thing Template](thingtemplate.md)

The definition is thus equivalent to

`Enterable template ->connector 'vocabWords' 'name' @location? "desc"?;`
