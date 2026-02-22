# Sense

*class* — defined in [sense.t](../by-file/sense.t.md) (line 104)


Sense: the basic class for senses.


**Superclass chain:** `object` > **SenseGlobal objects:** [sight](sight.md), [smell](smell.md), [sound](sound.md), [touch](touch.md)


## Properties


### `ambienceProp`

Defined in sense.t, line 173

Each sense can define this property to specify a property pointer used to define a Thing's "ambient" energy emissions. Senses which do not use ambient energy should define this to nil.


### `presenceProp`

Defined in sense.t, line 158

Each sense must define the property presenceProp as a property pointer giving the xxxPresence property for the sense. The xxxPresence property is the property of a Thing which determines whether or not the object has a "presence" in this sense, which is to say whether or not the object is emitting any detectable sensory data for the sense. For example, soundPresence indicates whether or not a Thing is making any noise.


### `sizeProp`

Defined in sense.t, line 125

Each sense must define the property sizeProp as a property pointer giving the xxxSize property for the sense. The xxxSize property is the property of a Thing which determines how "large" the object is with respect to the sense. For example, sightSize indicates how large the object is visually, while soundSize indicates how loud the object is.


### `thruProp`

Defined in sense.t, line 111

Each sense must define the property thruProp as a property pointer giving the xxxThru property for the sense. The xxxThru property is the property of a material which determines how the sense passes through that material.


## Methods


### `canObjBeSensed(obj, trans, ambient)`

Defined in sense.t, line 188

Determine if, in general, the given object can be sensed under the given conditions. Returns true if so, nil if not. By default, if the ambient level is zero, we'll return nil; otherwise, if the transparency level is 'transparent', we'll return true; otherwise, we'll consult the object's size:
