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
|     1 | 1st    |         2580760 |              1.224 |
|     1 | 2nd    |        25358365 |              0.932 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              1.776 |
|     2 | 2nd    |             531 |              2.359 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.624 |
|     3 | 2nd    |        89349241 |              0.425 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             21.866 |
|     4 | 2nd    |            1905 |              1.664 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              2.528 |
|     5 | 2nd    |            4507 |              3.167 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              1.687 |
|     6 | 2nd    |            1812 |            156.214 |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              5.752 |
|     7 | 2nd    | 509463489296712 |             13.412 |
|       |        |                 |                    |
|     8 | 1st    |             344 |              0.308 |
|     8 | 2nd    |            1182 |              0.54  |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             11.384 |
|     9 | 2nd    |   6448168620520 |            155.591 |
|       |        |                 |                    |
|    10 | 1st    |             535 |              9.833 |
|    10 | 2nd    |            1186 |             10.065 |
|       |        |                 |                    |
|    11 | 1st    |          183248 |              1.591 |
|    11 | 2nd    | 218811774248729 |             65.534 |
|       |        |                 |                    |
|    12 | 1st    |         1421958 |             66.069 |
|    12 | 2nd    |          885394 |             86.361 |
|       |        |                 |                    |
|    13 | 1st    |           32026 |              1.098 |
|    13 | 2nd    |  89013607072065 |              1.119 |
|       |        |                 |                    |
|    14 | 1st    |       219150360 |              0.849 |
|    14 | 2nd    |            8053 |           2193.75  |
|       |        |                 |                    |
|    15 | 1st    |         1438161 |             11.433 |
|    15 | 2nd    |         1437981 |             16.718 |
|       |        |                 |                    |
|    16 | 1st    |          123540 |           2066.86  |
|    16 | 2nd    |             665 |           2100.14  |
|       |        |                 |                    |
|    17 | 1st    |       404712716 |              0.1   |
|    17 | 2nd    | 202322348616234 |              2.764 |
