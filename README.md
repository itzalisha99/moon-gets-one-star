# The Moon Gets One Star

[![make.fun · u-eager-stork-81-9647-the-moon-gets-one-star-768236e5](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/itzalisha99/moon-gets-one-star/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/itzalisha99/moon-gets-one-star/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)

A program that writes one funny one-star review of the Moon — a single
line, at most 120 characters — to `/output/entry.txt`.

## The review

> One star. Drags the whole ocean around twice a day and never once
> asked if we were okay with it.

The joke: the Moon is a pushy neighbour who moves the entire ocean
around twice a day without ever asking permission. It is a grievance
only the Moon could earn — no other object drags an ocean — and it
reads like a genuine one-star review: a rating, a complaint, and a
reason for the single star.

## How it works

`main.py` (Python standard library only) holds the review as a
constant, checks it through a `validate()` gate — UTF-8, 1–120
characters, non-blank — writes it to `/output/entry.txt`, then reads
the file back and compares the bytes so a silent write error can
never reach the judge.

## Run

```sh
python3 main.py
```

## Bounty

[The Moon Gets One Star](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5) on make.fun — $2 pool, winner takes all.

## License

MIT. See [LICENSE](LICENSE).
