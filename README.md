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
|     1 | 1st    |         2580760 |              1.266 |
|     1 | 2nd    |        25358365 |              0.974 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              1.784 |
|     2 | 2nd    |             531 |              2.339 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.633 |
|     3 | 2nd    |        89349241 |              0.436 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             21.848 |
|     4 | 2nd    |            1905 |              1.648 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              2.575 |
|     5 | 2nd    |            4507 |              3.107 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              1.585 |
|     6 | 2nd    |            1812 |            151.844 |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              5.522 |
|     7 | 2nd    | 509463489296712 |             13.578 |
|       |        |                 |                    |
|     8 | 1st    |             344 |              0.287 |
|     8 | 2nd    |            1182 |              0.532 |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             11.412 |
|     9 | 2nd    |   6448168620520 |            153.266 |
|       |        |                 |                    |
|    10 | 1st    |             535 |              9.874 |
|    10 | 2nd    |            1186 |              9.993 |
|       |        |                 |                    |
|    11 | 1st    |          183248 |              1.577 |
|    11 | 2nd    | 218811774248729 |             64.008 |
|       |        |                 |                    |
|    12 | 1st    |         1421958 |             66.917 |
|    12 | 2nd    |          885394 |             88.761 |
|       |        |                 |                    |
|    13 | 1st    |           32026 |              1.138 |
|    13 | 2nd    |  89013607072065 |              1.145 |
|       |        |                 |                    |
|    14 | 1st    |       219150360 |              0.92  |
|    14 | 2nd    |            8053 |           2230.49  |
|       |        |                 |                    |
|    15 | 1st    |         1438161 |             10.626 |
|    15 | 2nd    |         1437981 |             16.058 |
