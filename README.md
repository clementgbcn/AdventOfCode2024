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
|     1 | 1st    |         2580760 |              1.432 |
|     1 | 2nd    |        25358365 |              0.959 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              2.165 |
|     2 | 2nd    |             531 |              2.451 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.94  |
|     3 | 2nd    |        89349241 |              0.451 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             22.743 |
|     4 | 2nd    |            1905 |              1.666 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              2.77  |
|     5 | 2nd    |            4507 |              3.165 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              2.474 |
|     6 | 2nd    |            1812 |            157.167 |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              6.346 |
|     7 | 2nd    | 509463489296712 |             13.901 |
|       |        |                 |                    |
|     8 | 1st    |             344 |              1.363 |
|     8 | 2nd    |            1182 |              0.778 |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             12.087 |
|     9 | 2nd    |   6448168620520 |            161.798 |
|       |        |                 |                    |
|    10 | 1st    |             535 |             10.943 |
|    10 | 2nd    |            1186 |             10.863 |
|       |        |                 |                    |
|    11 | 1st    |          183248 |              2.049 |
|    11 | 2nd    | 218811774248729 |             74.075 |
