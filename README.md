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
|     1 | 1st    |         2580760 |              1.245 |
|     1 | 2nd    |        25358365 |              0.963 |
|       |        |                 |                    |
|     2 | 1st    |             479 |              1.891 |
|     2 | 2nd    |             531 |              2.343 |
|       |        |                 |                    |
|     3 | 1st    |       159833790 |              0.633 |
|     3 | 2nd    |        89349241 |              0.433 |
|       |        |                 |                    |
|     4 | 1st    |            2613 |             21.781 |
|     4 | 2nd    |            1905 |              1.632 |
|       |        |                 |                    |
|     5 | 1st    |            5248 |              2.482 |
|     5 | 2nd    |            4507 |              3.197 |
|       |        |                 |                    |
|     6 | 1st    |            5331 |              2.108 |
|     6 | 2nd    |            1812 |            153.548 |
|       |        |                 |                    |
|     7 | 1st    |   3312271365652 |              5.523 |
|     7 | 2nd    | 509463489296712 |             13.588 |
