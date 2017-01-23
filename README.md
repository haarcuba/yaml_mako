# YAML-MAKO

These are the facts:

* [Mako](http://www.makotemplates.org/) templates are great.
* [YAML](https://en.wikipedia.org/wiki/YAML) is great.

Let's have them both!

# Installation

    $ pip install yaml-mako

# Example

Here's our yaml document, describint a general subscription, say to a newsletter:

```yaml
---
name: "subscription"
details:
    start time: ${start_date}
    end time: ${end_date}
    comment: dates should appear above after temlating
```

If you load this as plain `YAML`, you will get the equivalent of

```python
{'details': {'comment': 'dates should appear above after temlating',
  'end time': '${end_date}',
  'start time': '${start_date}'},
 'name': 'subscription'}
```

Using `yaml-mako` you can to this:

```python
import yaml_mako
import pprint
import datetime

stream = open( 'example.yaml' )
today = datetime.date.today()
oneYearLater = today + datetime.timedelta( 1 )
pprint.pprint( yaml_mako.load( stream, start_date = today, end_date = oneYearLater ) )
```

And we get:

```python
{'details': {'comment': 'dates should appear above after temlating',
             'end time': datetime.date(2017, 1, 24),
             'start time': datetime.date(2017, 1, 23)},
 'name': 'subscription'}
```
