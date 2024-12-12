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
|     1 | 1st    |         2580760 |              1.414 |
|     1 | 2nd    |        25358365 |              1     |
|       |        |                 |                    |
|     2 | 1st    |             479 |              1.836 |
|     2 | 2nd    |             531 |              2.385 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.672 |
|     3 | 2nd    |        89349241 |              0.448 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             22.099 |
|     4 | 2nd    |            1905 |              1.731 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              3.16  |
|     5 | 2nd    |            4507 |              3.343 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              1.588 |
|     6 | 2nd    |            1812 |            155.55  |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              5.906 |
|     7 | 2nd    | 509463489296712 |             13.465 |
|       |        |                 |                    |
|     8 | 1st    |             344 |              0.281 |
|     8 | 2nd    |            1182 |              0.539 |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             11.452 |
|     9 | 2nd    |   6448168620520 |            159.493 |
|       |        |                 |                    |
|    10 | 1st    |             535 |             10.058 |
|    10 | 2nd    |            1186 |             10.51  |
|       |        |                 |                    |
|    11 | 1st    |          183248 |              1.641 |
|    11 | 2nd    | 218811774248729 |             67.922 |
|       |        |                 |                    |
|    12 | 1st    |         1421958 |             63.968 |
|    12 | 2nd    |          885394 |             85.003 |
