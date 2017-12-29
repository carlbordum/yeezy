# yeezy
Password phrases are _the_ way the to stay safe online. Who better to say the phrase than beloved street poet Kanye "Yeezy" West?

```
$ pip install git+https://github.com/Zaab1t/yeezy
$ yeezy 10
cremate move downtown cop a sweet space livin life like
$ yeezy 9
grab a red bull and sip slow sip slow
$ yeezy 8
bad as shit but you need to stop
```

With yeezy you can generate password phrases with a Kanye West-based markov chain!


## Why pass phrases?
Your password is most likely 8 characters, where the two middle ones are numbers.

If you add constraints it is easier for a computer to iterate over possible passwords. That's why it is considered bad practice to force any other restriction (such as uppercase or numbers) than length. Computers are good at patterns (generating by rules), but they cannot deal with the exponential complexity of a long password.

Luckily humans are good at remembering silly phrases :)

This legendary dataset is from [Kaggle](https://www.kaggle.com/viccalexander/kanyewestverses).
