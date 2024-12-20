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
|     1 | 1st    |         2580760 |              1.588 |
|     1 | 2nd    |        25358365 |              0.977 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              2.412 |
|     2 | 2nd    |             531 |              2.509 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              1.286 |
|     3 | 2nd    |        89349241 |              0.484 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             23.074 |
|     4 | 2nd    |            1905 |              1.838 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              3.004 |
|     5 | 2nd    |            4507 |              3.226 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              2.11  |
|     6 | 2nd    |            1812 |            161.645 |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              6.475 |
|     7 | 2nd    | 509463489296712 |             14.326 |
|       |        |                 |                    |
|     8 | 1st    |             344 |              0.669 |
|     8 | 2nd    |            1182 |              0.598 |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             12.335 |
|     9 | 2nd    |   6448168620520 |            163.938 |
|       |        |                 |                    |
|    10 | 1st    |             535 |             11.15  |
|    10 | 2nd    |            1186 |             10.638 |
|       |        |                 |                    |
|    11 | 1st    |          183248 |              2.258 |
|    11 | 2nd    | 218811774248729 |             68.95  |
|       |        |                 |                    |
|    12 | 1st    |         1421958 |             72.604 |
|    12 | 2nd    |          885394 |             93.538 |
|       |        |                 |                    |
|    13 | 1st    |           32026 |              1.688 |
|    13 | 2nd    |  89013607072065 |              1.223 |
|       |        |                 |                    |
|    14 | 1st    |       219150360 |              1.114 |
|    14 | 2nd    |            8053 |           2232.18  |
|       |        |                 |                    |
|    15 | 1st    |         1438161 |             12.02  |
|    15 | 2nd    |         1437981 |             16.938 |
|       |        |                 |                    |
|    16 | 1st    |          123540 |           2153.43  |
|    16 | 2nd    |             665 |           2060.43  |
|       |        |                 |                    |
|    17 | 1st    |       404712716 |              0.346 |
|    17 | 2nd    | 202322348616234 |              2.088 |
|       |        |                 |                    |
|    18 | 1st    |             372 |              6.275 |
|    18 | 2nd    |            2907 |             11.446 |
|       |        |                 |                    |
|    19 | 1st    |             302 |            317.113 |
|    19 | 2nd    | 771745460576799 |            914.861 |
|       |        |                 |                    |
|    20 | 1st    |            1343 |             50.094 |
|    20 | 2nd    |          982891 |           1008.37  |
