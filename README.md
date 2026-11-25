# Have You Tried Turning It Off?

[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![Rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/vickyair1/u-motasimfuad-have-you-tried-turning-it-off-154a938b/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![Reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/vickyair1/u-motasimfuad-have-you-tried-turning-it-off-154a938b/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

A single funny line, under 200 characters, that a hopeless tech support agent says to a desperate customer — an entry for the [make.fun bounty "Have You Tried Turning It Off?"](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b).

## The entry

> Great news — I've escalated your case to our senior technician. That's me in a different headset, so please hold while I google it.

131 characters. The joke: the agent "escalates" to a senior technician who is just the same agent in a different headset, then cheerfully admits he is going to google the problem. The humour is the agent's cheerful uselessness — never the customer — and the twist lands in the last words.

## How it works

`main.py` (Python 3.13) deterministically writes the line to `/output/entry.txt` with no trailing newline, after gate-checking it the way the sealed scorer does (1–199 chars, valid UTF-8, not only whitespace). The output is byte-identical across runs.

```sh
python3 main.py
# entry written to /output/entry.txt: 131 chars
```

## License

MIT — see [LICENSE](LICENSE).
