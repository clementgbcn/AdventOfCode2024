# AdventOfCode2024

## Presentation

Advent of Code 2024 solution in Python

Run all the challenges with the command `python -m main -a`

Update the `README.md` `Results` section with `python -m main -r`

## Testing

Run the tests with the command `python -m pytest`

Moreover, you can get the coverage with
```
python -m coverage run -m pytest
python -m coverage html
open htmlcov/index.html
```

# Running Datadog Agent

```
export DD_SERVICE="advent-of-code-2024"
export DD_ENV="prod"
export DD_VERSION=0.1.0
export DD_TRACE_AGENT_URL=http://localhost:8136
export DD_GIT_COMMIT_SHA=$(git rev-parse HEAD)
export DD_GIT_REPOSITORY_URL=$(git config --get remote.origin.url | sed -e 's/:/\//' -e 's/^git@/https:\/\//' -e 's/\.git$//') 
export DD_PROFILING_ENABLE_CODE_PROVENANCE=true
export DD_PROFILING_STACK_V2_ENABLED=true
ddtrace-run -p python -m main -a
```

## Summary
![Results](https://github.com/clementgbcn/AdventOfCode2024/actions/workflows/check_results.yml/badge.svg)


## Results
|   Day | Star   |          Result |   Elapsed Time, ms |
|-------|--------|-----------------|--------------------|
|     1 | 1st    |         2580760 |              1.234 |
|     1 | 2nd    |        25358365 |              0.909 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              1.994 |
|     2 | 2nd    |             531 |              2.422 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.73  |
|     3 | 2nd    |        89349241 |              0.515 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             21.969 |
|     4 | 2nd    |            1905 |              1.738 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              2.591 |
|     5 | 2nd    |            4507 |              3.3   |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              1.63  |
|     6 | 2nd    |            1812 |            155.303 |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              5.66  |
|     7 | 2nd    | 509463489296712 |             13.6   |
|       |        |                 |                    |
|     8 | 1st    |             344 |              0.282 |
|     8 | 2nd    |            1182 |              0.532 |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             11.566 |
|     9 | 2nd    |   6448168620520 |            154.718 |
|       |        |                 |                    |
|    10 | 1st    |             535 |              9.955 |
|    10 | 2nd    |            1186 |             10.013 |
|       |        |                 |                    |
|    11 | 1st    |          183248 |              1.587 |
|    11 | 2nd    | 218811774248729 |             61.604 |
|       |        |                 |                    |
|    12 | 1st    |         1421958 |             67.078 |
|    12 | 2nd    |          885394 |             86.853 |
|       |        |                 |                    |
|    13 | 1st    |           32026 |              1.106 |
|    13 | 2nd    |  89013607072065 |              1.116 |
|       |        |                 |                    |
|    14 | 1st    |       219150360 |              0.834 |
|    14 | 2nd    |            8053 |           2199.74  |
|       |        |                 |                    |
|    15 | 1st    |         1438161 |             11.915 |
|    15 | 2nd    |         1437981 |             17.352 |
|       |        |                 |                    |
|    16 | 1st    |          123540 |           2836.73  |
|    16 | 2nd    |             665 |           2577.44  |
|       |        |                 |                    |
|    17 | 1st    |       404712716 |              0.238 |
|    17 | 2nd    | 202322348616234 |              2.214 |
|       |        |                 |                    |
|    18 | 1st    |             372 |              6.654 |
|    18 | 2nd    |            2907 |             12.087 |
|       |        |                 |                    |
|    19 | 1st    |             302 |            336.28  |
|    19 | 2nd    | 771745460576799 |           1002.32  |
