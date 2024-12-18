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
|     1 | 1st    |         2580760 |              1.231 |
|     1 | 2nd    |        25358365 |              0.923 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              1.763 |
|     2 | 2nd    |             531 |              2.327 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.63  |
|     3 | 2nd    |        89349241 |              0.443 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             21.813 |
|     4 | 2nd    |            1905 |              1.663 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              2.471 |
|     5 | 2nd    |            4507 |              3.301 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              1.645 |
|     6 | 2nd    |            1812 |            155.255 |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              5.91  |
|     7 | 2nd    | 509463489296712 |             14.382 |
|       |        |                 |                    |
|     8 | 1st    |             344 |              0.273 |
|     8 | 2nd    |            1182 |              0.538 |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             12.091 |
|     9 | 2nd    |   6448168620520 |            162.118 |
|       |        |                 |                    |
|    10 | 1st    |             535 |             10.015 |
|    10 | 2nd    |            1186 |             10.17  |
|       |        |                 |                    |
|    11 | 1st    |          183248 |              1.698 |
|    11 | 2nd    | 218811774248729 |             69.531 |
|       |        |                 |                    |
|    12 | 1st    |         1421958 |             67.3   |
|    12 | 2nd    |          885394 |             86.618 |
|       |        |                 |                    |
|    13 | 1st    |           32026 |              1.105 |
|    13 | 2nd    |  89013607072065 |              1.118 |
|       |        |                 |                    |
|    14 | 1st    |       219150360 |              0.841 |
|    14 | 2nd    |            8053 |           2314.91  |
|       |        |                 |                    |
|    15 | 1st    |         1438161 |             11.266 |
|    15 | 2nd    |         1437981 |             16.772 |
|       |        |                 |                    |
|    16 | 1st    |          123540 |           2074.96  |
|    16 | 2nd    |             665 |           2048.27  |
|       |        |                 |                    |
|    17 | 1st    |       404712716 |              0.099 |
|    17 | 2nd    | 202322348616234 |              2.201 |
|       |        |                 |                    |
|    18 | 1st    |             372 |              5.98  |
|    18 | 2nd    |            2907 |            185.011 |
