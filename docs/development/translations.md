# Translations

NetPoint coordinates all translation work using the [Transifex](https://explore.transifex.com/khulnasoft/netpoint/) platform. Signing up for a Transifex account is free.

All language translations in NetPoint are generated from the source file found at `netpoint/translations/en/LC_MESSAGES/django.po`. This file contains the original English strings with empty mappings, and is generated as part of NetPoint's release process. Transifex updates source strings from this file on a recurring basis, so new translation strings will appear in the platform automatically as it is updated in the code base.

Reviewers log into Transifex and navigate to their designated language(s) to translate strings. The initial translation for most strings will be machine-generated via the AWS Translate service. Human reviewers are responsible for reviewing these translations and making corrections where necessary.

Immediately prior to each NetPoint release, the translation maps for all completed languages will be downloaded from Transifex, compiled, and checked into the NetPoint code base by a maintainer.

## Updating Translation Sources

To update the English `.po` file from which all translations are derived, use the `makemessages` management command:

```nohighlight
./manage.py makemessages -l en
```

Then, commit the change and push to the `develop` branch on GitHub. After some time, any new strings will appear for translation on Transifex automatically.

## Proposing New Languages

If you'd like to add support for a new language to NetPoint, the first step is to [submit a GitHub issue](https://github.com/khulnasoft/netpoint/issues/new?assignees=&labels=type%3A+translation&projects=&template=translation.yaml) to capture the proposal. While we'd like to add as many languages as possible, we do need to limit the rate at which new languages are added. New languages will be selected according to community interest and the number of volunteers who sign up as translators.

Once a proposed language has been approved, a NetPoint maintainer will:

* Add it to the Transifex platform
* Designate one or more reviewers
* Create the initial machine-generated translations for review
* Add it to the list of supported languages
