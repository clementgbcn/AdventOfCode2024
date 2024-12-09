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
|     1 | 1st    |         2580760 |              1.28  |
|     1 | 2nd    |        25358365 |              0.939 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              1.924 |
|     2 | 2nd    |             531 |              2.373 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.644 |
|     3 | 2nd    |        89349241 |              0.493 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             21.73  |
|     4 | 2nd    |            1905 |              1.876 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              2.528 |
|     5 | 2nd    |            4507 |              3.048 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              2.166 |
|     6 | 2nd    |            1812 |            154.559 |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              5.779 |
|     7 | 2nd    | 509463489296712 |             13.441 |
|       |        |                 |                    |
|     8 | 1st    |             344 |              0.26  |
|     8 | 2nd    |            1182 |              0.543 |
|       |        |                 |                    |
|     9 | 1st    |   6421128769094 |             11.66  |
|     9 | 2nd    |   6448168620520 |            157.747 |
