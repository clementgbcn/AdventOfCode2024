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
|     1 | 1st    |         2580760 |              1.251 |
|     1 | 2nd    |        25358365 |              0.956 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              1.813 |
|     2 | 2nd    |             531 |              2.312 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.648 |
|     3 | 2nd    |        89349241 |              0.433 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             22.161 |
|     4 | 2nd    |            1905 |              1.782 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              2.565 |
|     5 | 2nd    |            4507 |              3.196 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              1.63  |
|     6 | 2nd    |            1812 |            156.53  |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              5.901 |
|     7 | 2nd    | 509463489296712 |             13.44  |
|       |        |                 |                    |
|     8 | 1st    |             344 |              0.299 |
|     8 | 2nd    |            1182 |              0.571 |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             11.35  |
|     9 | 2nd    |   6448168620520 |            152.785 |
|       |        |                 |                    |
|    10 | 1st    |             535 |              9.88  |
|    10 | 2nd    |            1186 |             10.017 |
|       |        |                 |                    |
|    11 | 1st    |          183248 |              1.583 |
|    11 | 2nd    | 218811774248729 |             60.205 |
|       |        |                 |                    |
|    12 | 1st    |         1421958 |             66.43  |
|    12 | 2nd    |          885394 |             85.956 |
|       |        |                 |                    |
|    13 | 1st    |           32026 |              1.105 |
|    13 | 2nd    |  89013607072065 |              1.109 |
|       |        |                 |                    |
|    14 | 1st    |       219150360 |              0.866 |
|    14 | 2nd    |            8053 |           2232.8   |
|       |        |                 |                    |
|    15 | 1st    |         1438161 |             12.493 |
|    15 | 2nd    |         1437981 |             17.651 |
|       |        |                 |                    |
|    16 | 1st    |          123540 |           2174.31  |
|    16 | 2nd    |             665 |           2152.82  |
|       |        |                 |                    |
|    17 | 1st    |       404712716 |              0.102 |
|    17 | 2nd    | 202322348616234 |              2.249 |
|       |        |                 |                    |
|    18 | 1st    |             372 |              5.985 |
|    18 | 2nd    |            2907 |             11.537 |
